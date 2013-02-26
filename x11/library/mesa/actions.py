# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

if get.buildTYPE() == "emul32":
    Libdir = "/usr/lib32"
else:
    Libdir = "/usr/lib"

def setup():
    shelltools.export("CFLAGS", "%s -DNDEBUG" % get.CFLAGS())

    autotools.autoreconf("-vif")

    # gallium-lvm is enabled by default by commit a86fc719d6402eb482657707741890e69e81700f
    options ="--enable-pic \
              --with-dri-driverdir=/usr/lib/xorg/modules/dri \
              --with-gallium-drivers=r300,r600,nouveau,svga,swrast \
              --with-dri-drivers=i915,i965,r200,radeon,nouveau,swrast \
              --enable-gallium-llvm \
              --enable-egl \
              --enable-gallium-egl \
              --with-egl-platforms=x11,drm \
              --enable-shared-glapi \
              --enable-gbm \
              --enable-glx-tls \
              --enable-dri \
              --enable-glx \
              --enable-osmesa \
              --enable-gles1 \
              --enable-gles2 \
              --enable-texture-float \
              --enable-xa \
              --enable-vdpau "

    if get.buildTYPE() == "emul32":
        # compile with llvm doesn't work for now, test it later
        options += " --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
                     --disable-gallium-llvm \
                     --with-gallium-drivers=r600,nouveau,swrast \
                     --enable-32-bit"

    autotools.configure(options)

    #pisitools.dosed("configs/autoconf", "(PYTHON_FLAGS) = .*", r"\1 = -t")

def build():
#    autotools.make("-C src/glsl glsl_lexer.cpp")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("%s/libGL.so.1.2.0" % Libdir, "%s/mesa" % Libdir)

    if get.buildTYPE() == "emul32":
        return

    pisitools.dodoc("docs/COPYING")
    pisitools.dohtml("docs/*")
