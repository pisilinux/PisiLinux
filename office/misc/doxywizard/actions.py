# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt4
from pisi.actionsapi import get

WorkDir = "doxygen-%s/addon/doxywizard" % get.srcVERSION()

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    pisitools.dodoc("README")

    shelltools.cd("../..")
    pisitools.dobin("bin/doxywizard")
    pisitools.doman("doc/doxywizard.1")

    pisitools.dodoc("LICENSE", "VERSION")
