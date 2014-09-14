#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

pisitools.cflags.add("-D_LARGEFILE64_SOURCE", "-D_FILE_OFFSET_BITS=64")

def setup():
    # fix linkage
    pisitools.dosed("pam_cap/Makefile", "(.*<\s\$\(LDLIBS\))", r"\1 -lpam")
    # no static libs
    pisitools.dosed("libcap/Makefile", "install.*STALIBNAME", deleteLine=True)
    # change shared libs mode
    pisitools.dosed("libcap/Makefile", "(.*?install -m) 0644 (.*?MINLIBNAME.*)", r"\1 0755 \2")
    # use pisilinux flags
    pisitools.dosed("Make.Rules", "^(CC|CFLAGS|LD)\s:=.*", deleteLine=True)

    pisitools.dosed("Make.Rules", "^(PAM_CAP\s:=).*", r"\1 %s" % ("no" if get.buildTYPE() == "emul32" else "yes"))

def build():
    autotools.make("lib_prefix=/usr lib=lib%s" % ("32" if get.buildTYPE() == "emul32" else ""))

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("prefix=/emul32 lib=../usr/lib32 DESTDIR=%s RAISE_SETFCAP=no" % get.installDIR())
        return

    autotools.rawInstall("prefix=/usr DESTDIR=%s SBINDIR=%s/sbin RAISE_SETFCAP=no" % ((get.installDIR(),)*2))

    pisitools.insinto("/etc/security", "pam_cap/capability.conf")

    pisitools.dodoc("CHANGELOG", "License", "README", "doc/capability.notes")
