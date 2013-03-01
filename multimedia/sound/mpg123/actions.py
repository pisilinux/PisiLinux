# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

#This package using ltdl. .la files should be deleted only for plugins
KeepSpecial = ["libtool"]

def setup():
    cpu = "x86-64" if get.ARCH() == "x86_64" else "sse"

    pisitools.dosed("configure", "-faltivec")
    options = '--with-audio="alsa oss" \
               --with-cpu=%s \
               --with-optimization=2 \
               --enable-network=yes \
               --disable-ltdl-install' % cpu

    if get.buildTYPE() == "emul32":
        options += " --with-cpu=i586"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32": return

    pisitools.dodoc("ChangeLog", "COPYING", "NEWS", "README", "AUTHORS")

    pisitools.remove("/usr/lib/libmpg123.la")
