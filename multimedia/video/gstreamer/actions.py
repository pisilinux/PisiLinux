#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-vfi")
    #shelltools.system("./autogen.sh --disable-gtk-doc --disable-docbook")

    options = '--with-package-name="GStreamer package for Pardus" \
               --with-package-origin="http://www.pardus-anka.org" \
               --enable-nls \
               --disable-dependency-tracking \
               --disable-examples \
               --disable-tests \
               --disable-failing-tests \
               --disable-static \
               --disable-rpath \
               --disable-valgrind \
               --disable-gtk-doc'

    if get.buildTYPE() == "emul32":
        options += " --bindir=/usr/bin32 \
                     --libexecdir=/usr/libexec32 \
                     --libdir=/usr/lib32"

        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/bin32")
        pisitools.removeDir("/usr/libexec32")

    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
