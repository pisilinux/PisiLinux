#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # /var/run => /run
    #pisitools.dosed("configure.ac", "^(\s+CONSOLE_KIT_PID_FILE=)\$\{localstatedir\}(\/run\/ConsoleKit\/pid)", r"\1\2")
    #pisitools.dosed("src/Makefile.am", "\$\(localstatedir\)(\/run\/ConsoleKit)", r"\1")
    #shelltools.system("sed -i -e '/SystemdService/d' data/org.freedesktop.ConsoleKit.service.in")

    #autotools.autoreconf("-fi")

    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --sbindir=/usr/sbin \
                         --with-rundir=/run \
                         --libexecdir=/usr/libexec/ConsoleKit \
                         --localstatedir=/var \
                         --enable-polkit \
                         --enable-pam-module \
                         --enable-udev-acl \
                         --disable-docbook-docs \
                         --disable-static \
                         --with-dbus-services=/usr/share/dbus-1/services \
                         --with-logrotate-dir=/etc/logrotate.d \
                         --with-xinitrc-dir=/etc/X11/xinit/xinitrc.d \
                         --with-pam-module-dir=/lib/security \
                         --with-systemdsystemunitdir=no \
                         XMLTO_FLAGS='--skip-validation' \
                         ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s/" % get.installDIR())
    
    pisitools.removeDir("/run")

    pisitools.dodoc("AUTHORS", "README", "COPYING", "HACKING", "NEWS", "TODO")
