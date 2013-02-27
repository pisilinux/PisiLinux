#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc('ChangeLog', 'LICENSE', 'README')

    # Remove unused hidden files
    pisitools.remove("/usr/lib/python2.7/site-packages/deluge/ui/web/js/deluge-all/.order")
    pisitools.remove("/usr/lib/python2.7/site-packages/deluge/ui/web/js/deluge-all/add/.order")
    pisitools.remove("/usr/lib/python2.7/site-packages/deluge/ui/web/js/deluge-all/data/.order")

