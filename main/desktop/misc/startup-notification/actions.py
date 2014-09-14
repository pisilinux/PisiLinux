#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system('sed -i -e "/AC_PATH_XTRA/d" configure.in')
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static")

    # Put flags in front of the libs. Needed for --as-needed.
    replace = (r"(\\\$deplibs) (\\\$compiler_flags)", r"\2 \1")
    pisitools.dosed("libtool", *replace)

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "doc/startup-notification.txt")
