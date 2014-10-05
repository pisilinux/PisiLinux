#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."


def setup():
    pass

def build():
    shelltools.system("/usr/lib/lazarus/lazbuild --lazarusdir=/usr/lib/lazarus --widgetset=qt -B winff.lpr")
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
