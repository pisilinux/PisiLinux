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
    #https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=741767
    pisitools.dosed("cli/complete.c", "CPPFunction *", "rl_completion_func_t *")
    autotools.configure()
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/applications", "gnome/gretl.desktop")
    pisitools.insinto("/usr/share/pixmaps", "gnome/gretl.png")
    pisitools.insinto("/usr/share/emacs/site-lisp", "utils/emacs/gretl.el")

    pisitools.doman("gretlcli.1")
    pisitools.removeDir("/usr/share/gretl/doc")

    pisitools.dodoc( "ChangeLog", "CompatLog", "COPYING", "README", "README.audio")
