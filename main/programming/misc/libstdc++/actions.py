#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "gcc-3.3.6"

# Global Path Variables
BINPATH = "/usr/%s/gcc-bin/3.3.6" % get.HOST()
LIBPATH = "/usr/lib/gcc-lib/%s/3.3.6" % get.HOST()
DATAPATH = "/usr/share/gcc-data/%s/3.3.6" % get.HOST()
STDCXX_INCDIR = "/usr/lib/gcc-lib/%s/3.3.6/include/g++-v3" % get.HOST()

# FIXME: do this smarter
mcpu = "generic" if get.ARCH() == "x86_64" else "atom"
cflags = get.CFLAGS().replace("mtune", "mcpu").replace("-fstack-protector", "").replace("-D_FORTIFY_SOURCE=2", "").replace("-mcpu=%s" % mcpu, "-mcpu=%s" % get.ARCH().replace("_", "-"))
cxxflags =  get.CXXFLAGS().replace("mtune", "mcpu").replace("-fstack-protector", "").replace("-D_FORTIFY_SOURCE=2", "").replace("-mcpu=%s" % mcpu, "-mcpu=%s" % get.ARCH().replace("_", "-"))

def setup():
    shelltools.export("CFLAGS", cflags)
    shelltools.export("CXXFLAGS", cxxflags)

    # Misdesign in libstdc++ (Redhat)
    shelltools.copy("libstdc++-v3/config/cpu/i486/atomicity.h", "libstdc++-v3/config/cpu/i386/atomicity.h")

    shelltools.system("./contrib/gcc_update --touch &> /dev/null")

    conf = "--enable-nls \
            --without-included-gettext \
            --disable-multilib \
            --prefix=/usr \
            --bindir=%s \
            --includedir=%s/include \
            --datadir=%s \
            --mandir=%s/man \
            --infodir=%s/info \
            --enable-shared \
            --host=%s \
            --target=%s \
            --with-system-zlib \
            --enable-languages=c++ \
            --enable-threads=posix \
            --enable-long-long \
            --disable-checking \
            --enable-cstdio=stdio \
            --enable-__cxa_atexit \
            --enable-version-specific-runtime-libs \
            --with-gxx-include-dir=%s \
            --with-local-prefix=/usr/local" %(BINPATH, LIBPATH, DATAPATH, DATAPATH, DATAPATH, get.HOST(), get.HOST(), STDCXX_INCDIR)

    # Build in a separate build tree
    shelltools.makedirs("%s/build" % get.workDIR())
    shelltools.cd("%s/build" % get.workDIR())
    shelltools.system("%s/%s/configure %s" % (get.workDIR(), WorkDir, conf))

    shelltools.touch("gcc/c-gperf.h")

def build():
    shelltools.cd("%s/build" % get.workDIR())
    autotools.make("all-target-libstdc++-v3 \
                    LIBPATH=\"%s\" \
                    BOOT_CFLAGS=\"%s\" STAGE1_CFLAGS=\"-O\"" % (LIBPATH, get.CFLAGS()))

def install():
    shelltools.cd("%s/build" % get.workDIR())


    # Do the 'make install' from the build directory
    autotools.rawInstall("prefix=/usr \
                        bindir=%s \
                        includedir=%s/include \
                        datadir=%s \
                        mandir=%s/man \
                        infodir=%s/info \
                        DESTDIR=\"%s\" \
                        LIBPATH=\"%s\"" % (BINPATH, LIBPATH, DATAPATH, DATAPATH, DATAPATH, get.installDIR(), LIBPATH),
                        "install-target-libstdc++-v3")

    # we'll move this into a directory we can put at the end of ld.so.conf
    # other than the normal versioned directory, so that it doesnt conflict
    # with gcc 3.3.3
    pisitools.domove("/%s/lib*" % LIBPATH, "/usr/lib/libstdc++-v3/")

    # we dont want the headers...
    pisitools.removeDir("/usr/lib/gcc*")
    # or locales...
    if shelltools.isDirectory("%s/usr/share" % get.installDIR()):
        pisitools.removeDir("/usr/share")
    # or anything other than the .so files, really.
    pisitools.remove("/usr/lib/libstdc++-v3/*.la")
    pisitools.remove("/usr/lib/libstdc++-v3/*.a")

    # we dont even want the un-versioned .so symlink, as it confuses some
    # apps and also causes others to link against the old libstdc++...
    pisitools.remove("/usr/lib/libstdc++-v3/libstdc++.so")
