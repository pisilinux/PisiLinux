#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "cakephp-%s" % get.srcVERSION()
BASEDIR = "/usr/share/php5/cakephp"

def install():
    pisitools.insinto(BASEDIR, "*")
    pisitools.insinto(BASEDIR, ".htaccess")

    # Remove redundant 'empty' and bat files shipped with archive
    for root, dirs, files in os.walk("%s%s" %(get.installDIR(), BASEDIR)):
        for name in files:
            if name == "empty":
                shelltools.unlink(os.path.join(root, name))
    pisitools.remove("%s/cake/console/cake.bat" % BASEDIR)

    pisitools.dosym("%s/cake/console/cake" % BASEDIR, "/usr/bin/cake")

    # Move the tmp dir into /var/tmp
    pisitools.domove("%s/app/tmp/*" % BASEDIR, "/var/tmp/cakephp")
    pisitools.removeDir("%s/app/tmp" % BASEDIR)
    pisitools.dosym("/var/tmp/cakephp", "%s/app/tmp" % BASEDIR)

    # To make access to log files easier
    pisitools.dosym("/var/tmp/cakephp/logs", "/var/log/cakephp")

    pisitools.dodoc("README", "cake/LICENSE.txt", "cake/VERSION.txt")

    # Remove redundant doc files
    for f in ("README", "cake/LICENSE.txt", "cake/VERSION.txt"):
        pisitools.remove("%s/%s" % (BASEDIR, f))
