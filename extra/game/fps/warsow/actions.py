#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

source = "source"
arch = "x86_64" if get.ARCH() == "x86_64" else "i386"

# this package is fragile to flags, you have been warned
#cflags = get.CFLAGS().replace("-fomit-frame-pointer", "")
#cxxflags = get.CXXFLAGS().replace("-fomit-frame-pointer", "")


def build():
    #shelltools.export("AR", "ar")
    #shelltools.export("RANLIB", "ranlib")
    #shelltools.export("CFLAGS", cflags)
    #shelltools.export("CXXFLAGS", cxxflags)

    shelltools.cd(source)
    #autotools.make("-C ../libsrcs/angelscript/angelSVN/sdk/angelscript/projects/gnuc")
    autotools.make("-j1")

def install():
    for i in ["doc", "rtf", "txt"]:
        pisitools.dodoc("docs/*.%s" % i)
    shelltools.cd(source)

    pisitools.insinto("/usr/share/warsow", "release/warsow.%s" % arch, "warsow")
    pisitools.insinto("/usr/share/warsow", "release/wsw_server.%s" % arch, "warsow-server")
    pisitools.insinto("/usr/share/warsow", "release/wswtv_server.%s" % arch, "warsowtv-server")

    pisitools.dodir("/usr/share/warsow")
    pisitools.insinto("/usr/share/warsow/", "release/basewsw")
    pisitools.insinto("/usr/share/warsow/", "release/libs")