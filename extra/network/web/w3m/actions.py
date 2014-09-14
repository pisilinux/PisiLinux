#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-unicode \
                         --disable-nls \
                         --with-termlib=ncurses \
                         --host=x86_64-pc-linux-gnu \
                         --enable-image=x11 \
                         --enable-keymap=w3m \
                         --disable-dict \
                         --without-mailer \
                         --with-imagelib=imlib2 \
                         --with-editor=/usr/bin/nano \
                         --with-browser=/usr/bin/firefox")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("ABOUT-NLS", "ChangeLog", "README")
 
