#!/usr/bin/python

import os
import time
import shutil
import subprocess, signal

PIDFILE = "/run/mysqld/mysqld.pid"
SOCKFILE = "/run/mysqld/mysqld.sock"
TMPFILE = "/tmp/pisilinux.sql"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if fromRelease in [str(r) for r in range(1,4)]:
        os.system("rm -rf /var/lib/mysql/*")
        os.remove("/etc/mysql/my.cnf")
        shutil.copy2("/etc/mysql/my.cnf.newconfig", "/etc/mysql/my.cnf")
        os.remove("/etc/mysql/my.cnf.newconfig")

    os.system("/bin/chown -R mysql:mysql /var/lib/mysql")
    os.system("/bin/chmod -R 0750 /var/lib/mysql")

    os.system("/bin/chown -R mysql:mysql /var/log/mysql")
    os.system("/bin/chmod 0750 /var/log/mysql")
    os.system("/bin/chmod -R 0660 /var/log/mysql/*")

    os.system("/bin/chown -R mysql:mysql /run/mysqld")
    os.system("/bin/chmod -R 0755 /run/mysqld")

    if os.path.exists("/var/rundirs/mysqld"):
        os.system("/bin/chown -R mysql:mysql /var/rundirs/mysqld")
        os.system("/bin/chmod -R 0755 /var/rundirs/mysqld")

    # On first install...
    if not os.path.exists("/var/lib/mysql/mysql"):
        # Create the database
        os.system("/usr/bin/mysql_install_db --datadir=/var/lib/mysql --basedir=/usr --user=mysql --force")

        # Run MySQL
        subprocess.Popen(['/usr/sbin/mysqld', '--user=mysql', '--skip-grant-tables', '--basedir=/usr', '--datadir=/var/lib/mysql', '--max_allowed_packet=8M', '--net_buffer_length=16K', '--socket=%s' % SOCKFILE, '--pid-file=%s' % PIDFILE])

        # Sleep for a while
        time.sleep(2)

        # Delete empty user
        sql = "DELETE FROM mysql.user WHERE USER=''"
        os.system("/usr/bin/mysql --socket=%s \
                                  -hlocalhost \
                                  -e \"%s\"" % (SOCKFILE, sql))

        # Generate timezones
        os.system("/usr/bin/mysql_tzinfo_to_sql /usr/share/zoneinfo > %s" % TMPFILE)

        # Generate help tables
        os.system("/bin/cat /usr/share/mysql/fill_help_tables.sql >> %s" % TMPFILE)

        # Load generated SQL script
        os.system('/usr/bin/mysql --socket=%s \
                                  -hlocalhost \
                                  -uroot \
                                  mysql < %s' % (SOCKFILE, TMPFILE))

        # Stop MySQL
        p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            if 'mysqld' in line: os.kill(int(line.split(None, 1)[0]), signal.SIGKILL)

        # Remove temporary SQL script
        os.unlink("/tmp/pisilinux.sql")
