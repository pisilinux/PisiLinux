#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "openal-soft-%s" % get.srcVERSION()

def setup():
    options = "-DALSA=1 \
               -DPULSEAUDIO=1 \
               -DOSS=1 \
               -DEXAMPLES=OFF"

    if get.buildTYPE() == "emul32":
        options += " -DCMAKE_INSTALL_PREFIX=/emul32 \
                     -DLIB_SUFFIX=32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    cmaketools.configure(options)

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # is there any "libdir" prefix for cmake ?
    if get.buildTYPE() == "emul32":
        from distutils.dir_util import copy_tree
        copy_tree("%s/emul32/lib32/" % get.installDIR(), "%s/usr/lib32" % get.installDIR())
        pisitools.removeDir("/emul32")
        pisitools.dosed("%s/usr/lib32/pkgconfig/openal.pc" % get.installDIR(), "emul32", "usr")
        return

    pisitools.dodoc("COPYING", "alsoftrc.sample")
