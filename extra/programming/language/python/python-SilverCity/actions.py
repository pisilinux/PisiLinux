#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "SilverCity-%s" % get.srcVERSION()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dosed("%s/usr/bin/cgi-styler-form.py" % get.installDIR(), "home/sweetapp/")

    pisitools.chmod("%s/usr/lib/%s/site-packages/SilverCity/default.css" % (get.installDIR(), get.curPYTHON()), 0644)
