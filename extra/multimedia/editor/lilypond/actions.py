#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("GUILE", "/usr/bin/guile1.8")
    shelltools.export("GUILE_CONFIG", "/usr/bin/guile-config1.8")
    shelltools.export("LDFLAGS", "-lpthread")
    pisitools.dosed("config.make.in", "^elispdir = .*$", "elispdir = $(datadir)/emacs/site-lisp/lilypond")
    pisitools.dosed("lily/freetype-error.cc", "freetype/fterrors.h", "freetype2/fterrors.h")
    pisitools.dosed("lily/pango-font.cc", "freetype/ftxf86.h", "freetype2/ftxf86.h")
    pisitools.dosed("lily/ttf.cc", "freetype/tttables.h", "freetype2/tttables.h")    
    pisitools.dosed("lily/open-type-font.cc", "freetype/tttables.h", "freetype2/tttables.h")
    autotools.configure("--with-ncsb-dir=/usr/share/fonts/default/ghostscript  --disable-documentation --disable-optimising --disable-pipe")
    shelltools.system("sed -i 's|GUILE_CFLAGS=.*|GUILE_CFLAGS=`pkg-config --cflags guile-1.8`|' configure")
    shelltools.system("sed -i 's|GUILE_LDFLAGS=.*|GUILE_LDFLAGS=`pkg-config --libs guile-1.8`|' configure")

def build():
    shelltools.export("LC_ALL", "C")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s vimdir=/usr/share/vim/vimfiles" % get.installDIR())

    pisitools.dodoc("COPYING", "NEWS.txt", "README.txt", "VERSION", "ROADMAP")
