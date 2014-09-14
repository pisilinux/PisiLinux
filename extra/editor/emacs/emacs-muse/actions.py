#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr" %get.installDIR())

    pisitools.remove("/usr/share/emacs/site-lisp/muse/*.elc")
    pisitools.remove("/usr/share/emacs/site-lisp/muse/contrib/*.elc")

    pisitools.doinfo("texi/*.info")
    pisitools.dodoc("COPYING", "AUTHORS", "NEWS", "README")
