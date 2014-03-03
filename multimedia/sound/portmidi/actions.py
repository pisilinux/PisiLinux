#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("JAVAC","/usr/lib/jvm/java-7-openjdk/bin/javac")
shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")

def setup():
    cmaketools.configure("-DCMAKE_SKIP_BUILD_RPATH=1 \
                          -DLIB_INSTALL_DIR=/usr/lib \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_CACHEFILE_DIR=%s/build \
                          -DINCLUDE_INSTALL_DIR=/usr/include \
                          -DVERSION=%s" % (get.curDIR(), get.srcVERSION()))

def build():
    autotools.make()
    shelltools.system("./build-pyportmidi")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/include", "pm_common/pmutil.h")
    shelltools.chmod("%s/usr/include/pmutil.h" % get.installDIR(), mode=0644)

    # Fix missing symlink for libporttime.so (FS#21528).
    pisitools.dosym("/usr/lib/libportmidi_s.a", "/usr/lib/libportmidi.a")
    pisitools.dosym("/usr/lib/libportmidi.so", "/usr/lib/libporttime.so")
    pisitools.dosym("/usr/lib/libportmidi.a", "/usr/lib/libporttime.a")

    # Install test applications
    for app in ["latency", "midithread", "midithru", "mm", "qtest", "sysex", "test"]:
        pisitools.insinto("/usr/bin", "build/Release/%s" % app, "portmidi-%s" % app)

    # Build and Install python module
    pisitools.dodir("/usr/lib/%s/site-packages/pyportmidi" % get.curPYTHON())
    pisitools.dolib("pm_python/pyportmidi/_pyportmidi.so", "/usr/lib/%s/site-packages/pyportmidi" % get.curPYTHON())
    pisitools.insinto("/usr/lib/%s/site-packages/pyportmidi" % get.curPYTHON(), "pm_python/pyportmidi/*.py")

    pisitools.dodoc("CHANGELOG.txt", "license.txt", "README.txt")