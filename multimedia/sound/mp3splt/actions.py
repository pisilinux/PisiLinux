#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--prefix=/usr \
			 --with-mp3splt-includes=/usr/include/ \
			 --with-mp3splt-libraries=/usr/lib \
			 --disable-dependency-tracking \
			 --enable-oggsplt_symlink")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
