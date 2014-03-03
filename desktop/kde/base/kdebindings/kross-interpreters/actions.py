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
jvmdir="/usr/lib/jvm/java-7-openjdk"

def setup():
    path = "%s/kross-interpreters-%s/java/KrossJNIConfig.cmake" % (get.workDIR(),get.srcVERSION())
    if get.ARCH() == "x86_64":
        shelltools.echo(path,"set(JAVA_JVM_LIBRARY %s/jre/lib/amd64/server/libjvm.so,)" % jvmdir)
        shelltools.echo(path,"set(JAVA_INCLUDE_PATH %s/include)" % jvmdir)
        shelltools.echo(path,"set(JAVA_INCLUDE_PATH2 %s/include/linux)" % jvmdir)
        shelltools.echo(path,"set(JAVA_AWT_LIBRARY %s/jre/lib/amd64)" % jvmdir)
        shelltools.echo(path,"set(JAVA_AWT_INCLUDE_PATH %s/include)" % jvmdir)
    elif get.ARCH() == "i686":
        shelltools.echo(path,"set(JAVA_JVM_LIBRARY %s/jre/lib/i386/server/libjvm.so)" % jvmdir)
        shelltools.echo(path,"set(JAVA_INCLUDE_PATH %s/include)" % jvmdir)
        shelltools.echo(path,"set(JAVA_INCLUDE_PATH2 %s/include/linux)" % jvmdir)
        shelltools.echo(path,"set(JAVA_AWT_LIBRARY %s/jre/lib/i386)" % jvmdir)
        shelltools.echo(path,"set(JAVA_AWT_INCLUDE_PATH %s/include)" % jvmdir)

    kde4.configure("-DBUILD_csharp=OFF \
                    -DENABLE_KROSSFALCON=OFF \
                    -DENABLE_PHP-QT=ON \
                    -DRUBY_SITE_LIB_DIR=/usr/lib/ruby/site_ruby/2.0.0 \
                    -DRUBY_SITE_ARCH_DIR=/usr/lib/ruby/site_ruby/2.0.0/x86_64-linux")

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dodoc("COPYING")
