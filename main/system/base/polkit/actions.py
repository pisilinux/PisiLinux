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
    #autotools.autoreconf("-fi")
    autotools.configure("--with-pam-module-dir=/lib/security/ \
                         --with-os-type=pardus \
                         --with-mozjs=mozjs-17.0 \
                         --with-dbus \
                         --enable-examples \
                         --enable-introspection \
                         --enable-libsystemd-login=no \
                         --with-systemdsystemunitdir=no \
                         --disable-man-pages \
                         --disable-gtk-doc \
                         --disable-static")
    
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ") 

def build():
    shelltools.export('HOME', get.workDIR())
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s/" % get.installDIR())

    pisitools.dodir("/var/lib/polkit-1")
    shelltools.chmod("%s/var/lib/polkit-1" % get.installDIR(), mode=00700)
    shelltools.chmod("%s/etc/polkit-1/rules.d" % get.installDIR(), mode=00700)
    shelltools.chown("%s/etc/polkit-1/rules.d" % get.installDIR(),"polkitd","root") #yada? "polkitd","root"
    shelltools.chown("%s/var/lib/polkit-1" % get.installDIR(),"polkitd","polkitd")  
    shelltools.chown("%s/usr/share/polkit-1" % get.installDIR(),"polkitd","root") #yada? "polkitd","root"
    pisitools.dodoc("AUTHORS", "NEWS", "README", "HACKING", "COPYING")
