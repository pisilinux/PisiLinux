#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.rawConfigure()

def build():
    autotools.make()

def install():
    pisitools.dobin("mpgtx")
    pisitools.doman("man/mpgtx.1")

    for i in ["mpgjoin", "mpgsplit", "mpgcat", "mpginfo", "mpgdemux", "tagmp3"]:
        pisitools.dosym("mpgtx", "/usr/bin/%s" % i)
        pisitools.dosym("mpgtx.1", "/usr/share/man/man1/%s.1" % i)

    pisitools.dodoc("COPYING", "README", "TODO", "AUTHORS", "ChangeLog")
