# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="distribute-%s" % get.srcVERSION()

def install():
    pythonmodules.install()
    pisitools.remove("/usr/lib/%s/site-packages/setuptools/*.exe" % get.curPYTHON())
