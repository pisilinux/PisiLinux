#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

KeepSpecial=["perl"]

def setup():
    shelltools.export("LC_ALL", "C")
    shelltools.export("BUILD_BZIP2", "0")

    shelltools.system('sh Configure -des \
                      -Darchname=%s-linux \
                      -Dcccdlflags=-fPIC \
                      -Dccdlflags=-rdynamic \
                      -Dcc=%s \
                      -Dprefix=/usr \
                      -Dvendorprefix=/usr \
                      -Dsiteprefix=/usr \
                      -Ulocincpth=  \
                      -Doptimize="%s" \
                      -Duselargefiles \
                      -Dusethreads \
                      -Duseithreads \
                      -Dd_semctl_semun \
                      -Dscriptdir=/usr/bin \
                      -Dman1dir=/usr/share/man/man1 \
                      -Dman3dir=/usr/share/man/man3 \
                      -Dinstallman1dir=%s/usr/share/man/man1 \
                      -Dinstallman3dir=%s/usr/share/man/man3 \
                      -Dlibperl=libperl.so.%s \
                      -Duseshrplib \
                      -Dman1ext=1 \
                      -Dman3ext=3pm \
                      -Dcf_by="Pardus ANKA" \
                      -Ud_csh \
                      -Di_ndbm \
                      -Di_gdbm \
                      -Di_db \
                      -Ubincompat5005 \
                      -Uversiononly \
                      -Dpager="/usr/bin/less -isr" \
                      -Dd_gethostent_r_proto -Ud_endhostent_r_proto -Ud_sethostent_r_proto \
                      -Ud_endprotoent_r_proto -Ud_setprotoent_r_proto \
                      -Ud_endservent_r_proto -Ud_setservent_r_proto \
                      ' %(get.ARCH(), get.CC(), get.CFLAGS(), get.installDIR(), get.installDIR(), get.srcVERSION()))

def build():
    # colorgcc uses Term::ANSIColor
    paths = get.ENV("PATH").split(":")
    if "/usr/share/colorgcc" in paths:
        paths.remove("/usr/share/colorgcc")
    shelltools.export("PATH", ":".join(paths))
    ##
    autotools.make()

def check():
    #symlink libperl.so.x.y.z to libperl.so
    #so we can pass /lib/ExtUtils/t/Embed.t test
    shelltools.sym("libperl.so.%s" % get.srcVERSION(),"libperl.so")
    autotools.make("-j1 test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/bin/perl")
    # Conflicts with perl-Module-Build
    pisitools.remove("/usr/bin/config_data")

    pisitools.dosym("/usr/bin/perl%s" % get.srcVERSION(), "/usr/bin/perl")

    # Perl5 library
    # NEEDS MODIFICATION FOR NEW VERSION
    pisitools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so")
    pisitools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so.5")
    pisitools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so.5.16")
    pisitools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so.5.16.2")

    # Docs
    pisitools.dodir("/usr/share/doc/%s/html" % get.srcNAME())
    shelltools.system('LD_LIBRARY_PATH=%s ./perl installhtml \
                       --podroot="." \
                       --podpath="lib:ext:pod:vms" \
                       --recurse \
                       --htmldir="%s/usr/share/doc/%s/html"' % (get.curDIR(), get.installDIR(), get.srcNAME()))

    pisitools.dodoc("Changes*", "Artistic", "Copying", "README", "AUTHORS")
