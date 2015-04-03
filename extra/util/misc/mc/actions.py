#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-screen=slang \
                         --with-gpm-mouse \
                         --with-vfs \
                         --with-ext2undel \
                         --with-edit \
                         --with-x=yes \
                         --enable-charset \
                         --enable-nls \
                         --with-samba \
                         --with-configdir=/etc/samba \
                         --with-codepagedir=/var/lib/samba/codepages \
                         --with-privatedir=/etc/samba/private")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("ABOUT*", "AUTHORS", "ChangeLog", "NEWS", "README*")
