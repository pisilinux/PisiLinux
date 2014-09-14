#!/usr/bin/python
# -*- coding: utf-8 -*-·
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir ="PyGreSQL-%s" % get.srcVERSION()

def install():
     pythonmodules.install()
     pisitools.rename("/usr/lib/%s/site-packages/_pg.so" % get.curPYTHON(), "_pgmodule.so")
     pisitools.dodoc("docs/*")
     pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "tutorial")
