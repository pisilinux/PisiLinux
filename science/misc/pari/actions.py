#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./Configure \
                       --prefix=/usr \
                       --datadir=/usr/share/pari \
                       --libdir=/usr/lib \
                       --mandir=/usr/share/man/man1 \
                       --with-readline=/usr \
                       --with-gmp=/usr")

def build():
    autotools.make()

def check():
    autotools.make("dobench")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove precompiled lisp files
    #pisitools.remove("/usr/share/emacs/site-lisp/pari/*.elc")

    for d in ["doc","examples"]:
        pisitools.removeDir("/usr/share/pari/%s" % d)

    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "examples")
    pisitools.dodoc("AUTHORS", "CHANGES", "COPYING", "NEW", "README")
