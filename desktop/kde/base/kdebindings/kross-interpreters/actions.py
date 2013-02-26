#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    path = "%s/kross-interpreters-%s/java/KrossJNIConfig.cmake" % (get.workDIR(),get.srcVERSION())
    if get.ARCH() == "x86_64":
        shelltools.echo(path,"set(JAVA_JVM_LIBRARY /opt/sun-jdk/jre/lib/amd64/server/libjvm.so)")
        shelltools.echo(path,"set(JAVA_INCLUDE_PATH /opt/sun-jdk/include)")
        shelltools.echo(path,"set(JAVA_INCLUDE_PATH2 /opt/sun-jdk/include/linux)")
        shelltools.echo(path,"set(JAVA_AWT_LIBRARY /opt/sun-jdk/jre/lib/amd64)")
        shelltools.echo(path,"set(JAVA_AWT_INCLUDE_PATH /opt/sun-jdk/include)")
    elif get.ARCH() == "i686":
        shelltools.echo(path,"set(JAVA_JVM_LIBRARY /opt/sun-jdk/jre/lib/i386/server/libjvm.so)")
        shelltools.echo(path,"set(JAVA_INCLUDE_PATH /opt/sun-jdk/include)")
        shelltools.echo(path,"set(JAVA_INCLUDE_PATH2 /opt/sun-jdk/include/linux)")
        shelltools.echo(path,"set(JAVA_AWT_LIBRARY /opt/sun-jdk/jre/lib/i386)")
        shelltools.echo(path,"set(JAVA_AWT_INCLUDE_PATH /opt/sun-jdk/include)")

    kde4.configure("-DBUILD_csharp=OFF \
                    -DENABLE_KROSSFALCON=OFF \
                    -DENABLE_PHP-QT=ON \
                    -DRUBY_SITE_LIB_DIR=/usr/lib/ruby/site_ruby/1.8 \
                    -DRUBY_SITE_ARCH_DIR=/usr/lib/ruby/site_ruby/1.8/i686-linux")

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dodoc("COPYING")
