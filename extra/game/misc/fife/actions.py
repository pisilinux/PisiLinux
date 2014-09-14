#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def build():
    scons.make("-j1 fife-shared fife-python \
                --lib-dir=/usr/lib \
	        --prefix=/usr \
	        --python-prefix=/usr/lib/python2.7/site-packages/ ")
	        
def install():
    scons.install("-j1 install-shared install-python install-dev \
	           --lib-dir=/usr/lib \
	           --prefix=/usr \
	           --python-prefix=/usr/lib/python2.7/site-packages/ \
	           --install-sandbox=%s" % get.installDIR())

