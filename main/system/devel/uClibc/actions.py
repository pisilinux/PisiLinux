#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# Reset CFLAGS
CFLAGS = "%s -D__USE_GNU -fgnu89-inline -fno-stack-protector" % get.CFLAGS()

UCLIBC_ROOT="/usr/lib/uClibc"

# Make parameters
MAKE_PARAMS = """\
TARGET_CPU="%(target_cpu)s"
TARGET_ARCH="%(target_arch)s"
GCC_BIN="%(cc)s"
HOSTCC="%(cc)s"
CC="%(cc)s"
HOSTCFLAGS="%(cflags)s %(ldflags)s"
OPTIMIZATION="%(cflags)s -Os"
""" % {
        "target_arch"   : get.ARCH().replace("i686", "i386"),
        "target_cpu"    : get.ARCH(),
        "cc"            : get.CC(),
        "cflags"        : CFLAGS,
        "ldflags"       : get.LDFLAGS(),
        }

def remove_pisilinux_section(_dir):
    import os
    for k in shelltools.ls(_dir):
        # FIXME: should we do this only on nonshared or all ?
        # if ("crt" in k and k.endswith(".o")) or k.endswith("nonshared.a"):
        if ("crt" in k and k.endswith(".o")) or k.endswith(".a"):
            i = os.path.join(_dir, k)
            shelltools.system('objcopy -R ".comment.PISILINUX.OPTs" -R ".note.gnu.build-id" %s' % i)

def create_symlinks():
    systools = ("addr2line", "ar", "as", "cpp", "nm",
                "objcopy", "objdump", "ranlib",
                "size", "strings", "strip")

    gcclinks = ("c++", "cc", "g++")

    # Create arch prefixed symlinks in /usr/bin for systools
    for tool in systools:
        pisitools.dosym(tool, "/usr/bin/%s-uclibc-%s" % (get.ARCH(), tool))

    for link in gcclinks:
        pisitools.remove("%s/usr/bin/%s" % (UCLIBC_ROOT, link))
        pisitools.dosym("%s-uclibc-gcc" % get.ARCH(), "/usr/bin/%s-uclibc-%s" % (get.ARCH(), link))
        pisitools.dosym("/usr/bin/%s-uclibc-%s" % (get.ARCH(), link), "%s/usr/bin/%s" % (UCLIBC_ROOT, link))

    for native in ("gcc", "ld"):
        # Move around gcc and ld (native uClibc binaries)
        pisitools.domove("%s/bin/%s-uclibc-%s" % (UCLIBC_ROOT, get.ARCH(), native), "/usr/bin")
        pisitools.remove("%s/usr/bin/%s" % (UCLIBC_ROOT, native))
        pisitools.dosym("/usr/bin/%s-uclibc-%s" % (get.ARCH(), native), "%s/usr/bin/%s" % (UCLIBC_ROOT, native))

    # Remove bin/ under UCLIBC_ROOT
    pisitools.removeDir("%s/bin" % UCLIBC_ROOT)

def setup():
    # Skip ether tests
    shelltools.unlink("test/inet/tst-ethers-line.c")
    shelltools.unlink("test/inet/tst-ethers.c")

    pisitools.dodir("kernel-include")
    for d in ("asm", "asm-generic", "linux"):
        shelltools.copytree("/usr/include/%s" % d, "kernel-include/%s" % d)
        shelltools.sym("../kernel-include/%s" % d, "test/%s" % d)

    pisitools.dosed(".config", "^(TARGET_ARCH=).*$", '\\1"%s"' % get.ARCH())
    pisitools.dosed(".config", "^(UCLIBC_EXTRA_CFLAGS=).*$", '\\1"%s"' % CFLAGS)
    pisitools.dosed(".config", "^(RUNTIME_PREFIX=).*$", '\\1"%s"' % UCLIBC_ROOT)
    pisitools.dosed(".config", "^(DEVEL_PREFIX=).*$", '\\1"%s/usr"' % UCLIBC_ROOT)

def build():
    shelltools.system('yes "" | make oldconfig')

    autotools.make("%s" % MAKE_PARAMS)

def install():
    autotools.rawInstall('PREFIX="%s" %s' % (get.installDIR(), MAKE_PARAMS))
    autotools.rawInstall('-C utils PREFIX="%s" %s' % (get.installDIR(), MAKE_PARAMS), "utils_install")

    # Create symbolic links to /usr/include for some of the headers
    for d in ("asm", "asm-generic", "linux"):
        pisitools.dosym("/usr/include/%s" % d, "%s/usr/include/%s" % (UCLIBC_ROOT, d))

    # For ld.so.conf files
    pisitools.dodir("%s/etc" % UCLIBC_ROOT)

    # Create the necessary symlinks into /usr/bin
    #create_symlinks()

    remove_pisilinux_section("%s/usr/lib/uClibc/usr/lib" % get.installDIR())

    pisitools.dodoc("Changelog", "COPYING*", "TODO", "README")
