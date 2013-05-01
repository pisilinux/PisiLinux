#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    shelltools.system('/usr/bin/apxs -o mod_fastcgi.so -c *.c')

def install():
    pisitools.insinto('/usr/lib/apache2/modules', '.libs/mod_fastcgi.so')