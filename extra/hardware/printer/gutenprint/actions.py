#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("%s/m4local" % get.curDIR())
    shelltools.export("AT_M4DIR", "m4extra")
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-fi")

    autotools.configure("--with-cups \
                         --with-foomatic \
                         --with-ghostscript \
                         --with-readline \
                         --enable-test \
                         --enable-escputil \
                         --enable-cups-1_2-enhancements \
                         --enable-simplified-cups-ppds \
                         --enable-static-genppd \
                         --without-gimp2 \
                         --disable-cups-ppds \
                         --disable-rpath \
                         --disable-static \
                         --disable-testpattern \
                         --disable-translated-cups-ppds \
                         --disable-libgutenprintui2 \
                         --disable-dependency-tracking \
                         --disable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    pisitools.dohtml("%s/usr/share/gutenprint/doc/reference-html/*" % get.installDIR())

    pisitools.removeDir("/usr/share/gutenprint/doc/")
    #pisitools.removeDir("/usr/include/gutenprintui2")

    # FIXME: Remove command.types, check if any other file exists
    pisitools.removeDir("/etc/")

    pisitools.remove("/usr/share/foomatic/kitload.log")
