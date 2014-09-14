#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "Markdown-%s" % get.srcVERSION()

extensions = "%s/%s/extensions" % (get.docDIR(), get.srcNAME())
# egg-info dir
eggDir = "/usr/lib/python2.7/site-packages/markdown-%s-py2.7.egg-info" % get.srcVERSION()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    # For creating egg-info
    pisitools.dodir("%s" % eggDir)
    pisitools.insinto("%s/" % eggDir, "PKG-INFO" )

    for i in ['docs/*.txt']:
        pisitools.dodoc(i)

    shelltools.chmod("docs/extensions/*", 0644)
    pisitools.insinto(extensions, "docs/extensions/*")
