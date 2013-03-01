#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "python-%s-docs-html" % get.srcVERSION()
docdir = "/%s/%s/html" % (get.docDIR(), get.srcNAME())


def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    pisitools.insinto(docdir, "*")
    pisitools.removeDir("%s/_sources" % docdir)

    fixperms(os.path.join(get.installDIR(), docdir.lstrip("/")))

    pisitools.dodir("/etc/env.d")
    shelltools.echo("%s/etc/env.d/50python-docs" % get.installDIR(), "PYTHONDOCS=%s/library" % docdir)

