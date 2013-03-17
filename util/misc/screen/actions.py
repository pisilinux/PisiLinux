#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("LC_ALL", "POSIX")

def setup():
    pisitools.dosed("doc/screen.1", "/usr/local/etc/screenrc", "/etc/screenrc")
    pisitools.dosed("doc/screen.1", "/usr/local/screens", "run/screen")
    pisitools.dosed("doc/screen.1", "/local/etc/screenrc", "/etc/screenrc")
    pisitools.dosed("doc/screen.1", "/etc/utmp", "run/utmp")
    pisitools.dosed("doc/screen.1", "/local/screens/S-", "/run/screen/S-")

    # Allow for more rendition (color/attribute) changes in status bars
    pisitools.dosed("screen.c", "#define MAX_WINMSG_REND 16", "#define MAX_WINMSG_REND 64")

    shelltools.export("CFLAGS", "%s -DPTYMODE=0620 -DPTYGROUP=5 -DUSE_PAM" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -DPTYMODE=0620 -DPTYGROUP=5 -DUSE_PAM" % get.CXXFLAGS())

    autotools.autoconf()

    autotools.configure("--enable-pam \
                         --with-socket-dir=/run/screen \
                         --with-sys-screenrc=/etc/screenrc \
                         --with-pty-mode=0620 \
                         --with-pty-group=5 \
                         --enable-rxvt_osc \
                         --enable-colors256")

def build():
    autotools.make("term.h")
    autotools.make()

def install():
    pisitools.dobin("screen")

    pisitools.dodir("/run/screen")
    pisitools.dodir("/etc/pam.d")

    pisitools.insinto("/usr/share/terminfo", "terminfo/screencap")
    pisitools.insinto("/usr/share/screen/utf8encodings", "utf8encodings/??")

    shelltools.chmod("%s/run/screen" % get.installDIR(), 0775)

    pisitools.doman("doc/screen.1")
    pisitools.doinfo("doc/screen.info*")
    pisitools.dodoc("README", "ChangeLog", "TODO", "NEWS*", "doc/FAQ", "doc/README.DOTSCREEN")
