#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

def setup():
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-fi")
    autotools.configure("--with-rpmbuild=/bin/false \
                         --with-drivers=all \
                         --enable-nls \
                         --without-aalib \
                         --disable-rpath \
                         --disable-lockdev \
                         --disable-resmgr \
                         --disable-ttylock \
                         --disable-baudboy \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s \
                          udevscriptdir=/lib/udev" % get.installDIR())

    HAL_FDI="usr/share/hal/fdi/information/20thirdparty/10-camera-libgphoto2.fdi"
    UDEV_RULES="lib/udev/rules.d/40-libgphoto2.rules"
    CAM_LIST="usr/lib/libgphoto2/print-camera-list"
    CAM_LIBS="usr/lib/libgphoto2/%s" % get.srcVERSION()

    # Create hal directory
    pisitools.dodir(shelltools.dirName(HAL_FDI))

    # Export the necessary env variables
    shelltools.export("CAMLIBS", "%s/%s" % (get.installDIR(), CAM_LIBS))
    shelltools.export("LIBDIR", "%s/usr/lib/" % get.installDIR())
    shelltools.export("LD_LIBRARY_PATH", "%s/usr/lib/" % get.installDIR())

    # Generate HAL FDI file
    f = open(os.path.join(get.installDIR(), HAL_FDI), "w")
    f.write(os.popen("%s/%s hal-fdi" % (get.installDIR(), CAM_LIST)).read())
    f.close()

    # Generate UDEV rule which will replace the HAL FDI when HAL is deprecated
    pisitools.dodir("/lib/udev/rules.d")
    f = open(os.path.join(get.installDIR(), UDEV_RULES), "w")
    f.write(os.popen("%s/%s udev-rules version 136" % (get.installDIR(), CAM_LIST)).read())
    f.close()

    pisitools.removeDir("/usr/share/doc/libgphoto2_port")

    # Remove circular symlink
    pisitools.remove("/usr/include/gphoto2/gphoto2")

    pisitools.dodoc("ChangeLog", "NEWS*", "README", "AUTHORS", "TESTERS", "MAINTAINERS", "HACKING")

