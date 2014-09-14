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
    autotools.configure("--enable-everything \
                         --enable-perl \
                         --disable-iso14755 \
                         --enable-mousewheel \
                         --enable-slipwheeling \
                         --enable-xft \
                         --enable-pixbuf \
                         --enable-font-styles \
                         --enable-transparency \
                         --enable-fading \
                         --enable-smart-resize \
                         --enable-text-blink \
                         --enable-pointer-blank \
                         --enable-utmp \
                         --enable-wtmp \
                         --enable-rxvt-scroll \
                         --enable-next-scroll \
                         --enable-xterm-scroll \
                         --enable-frills \
                         --enable-keepscrolling \
                         --enable-selectionscrolling \
                         --enable-font-styles \
                         --enable-256-color \
                         --enable-combining")

def build():
    autotools.make()
    pisitools.dosed("doc/rxvt-tabbed", "RXVT_BASENAME = \"rxvt\"", "RXVT_BASENAME = \"urxvt\"")

def install():
    shelltools.export("TERMINFO", "%s/usr/share/terminfo" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/terminfo/r", "doc/etc/rxvt-unicode.terminfo", "rxvt-unicode")
    pisitools.insinto("/etc", "doc/etc/rxvt-unicode.termcap")

    shelltools.chmod("%s/usr/share/terminfo/r/rxvt-unicode" % get.installDIR(), 0644)
    shelltools.chmod("%s/etc/rxvt-unicode.termcap" % get.installDIR(), 0644)

    pisitools.dodoc("README.FAQ", "Changes", "doc/README*", "doc/changes.txt", "doc/rxvt-tabbed")

    # Should be provided by ncurses
    pisitools.remove("/usr/share/terminfo/r/rxvt-unicode")
