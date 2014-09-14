#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

def build():
    autotools.make("OPTIMIZE=\"%s\" PREFIX=\"/usr\"" % get.CFLAGS())

def install():
    # PREFIX for perl script, DESTDIR for c_stuff
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr" % get.installDIR())

    perlmodules.removePodfiles()

    pisitools.insinto("/usr/share/pixmaps", "icons/frozen-bubble-icon-48x48.png", "frozen-bubble.png")

    pisitools.dodoc("AUTHORS", "COPYING", "README", "NEWS", "TODO", "TIPS")
