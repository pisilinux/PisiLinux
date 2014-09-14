#/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/lib/*.a")
    pisitools.removeDir("/usr/share/doc/wordnet/ps")
    pisitools.domove("/usr/share/wnres", "/usr/share/wordnet")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "LICENSE", "README")
