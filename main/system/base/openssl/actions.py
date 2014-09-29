#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    options = " --prefix=/usr \
                --libdir=lib \
                --openssldir=/etc/ssl \
                --enginesdir=/usr/lib/openssl/engines \
                shared -Wa,--noexecstack \
                zlib enable-camellia enable-seed enable-tlsext enable-rfc3779 \
                enable-cms enable-md2 threads"

    if get.buildTYPE() == "_emul32":
        options += " --prefix=/_emul32 --libdir=lib32"
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.system("./Configure linux-elf %s" % options)
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")

    else:
        options += " enable-ec_nistp_64_gcc_128"
        shelltools.system("./Configure linux-x86_64 %s" % options)
        pisitools.dosed("Makefile", "^(SHARED_LDFLAGS=).*", "\\1 ${LDFLAGS}")
        pisitools.dosed("Makefile", "^(CFLAG=.*)", "\\1 ${CFLAGS}")

def build():
    autotools.make("depend")
    autotools.make("-j1")
    autotools.make("rehash")

def check():
    #Revert ca-dir patch not to fail test
    shelltools.system("patch -p1 -R < openssl-1.0.0-beta4-ca-dir.patch")

    homeDir = "%s/test-home" % get.workDIR()
    shelltools.export("HOME", homeDir)
    shelltools.makedirs(homeDir)
    autotools.make("-j1 test")

    #Passed. So, re-patch
    shelltools.system("patch -p1 < openssl-1.0.0-beta4-ca-dir.patch")

def install():
    autotools.rawInstall("INSTALL_PREFIX=%s MANDIR=/usr/share/man" % get.installDIR())

    # Rename conflicting manpages
    pisitools.rename("/usr/share/man/man1/passwd.1", "ssl-passwd.1")
    pisitools.rename("/usr/share/man/man3/rand.3", "ssl-rand.3")
    pisitools.rename("/usr/share/man/man3/err.3", "ssl-err.3")

    if get.buildTYPE() == "_emul32":
        #from distutils.dir_util import copy_tree
        shelltools.copytree("%s/_emul32/lib32/" % get.installDIR(), "%s/usr/lib32" % get.installDIR())
        pisitools.removeDir("/_emul32")
        pisitools.remove("/usr/lib32/*.a")
        path = "%s/usr/lib32/pkgconfig" % get.installDIR()
        for f in shelltools.ls(path): pisitools.dosed("%s/%s" % (path, f), "^(prefix=\/)_emul32", r"\1usr")
        return

    # Move engines to /usr/lib/openssl/engines
    pisitools.dodir("/usr/lib/openssl")
    pisitools.domove("/usr/lib/engines", "/usr/lib/openssl")

    # Certificate stuff
    pisitools.dobin("tools/c_rehash")


    # Create needed dirs
    for cadir in ["misc", "private"]:
        pisitools.dodir("/etc/ssl/%s" % cadir)

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("CHANGES*", "FAQ", "LICENSE", "NEWS", "README", "doc/*.txt")
