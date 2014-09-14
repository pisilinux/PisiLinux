#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "glibc-2.20"

arch = "x86-64" if get.ARCH() == "x86_64" and not get.buildTYPE() == "emul32" else "i686"
defaultflags = "-O3 -g -fasynchronous-unwind-tables -mtune=generic -march=%s" % arch
if get.buildTYPE() == "emul32": defaultflags += " -m32"
# this is getting ridiculous, also gdb3 breaks resulting binary
#sysflags = "-mtune=generic -march=x86-64" if get.ARCH() == "x86_64" else "-mtune=generic -march=i686"

### helper functions ###
def removePisiLinuxSection(_dir):
    for root, dirs, files in os.walk(_dir):
        for name in files:
            # FIXME: should we do this only on nonshared or all ?
            # if ("crt" in name and name.endswith(".o")) or name.endswith("nonshared.a"):
            if ("crt" in name and name.endswith(".o")) or name.endswith(".a"):
                i = os.path.join(root, name)
                shelltools.system('objcopy -R ".comment.PISILINUX.OPTs" -R ".note.gnu.build-id" %s' % i)

ldconf32bit = """/lib32
/usr/lib32
"""

def setup():
    shelltools.export("LANGUAGE","C")
    shelltools.export("LANG","C")
    shelltools.export("LC_ALL","C")

    shelltools.export("CC", "gcc %s " % defaultflags)
    shelltools.export("CXX", "g++ %s " % defaultflags)

    shelltools.export("CFLAGS", defaultflags)
    shelltools.export("CXXFLAGS", defaultflags)

    shelltools.makedirs("build")
    shelltools.cd("build")
    options = "--prefix=/usr \
               --libdir=/usr/lib \
               --mandir=/usr/share/man \
               --infodir=/usr/share/info \
               --libexecdir=/usr/lib/misc \
               --with-bugurl=https://bugs.pisilinux.org \
               --enable-add-ons \
               --enable-bind-now \
               --enable-kernel=2.6.32 \
               --enable-stackguard-randomization \
               --without-selinux \
               --without-gd \
               --disable-profile \
               --enable-obsolete-rpc \
               --enable-lock-elision \
               --enable-multi-arch \
               --with-tls"
    if get.buildTYPE() == "emul32":
        options += "\
                    --libdir=/usr/lib32 \
                    --enable-multi-arch i686-pc-linux-gnu \
                   "

    shelltools.system("../configure %s" % options)

def build():
    shelltools.cd("build")
    if get.buildTYPE() == "emul32":
        shelltools.echo("configparms","build-programs=no")
        shelltools.echo("configparms", "slibdir=/lib32")
        shelltools.echo("configparms", "rtlddir=/lib32")
        shelltools.echo("configparms", "bindir=/tmp32")
        shelltools.echo("configparms", "sbindir=/tmp32")
        shelltools.echo("configparms", "rootsbindir=/tmp32")
        shelltools.echo("configparms", "datarootdir=/tmp32/share")

        autotools.make()

        pisitools.dosed("configparms", "=no", "=yes")
        shelltools.echo("configparms", "CC += -fstack-protector-strong -D_FORTIFY_SOURCE=2")
        shelltools.echo("configparms", "CXX += -fstack-protector-strong -D_FORTIFY_SOURCE=2")

    else:
        shelltools.echo("configparms", "slibdir=/lib")
        shelltools.echo("configparms", "rtlddir=/lib")

    autotools.make()

def check():
     shelltools.cd("build")
     autotools.make("check || true")


def install():
    shelltools.cd("build")

    autotools.rawInstall("install_root=%s" % get.installDIR())

    pisitools.dodir("/etc/ld.so.conf.d")

    if get.buildTYPE() != "emul32":
        #Install locales once.
        autotools.rawInstall("install_root=%s localedata/install-locales" % get.installDIR())

        # Remove our options section from crt stuff
        removePisiLinuxSection("%s/usr/lib/" % get.installDIR())


    if get.buildTYPE() == "emul32":
        pisitools.dosym("/lib32/ld-linux.so.2", "/lib/ld-linux.so.2")

        shelltools.echo("%s/etc/ld.so.conf.d/60-glibc-32bit.conf" % get.installDIR(), ldconf32bit)

        # Remove our options section from crt stuff
        removePisiLinuxSection("%s/usr/lib32/" % get.installDIR())

        pisitools.removeDir("/tmp32")


    # We'll take care of the cache ourselves
    if shelltools.isFile("%s/etc/ld.so.cache" % get.installDIR()):
        pisitools.remove("/etc/ld.so.cache")

    # Prevent overwriting of the /etc/localtime symlink
    if shelltools.isFile("%s/etc/localtime" % get.installDIR()):
        pisitools.remove("/etc/localtime")

    # Nscd needs this to work
    pisitools.dodir("/var/run/nscd")
    pisitools.dodir("/var/db/nscd")

    # remove zoneinfo files since they are coming from timezone packages
    # we disable timezone build with a patch, keeping these lines for easier maintenance
    if shelltools.isDirectory("%s/usr/share/zoneinfo" % get.installDIR()):
        pisitools.removeDir("/usr/share/zoneinfo")

    #while bootstrapping whole system zic should not be removed. timezone package does not build without it. # 2013
    #for i in ["zdump","zic"]:
        #if shelltools.isFile("%s/usr/sbin/%s" % (get.installDIR(), i)):
            #pisitools.remove("/usr/sbin/%s" % i)

    shelltools.cd("..")
    pisitools.dodoc("BUGS", "ChangeLog*", "CONFORMANCE", "NAMESPACE", "NEWS", "PROJECTS", "README*", "LICENSES")

