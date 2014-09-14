#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    # fix sandbox violations when attempt to read "/missing.xml"
    pisitools.dosed("testapi.c", "\/missing.xml", "missing.xml")

    options = "--with-zlib \
               --with-readline \
               --enable-ipv6 \
               --disable-static \
               --with-threads \
               --with-history \
              "

    if get.buildTYPE() == "emul32":
        options += " --bindir=/emul32/bin \
                     --without-python"
    else: options += " --with-python"

    autotools.configure(options)
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/share/gtk-doc")
        return

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
