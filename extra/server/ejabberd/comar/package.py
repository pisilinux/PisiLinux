#!/usr/bin/python

import os
import time
import shutil
import tempfile

permissions = {
                "/etc/ejabberd"                             :   ["0750", "ejabberd:ejabberd"],
                "/etc/ejabberd/ejabberd.cfg"                :   ["0640", "ejabberd:ejabberd"],
                "/etc/ejabberd/ejabberdctl.cfg"             :   ["0640", "ejabberd:ejabberd"],
                "/etc/ejabberd/inetrc"                      :   ["0640", "ejabberd:ejabberd"],
                "/var/lib/ejabberd"                         :   ["0750", "ejabberd:ejabberd"],
                "/var/lib/ejabberd/spool"                   :   ["0750", "ejabberd:ejabberd"],
                "/var/lock/ejabberdctl"                     :   ["0750", "ejabberd:ejabberd"],
                "/var/log/ejabberd"                         :   ["0750", "ejabberd:ejabberd"],
                "/usr/lib/ejabberd/priv/bin/epam"           :   ["4750", "root:ejabberd"],
                "/usr/sbin/ejabberdctl"                     :   ["0755", "root:ejabberd"],
            }

def backup():

    def ctl(*cmd):
        return os.system("/usr/sbin/ejabberdctl %s" % " ".join(cmd))

    # Backup DB in every upgrade
    if ctl("status") == 0:
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%S")
        backup_dir = tempfile.mkdtemp(prefix="ejabberd-%s." % timestamp,
                                      dir="/var/tmp")
        backup_file = os.path.join(backup_dir, "ejabberd-database")
        os.system("/bin/chown ejabberd:ejabberd %s" % backup_dir)
        ctl("backup", backup_file)

        if os.path.exists(backup_file):
            os.system("/bin/chmod 700 %s" % backup_dir)
        else:
            shutil.rmtree(backup_dir)

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    #backup()

    # Create certificate if it doesn't exist
    os.system("/etc/ejabberd/self-cert.sh")

    # fix cookie path (since ver. 2.1.0 cookie stored in /var/lib/ejabberd/spool
    # rather than in /var/lib/ejabberd
    cookie_file = ".erlang.cookie"
    if os.path.exists("/var/lib/ejabberd/%s" % cookie_file):
        shutil.copy2("/var/lib/ejabberd/%s" % cookie_file,
                     "/var/lib/ejabberd/spool/%s" % cookie_file)

    for _file, perms in permissions.items():
        if os.path.exists(_file):
            os.system("/bin/chown -R %s %s" % (perms[1], _file))
            os.system("/bin/chmod %s %s" % (perms[0], _file))
