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
from pisi.actionsapi import libtools
from pisi.actionsapi import texlivemodules

import os

WorkDir = "."

def setup():
    if get.ARCH() == "x86_64":
        shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())

    shelltools.cd("/%s/source/" % get.workDIR())

    # prevent compiling Xdvi with libXp
    # it's a workaround should be fixed with a better regex pattern
    pisitools.dosed("texk/xdvik/configure","-lXp ")

    shelltools.makedirs("%s/source/build" % get.workDIR())
    shelltools.cd("%s/source/build" % get.workDIR())

    shelltools.sym("../configure", "configure")
    autotools.configure("--disable-native-texlive-build \
                         --with-banner-add=\"/Pardus\" \
                         --disable-multiplatform \
                         --disable-chktex \
                         --disable-dialog \
                         --disable-dialog \
                         --disable-detex \
                         --disable-dvipng \
                         --disable-dvi2tty \
                         --disable-dvipdfmx \
                         --disable-lcdf-typetools \
                         --disable-ps2eps \
                         --disable-psutils \
                         --disable-t1utils \
                         --disable-bibtexu \
                         --disable-xz \
                         --disable-xdvik \
                         --with-system-zlib \
                         --with-system-pnglib \
                         --with-system-ncurses \
                         --with-system-t1lib \
                         --with-system-gd \
                         --with-system-xpdf \
                         --with-system-freetype2 \
                         --with-freetype2-libdir=/usr/lib \
                         --with-freetype2-include=/usr/include/freetype2 \
                         --with-xdvi-x-toolkit=xaw \
                         --disable-dump-share \
                         --disable-aleph \
                         --disable-luatex \
                         --with-clisp-runtime=default \
                         --enable-xindy --disable-xindy-rules --disable-xindy-docs")

def build():
    shelltools.cd("%s/source/build" % get.workDIR())
    autotools.make()

def install():
    # install texmf tree
    folders = ["/usr/share",
               "/etc/texmf/web2c",
               "/etc/texmf/chktex",
               "/etc/texmf/dvips/config",
               "/etc/texmf/dvipdfm/config",
               "/etc/texmf/dvipdfmx",
               "/etc/texmf/tex/generic/config",
               "/etc/texmf/ttf2pk",
               "/etc/texmf/xdvi",
               "/etc/fonts/conf.avail"]

    for dirs in folders:
        pisitools.dodir(dirs)

    pisitools.insinto("/usr/share", "texmf")
    pisitools.insinto("/etc/fonts/conf.avail/", "09-texlive-fonts.conf")

    # replace upstream texmf.cnf with ours
    pisitools.remove("/usr/share/texmf/web2c/texmf.cnf")
    pisitools.insinto("/etc/texmf/web2c/", "texmf.cnf")

    # the location of texmf.cnf is hard-wired to be under /usr/share/texmf/web2c
    # we make a symlink from /etc/texmf/web2c/texmf.cnf to the latter
    pisitools.dosym("/etc/texmf/web2c/texmf.cnf", "/usr/share/texmf/web2c/texmf.cnf")

    # fix location of TEXMFCACHE for luatools
    pisitools.dosed("%s/usr/share/texmf/web2c/texmfcnf.lua" % get.installDIR(), "texlive2010", "texlive")

    # remove aleph from fmtutil.cnf
    pisitools.dosed("%s/usr/share/texmf/web2c/fmtutil.cnf" % get.installDIR(), "^.*aleph.*$")

    # move man files to /usr/share/man, check for new man files at every update
    for man in ["1", "5"]:
        pisitools.domove("/usr/share/texmf/doc/man/man%s" % man, "/usr/share/man/")

    # move info files to /usr/share/info
    pisitools.domove("/usr/share/texmf/doc/info", "/usr/share")

    # copy config files to $TEXMFSYSCONFIG tree (defined in texmf.cnf)
    config_files = [ "/usr/share/texmf/chktex/chktexrc",
                     "/usr/share/texmf/web2c/mktex.cnf",
                     "/usr/share/texmf/web2c/updmap.cfg",
                     "/usr/share/texmf/web2c/fmtutil.cnf",
                     "/usr/share/texmf/dvips/config/config.ps",
                     "/usr/share/texmf/dvipdfmx/dvipdfmx.cfg",
                     "/usr/share/texmf/tex/generic/config/pdftexconfig.tex",
                     "/usr/share/texmf/tex/generic/config/language.dat",
                     "/usr/share/texmf/tex/generic/config/language.def",
                     "/usr/share/texmf/ttf2pk/ttf2pk.cfg",
                     "/usr/share/texmf/xdvi/XDvi"]

    for share_file in config_files:
        etc_file = share_file.replace("/usr/share", "/etc")
        shelltools.copy("%s/%s" % (get.installDIR(), share_file) , "%s/%s" % (get.installDIR(), etc_file))

    # clean updmap.cfg
    pisitools.dosed("%s/etc/texmf/web2c/updmap.cfg" % get.installDIR(), "^(Map|MixedMap).*$")
    pisitools.dosed("%s/etc/texmf/web2c/updmap.cfg" % get.installDIR(), "^#! (Map|MixedMap).*$")

    ################################################################
    ########### make install

    shelltools.cd("%s/source/build" % get.workDIR())

    # prefix should be user defined, we don't need all files
    autotools.install("prefix=%s/source/build/usr texmf=%s/usr/share/texmf" % (get.workDIR(), get.installDIR()))

    shelltools.move("%s/source/build/usr/bin" % get.workDIR(), "%s/usr" % get.installDIR())
    shelltools.move("%s/source/build/usr/lib" % get.workDIR(), "%s/usr" % get.installDIR())
    shelltools.move("%s/source/build/usr/include" % get.workDIR(), "%s/usr" % get.installDIR())

    # fix symlinks, some are incorrect
    # makefile patching is another way, but there are lot of scripts
    # pathing each makefile makes it much harder, for now this is a "simpler" solution
    for binary in shelltools.ls(get.installDIR() + "/usr/bin"):
        real_path = shelltools.realPath(get.installDIR() + "/usr/bin/" + binary)
        if "texmf" in real_path and not os.path.exists(real_path): # modify only if it is broken
            base_path = real_path.replace(get.installDIR() + "/usr", "")
            new_path = "/usr/share" + base_path
            shelltools.unlink(get.installDIR() + "/usr/bin/" + binary)
            pisitools.dosym(new_path, "/usr/bin/" + binary)

    # create symlinks for formats
    # shelltools.export("PATH", get.installDIR() + "/usr/bin")
    shelltools.system("PATH=\"$PATH:%s/usr/bin\" texlinks -f %s/usr/share/texmf/web2c/fmtutil.cnf %s/usr/bin/" % (get.installDIR(), get.installDIR(), get.installDIR()))

    # remove symlinks to scripts that are not in texlive-bin or texlive-core:
    symlinks_to_remove = ["authorindex",
                          "ebong",
                          "bibexport",
                          "cachepic",
                          "epspdf",
                          "epspdftk",
                          "fig4latex",
                          "makeglossaries",
                          "mathspic",
                          "mkgrkindex",
                          "pdfannotextractor",
                          "perltex",
                          "pst2pdf",
                          "ps4pdf",
                          "splitindex",
                          "svn-multi",
                          "htcontext",
                          "htlatex",
                          "htmex",
                          "ht",
                          "httexi",
                          "httex",
                          "htxelatex",
                          "htxetex",
                          "mk4ht",
                          "ulqda",
                          "vpe",
                          "tlmgr"]

    for symlink in symlinks_to_remove:
        pisitools.remove("/usr/bin/%s" % symlink)


    # remove files form disabled packages
    # we copy all man and info files into mandir. Disabling packages just remove binaries.
    # the remaining man and info files should be deleted manually

    # dvipng
    pisitools.remove("/usr/share/man/man1/dvipng.1")
    pisitools.remove("/usr/share/info/dvipng.info")
    pisitools.remove("/usr/share/man/man1/dvigif.1")

    # lcdf-typetools
    pisitools.remove("/usr/share/man/man1/t1rawafm.1")
    pisitools.remove("/usr/share/man/man1/cfftot1.1")
    pisitools.remove("/usr/share/man/man1/t1lint.1")
    pisitools.remove("/usr/share/man/man1/ttftotype42.1")
    pisitools.remove("/usr/share/man/man1/t1dotlessj.1")
    pisitools.remove("/usr/share/man/man1/mmpfb.1")
    pisitools.remove("/usr/share/man/man1/otftotfm.1")
    pisitools.remove("/usr/share/man/man1/otfinfo.1")
    pisitools.remove("/usr/share/man/man1/t1testpage.1")
    pisitools.remove("/usr/share/man/man1/mmafm.1")
    pisitools.remove("/usr/share/man/man1/t1reencode.1")

    # chktex
    pisitools.remove("/usr/share/man/man1/deweb.1")

    # dvi2tty
    pisitools.remove("/usr/share/man/man1/dvi2tty.1")

    # dvipdfm
    pisitools.remove("/usr/share/texmf/tex/latex/dvipdfm/dvipdfm.def")
    pisitools.remove("/usr/share/man/man1/dvipdfm.1")
    pisitools.remove("/usr/share/texmf/dvipdfm/config/config")

    # xdvik
    pisitools.remove("/usr/share/man/man1/xdvi.1")
    pisitools.remove("/usr/share/texmf/xdvi/xdvi.cfg")
    pisitools.remove("/usr/share/texmf/xdvi/XDvi")

    #ps2eps
    pisitools.remove("/usr/share/man/man1/bbox.1")
    pisitools.remove("/usr/share/man/man1/ps2eps.1")
