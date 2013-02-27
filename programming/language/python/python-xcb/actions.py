# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "xpyb-%s" % get.srcVERSION()

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

def setup():
    autotools.configure("--enable-xinput")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.rename("/usr/share/doc/xpyb", get.srcNAME())
