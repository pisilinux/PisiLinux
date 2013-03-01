#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "soundtouch"

def setup():
    pisitools.dosed("source/SoundStretch/Makefile.*", "-O3", "")

    autotools.configure("--enable-shared \
                         --disable-dependency-tracking \
                         --disable-static \
                         --disable-integer-samples \
                         --with-pic")

    # Avoid rpath
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s pkgdocdir=/usr/share/doc/%s" % (get.installDIR(), get.srcNAME()))

    # Install compat symlinks for pkgconfig files
    pisitools.dosym("soundtouch-1.4.pc", "/usr/lib/pkgconfig/libSoundTouch.pc")
    pisitools.dosym("soundtouch-1.4.pc", "/usr/lib/pkgconfig/soundtouch-1.0.pc")

    # Install docs
    pisitools.dodoc("COPYING.TXT", "README.html")
