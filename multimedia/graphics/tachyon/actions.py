#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "tachyon"
buildtype = "linux-thr-ogl"
additionalflags = "-fPIC" if get.ARCH() == "x86_64" else ""

def setup():
    pisitools.dosed("unix/Make-arch", "pardusCC", get.CC())
    shelltools.unlinkDir("scenes/CVS")

def build():
    shelltools.export("CFLAGS", "%s %s" % (get.CFLAGS(), additionalflags))
    shelltools.cd("unix")
    autotools.make('USEJPEG=-DUSEJPEG JPEGLIB=-ljpeg\
                    USEPNG=-DUSEPNG PNGLIB="-lpng -lz" \
                    %s' % buildtype)

def install():
    pisitools.dobin("compile/%s/tachyon" % buildtype)
    pisitools.dolib_so("compile/%s/libtachyon.so.0.0" % buildtype)

    pisitools.dosym("libtachyon.so.0.0", "/usr/lib/libtachyon.so.0")
    pisitools.dosym("libtachyon.so.0.0", "/usr/lib/libtachyon.so")

    pisitools.insinto("/usr/share/tachyon/", "scenes")

    pisitools.dohtml("docs/tachyon/*")
    pisitools.dodoc("Changes", "Copyright", "README")
