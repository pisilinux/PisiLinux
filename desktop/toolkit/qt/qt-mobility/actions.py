# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import qt4

def setup():
    shelltools.system("./configure \
                      -prefix /usr\
                      -bindir /usr/bin \
                      -headerdir /usr/include \
                      -libdir /usr/lib/qt4 \
                      -plugindir /usr/lib/qt4/plugins \
                      -release")

def build():
    qt4.make()

def install():    
    qt4.install()
