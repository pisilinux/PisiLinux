#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")

def setup():
    kde4.configure("-DBUILD_csharp=OFF \
                    -DCMAKE_BUILD_TYPE=Release \
                    -DENABLE_KROSSFALCON=OFF \
                    -DENABLE_PHP-QT=ON \
                    -DKDE4_BUILD_TESTS=OFF \
                    -DBUILD_ruby=OFF \
                    -DPYTHON_EXECUTABLE=/usr/bin/python \
                    -DRUBY_SITE_LIB_DIR=/usr/lib/ruby/site_ruby/2.2.0 \
                    -DRUBY_SITE_ARCH_DIR=/usr/lib/ruby/site_ruby/2.2.0/x86_64-linux")

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dodoc("COPYING")
