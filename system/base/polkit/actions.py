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
    #Use it for root user instead of wheel group
    #shelltools.system("sed -i -e 's|unix-group:wheel|unix-user:0|' src/polkitbackend/*-default.rules")
    # Use it if we have spidermonkey 1.8.7 or newer...
    #shelltools.system("sed -i -e '/mozjs/s:185:187:g' configure")
    #look http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/sys-auth/polkit/polkit-0.107.ebuild
    #shelltools.system("cmd='sed -i -e "/mozjs/s:185:187:g" configure src/polkitbackend/polkitbackendjsauthority.c'")
    autotools.autoreconf("-fi")
    autotools.configure("--with-pam-module-dir=/lib/security/ \
                         --with-os-type=PisiLinux \
                         --enable-examples \
                         --enable-introspection \
                         --enable-libsystemd-login=no \
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
