#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-posix-regex \
                         --without-readlib \
                         --disable-etags \
                         --enable-tmpdir=/tmp")

def build():
    autotools.make()

def install():
    autotools.install()

    # Don't conflict with emacs
    pisitools.rename("/usr/bin/ctags", "exuberant-ctags")
    pisitools.rename("/usr/share/man/man1/ctags.1", "exuberant-ctags.1")

    pisitools.dohtml("EXTENDING.html", "ctags.html")
    pisitools.dodoc("COPYING", "FAQ", "NEWS", "README")
