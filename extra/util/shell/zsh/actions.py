#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure('--bindir=/bin \
                         --with-tcsetpgrp \
                         --enable-maildir-support \
                         --enable-etcdir=/etc/zsh \
                         --enable-zshenv=/etc/zsh/zshenv \
                         --enable-zlogin=/etc/zsh/zlogin \
                         --enable-zlogout=/etc/zsh/zlogout \
                         --enable-zprofile=/etc/zsh/zprofile \
                         --enable-zshrc=/etc/zsh/zshrc \
                         --enable-fndir=/usr/share/zsh/functions \
                         --enable-scriptdir=/usr/share/zsh/scripts \
                         --enable-site-fndir=/usr/share/zsh/site-functions \
                         --enable-function-subdirs \
                         --enable-pcre \
                         --enable-cap \
                         --enable-multibyte \
                         --enable-cflags="%s" \
                         --enable-ldflags="%s"' % (get.CFLAGS(),get.LDFLAGS()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove versioned copy
    pisitools.remove("/bin/%s" % (get.srcDIR()))

    pisitools.doman("Doc/*.1")
    pisitools.dodoc("ChangeLog", "FEATURES", "LICENCE", "META-FAQ", "NEWS", "README")
