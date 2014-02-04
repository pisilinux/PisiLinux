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
    autotools.autoreconf("-if")
    
    autotools.configure("--disable-gui \
                         --includedir=/usr/include/iodbc \
                         --with-iodbc-inidir=/etc/iodbc \
                         --with-layout=gentoo \
                         --disable-libodbc \
                         --disable-static")

def build():
    autotools.make()
    

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.system("chrpath --delete %s/usr/bin/iodbctest" % get.installDIR())
    shelltools.system("chrpath --delete %s/usr/bin/iodbctestw" % get.installDIR())
    
    pisitools.remove("/usr/lib/*la")
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")

    pisitools.domove("/usr/share/libiodbc/samples", "/usr/share/doc/libiodbc")
    pisitools.removeDir("/usr/share/libiodbc")
