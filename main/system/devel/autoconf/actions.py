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
    # Fixup version
    shelltools.echo(".version", get.srcVERSION().split("_")[0])

    # Disable emacs scripts
    shelltools.export("EMACS", "no")

    autotools.configure()

def build():
    autotools.make()

# takes too long, do it by hand
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # binutils installs this infopage
    pisitools.remove("/usr/share/info/standards.info")

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog*", "NEWS", "README")
