#!/usr/bin/python

import os, re
import shutil

OUR_ID = 794
OUR_NAME = "mysql"
OUR_DESC = "mysql"

DATADIR = "/var/lib/mysql"
DATADIRMODE = 0755

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    try:
        os.system ("groupadd -g %d %s" % (OUR_ID, OUR_NAME))
        os.system ("useradd -m -d /var/lib/mysql -r -s /bin/false -u %d -g %d %s -c %s" % (OUR_ID, OUR_ID, OUR_NAME, OUR_DESC))
    except:
        pass


    os.system("/sbin/mudur_tmpfiles.py /usr/lib/tmpfiles.d/mariadb.conf")
    
        # Create the database
    os.system("/bin/chown -R mysql:mysql %s" % DATADIR)
    os.system("/bin/chown -R mysql:mysql /var/log/mysqld.log")
    os.system("/usr/bin/mysql_install_db --user=mysql --datadir=/var/lib/mysql --basedir=/usr --force")
    os.system("/usr/bin/mysql_upgrade --force")

    # On first install...
    if not os.path.exists(DATADIR):
        os.makedirs(DATADIR, DATADIRMODE)
        

def postRemove():
    try:
        os.system ("userdel %s" % OUR_NAME)
        os.system ("groupdel %s" % OUR_NAME)
    except:
        pass
