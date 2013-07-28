# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "mozjs%s/js/src" % get.srcVERSION()

def setup():
   autotools.configure("--enable-jemalloc \
                        --enable-readline \
                        --enable-threadsafe \
                        --with-system-nspr \
                        --enable-system-ffi ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README*")