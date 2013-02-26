#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().split("_")[0])

def build():
    #parallel compilation of cdda2wav exetuable is broken in this release
    autotools.make('-j1 CC="%s -D__attribute_const__=const" \
                    COPTX="-O2 -pipe" CPPOPTX="-O2 -pipe" LDOPTX="%s" \
                    LINKMODE=dynamic' % (get.CC(), get.LDFLAGS()))

def install():
    for app in ["cdrecord","cdda2wav","mkisofs","readcd"]:
        pisitools.dobin("%s/OBJ/*/%s" % (app,app))

    for app in ["devdump","isodump","isoinfo","isovfy"]:
        pisitools.dobin("mkisofs/diag/OBJ/*/%s" % app)

    pisitools.dosbin("rscsi/OBJ/*/rscsi")
    pisitools.insinto("/usr/lib","libs/*/pic/*.so*")

    pisitools.insinto("/usr/include", "incs/*/align.h")
    pisitools.insinto("/usr/include", "incs/*/avoffset.h")
    pisitools.insinto("/usr/include", "incs/*/xconfig.h")
    pisitools.insinto("/usr/include/schily", "include/schily/*.h")
    pisitools.insinto("/usr/include/scg", "libscg/scg/*.h")

    pisitools.insinto("/etc/default", "rscsi/rscsi.dfl")
    pisitools.insinto("/etc/default", "cdrecord/cdrecord.dfl")

    for man in ["btcflash/btcflash.1", "cdda2wav/cdda2ogg.1",
                "cdda2wav/cdda2wav.1", "cdda2wav/cdda2wav.1",
                "cdrecord/cdrecord.1", "readcd/readcd.1",
                "rscsi/rscsi.1"]:
        pisitools.dosed(man, "/opt/schily", "/usr")

    pisitools.doman("*/*.1", "*/*.8")

    pisitools.dodoc("ABOUT", "Changelog", "READMEs/README.linux")
