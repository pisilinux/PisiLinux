#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mmm-mode-%s" % get.srcVERSION()

def setup():
    autotools.configure("--with-emacs \
                         --with-lispdir=/usr/share/emacs/site-lisp/mmm-mode")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.doinfo("*.info*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
