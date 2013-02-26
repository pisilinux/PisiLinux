#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

DB_FILE = "/var/lib/mlocate/mlocate.db"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists(DB_FILE):
        os.system("/bin/touch %s" % DB_FILE)

    os.system("/bin/chown -R root:slocate /var/lib/mlocate")
    os.system("/bin/chown root:slocate /usr/bin/updatedb")
    os.system("/bin/chown root:slocate /usr/bin/locate")
    os.system("/bin/chmod g+s /usr/bin/locate")
