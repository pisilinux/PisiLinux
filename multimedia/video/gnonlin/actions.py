#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --enable-gtk-doc \
                         --disable-valgrind \
                         --with-package-name='Pardus %s package' \
                         --with-package-origin='http://www.pardus-anka.org/' \
                         " % get.srcNAME())


def build():
    autotools.make()


def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "RELEASE")
