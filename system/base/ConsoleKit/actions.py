#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    # /var/run => /run
    pisitools.dosed("configure.ac", "^(\s+CONSOLE_KIT_PID_FILE=)\$\{localstatedir\}(\/run\/ConsoleKit\/pid)", r"\1\2")
    pisitools.dosed("src/Makefile.am", "\$\(localstatedir\)(\/run\/ConsoleKit)", r"\1")

    autotools.autoreconf("-fi")

    autotools.configure("\
                         --with-pid-file=/run/ConsoleKit/pid \
                         --with-systemdsystemunitdir=no \
                         --disable-static \
                         --enable-pam-module \
                         --enable-udev-acl \
                        ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s/" % get.installDIR())
    pisitools.dodir("/run/console")

    pisitools.dodoc("AUTHORS","ChangeLog","README", "COPYING", "HACKING", "NEWS", "TODO")
