#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("sed -i -e '/AC_PATH_XTRA/d' -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADER/' configure.ac")
    libtools.libtoolize("--force --install")
    autotools.autoreconf("-fi")

    autotools.configure("--with-x \
                         --disable-gl \
                         --disable-static")

def build():
    autotools.make()

    # libungif compatibility - instructions taken from Redhat specfile
    MAJOR=get.srcVERSION().split(".")[0]
    shelltools.system('%s -shared -Wl,-soname,libungif.so.%s -Llib/.libs -lgif -o libungif.so.%s' % (get.CC(), MAJOR, get.srcVERSION()))

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/")
    pisitools.dodoc("AUTHORS","BUGS","ChangeLog","NEWS","doc/*.txt")
