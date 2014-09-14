#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    pisitools.dobin("nikto.pl")
    pisitools.rename("/usr/bin/nikto.pl", "nikto")
    pisitools.insinto("/etc/", "nikto.conf")
    pisitools.insinto("/usr/share/nikto/", "plugins")
    pisitools.insinto("/usr/share/nikto/", "templates")
    pisitools.dohtml("docs/nikto_manual.html")
    pisitools.doman("docs/nikto.1")
    pisitools.dodoc("docs/*.txt", "docs/nikto.dtd")
    shelltools.chmod("%s/usr/share/nikto/plugins/*" % get.installDIR(), 0644)
