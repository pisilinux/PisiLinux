#!/usr/bin/python
# -*- coding: utf-8 -*-·
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
#    pythonmodules.configure()
    pythonmodules.compile()

def install():
    pythonmodules.install()
    shelltools.system("rm -rf %s/usr/bin" % get.installDIR())
    shelltools.system("rm -rf %s/usr/share/man" % get.installDIR())

