# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # For 32bit machines:
    #   * It get compiled with the normal options below. The emul32 are ignored
    #     on 32bit machines. Nothing is added to options variable.
    #
    # For 64bit machines:
    #   * First we compile for 64bit with the option --enable-win64. These build
    #     files are stored in the normal "work" dir
    #   * In the second run (for emul32 buildType), the 32bit part is compiled
    #     with the spesific libdir and the --with-wine64 options that is pointing
    #     to the 64bit files that was compiled in the first step (files in the work)
    #
    # More info can be obtained here: http://wiki.winehq.org/Wine64

    ## NOTE: This is 32bit only, but the actions.py still contains 64bit parts
    ##       It's not necessary. I just don't want to break the maintainability of
    ##       two seperate wine builds.

    autotools.autoreconf("-vif")
    options = "--without-capi \
               --with-curses \
               --without-esd \
               --with-opengl \
               --with-pulse \
               --with-x"

    if get.buildTYPE() == "emul32":
        options += "--libdir=/usr/lib32 \
                    --with-wine64=%s/work/%s" % (get.pkgDIR(), get.srcDIR())
    elif get.ARCH() == "x86_64":
        options += " --enable-win64"

    autotools.configure(options)

def build():
    autotools.make()

def install():
    # We need especially specify libdir and dlldir prefixes. Otherwise the
    # 32bit parts overwrite the 64bit files under /usr/lib

    if get.buildTYPE() == "emul32":
        autotools.install("UPDATE_DESKTOP_DATABASE=/bin/true libdir=%s/usr/lib32 dlldir=%s/usr/lib32/wine" % (get.installDIR(), get.installDIR()))
    else:
        autotools.install("UPDATE_DESKTOP_DATABASE=/bin/true libdir=%s/usr/lib dlldir=%s/usr/lib/wine" % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("ANNOUNCE", "AUTHORS", "COPYING.LIB", "LICENSE*", "README", "documentation/README.*")
