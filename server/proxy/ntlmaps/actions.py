#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    # Exe
    pisitools.doexe("main.py", "/usr/bin")
    pisitools.rename("/usr/bin/main.py", "ntlmaps")

    # Libs
    pisitools.insinto("/usr/lib/%s/site-packages" % get.curPYTHON(), "lib/*")

    # Conf
    pisitools.insinto("/etc/ntlmaps", "server.cfg")
    shelltools.chmod("%s/etc/ntlmaps/server.cfg" % get.installDIR(), 0640)

    # Docs
    pisitools.dohtml("doc/*.htm")
    pisitools.dodoc("COPYING", "doc/changelog.txt", "doc/ENCRYPTION.txt", "doc/README.txt", "doc/research.txt")
