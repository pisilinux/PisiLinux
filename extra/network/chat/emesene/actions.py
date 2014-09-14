#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    # Use /usr/share instead of /usr/lib
    from distutils.dir_util import copy_tree
    copy_tree("%s/usr/lib/python2.7/site-packages/emesene" % get.installDIR(), "%s/usr/share/emesene" % get.installDIR())

    pisitools.removeDir("/usr/lib")



