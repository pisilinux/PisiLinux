#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "winff"

shelltools.export("HOME", get.workDIR())

def setup():
    pass

def build():
    shelltools.system("/usr/lib/lazarus/lazbuild --widgetset=qt -B winff.lpr")
#   shelltools.system("strip --strip-all winff")
   
def install():
    pisitools.dobin("winff")
    
    pisitools.insinto("/usr/share/winff", "presets.xml")   
   
    for lang in ["de", "es", "fr", "it", "nl", "pl", "tr"]:
        pisitools.domo("languages/winff.%s.po" % lang, lang, "winff.mo")
    
    for icon in ("16x16", "24x24", "32x32", "48x48"):
        pisitools.insinto("/usr/share/icons/hicolor/%s/apps/" % icon, "winff-icons/%s/winff.png" % icon)
    
    pisitools.insinto("/usr/share/pixmaps", "winff-icons/48x48/winff.png")
    
    pisitools.dodoc("*.txt", "docs/*.pdf", "docs/*.odt", "docs/*.txt", "winff-icons/*.txt")
