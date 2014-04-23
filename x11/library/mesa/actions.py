# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

Libdir = "/usr/lib32" if get.buildTYPE() == "emul32" else "/usr/lib"

def setup():
    autotools.autoreconf("-vif")

    options ="\
              --with-dri-driverdir=/usr/lib/xorg/modules/dri \
              --with-gallium-drivers=r300,r600,nouveau,svga,swrast \
              --with-dri-drivers=i915,i965,r200,radeon,nouveau,swrast \
              --with-egl-platforms=x11,drm,wayland \
              --enable-gallium-llvm \
              --enable-egl \
              --enable-gallium-egl \
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
              --enable-vdpau \
              --enable-dri3 \
             "

    if get.buildTYPE() == "emul32":
        # compile with llvm doesn't work for now, test it later
        options += " --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
                     --disable-gallium-llvm \
                     --with-gallium-drivers=r600,nouveau,swrast \
                     --enable-32-bit"

    autotools.configure(options)
    pisitools.dosed("libtool","( -shared )", " -Wl,--as-needed\\1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("%s/libGL.so.1.2.0" % Libdir, "%s/mesa" % Libdir)
    pisitools.dosym("libGL.so.1.2.0", "%s/libGL.so.1.2" % Libdir)

    if get.buildTYPE() == "emul32":
        return

    pisitools.dodoc("docs/COPYING")
    pisitools.dohtml("docs/*")
