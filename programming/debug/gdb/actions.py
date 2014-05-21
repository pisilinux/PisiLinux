#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("config/override.m4", "2.64", "2.69")
    shelltools.system('sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" libiberty/configure')
    autotools.autoreconf("-vfi")
    autotools.configure("--with-system-readline \
                         --with-separate-debug-dir=/usr/lib/debug \
                         --with-gdb-datadir=/usr/share/gdb \
                         --with-pythondir=/usr/lib/%s/site-packages \
                         --disable-nls \
                         --disable-rpath \
                         --with-python \
                         --with-expat" % get.curPYTHON())


def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    
    for libdel in ["libbfd.a","libopcodes.a"]:
        pisitools.remove("/usr/lib/%s" % libdel)

    # these are not necessary
    for info in ["bfd","configure","standards"]:
        pisitools.remove("/usr/share/info/%s.info" % info)
        
    for hea in ["ansidecl","symcat","dis-asm", "bfd", "bfdlink"]:
        pisitools.remove("/usr/include/%s.h" % hea)
    
    pisitools.dodoc("README*", "MAINTAINERS", "COPYING*", "ChangeLog*")