#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_PREFIX=/usr")      
                          
def build():
    cmaketools.make()

def install():    
    pisitools.insinto("/usr/share/freshplayerplugin/", "data/freshwrapper.conf.example")
    pisitools.insinto("/usr/lib/mozilla/plugins/", "libfreshwrapper-pepperflash.so")
    
    pisitools.dosed("%s/usr/share/freshplayerplugin/freshwrapper.conf.example" % get.installDIR(), "/opt/google/chrome", "/usr/lib/chromium-browser")
    
    pisitools.dodoc("COPYING", "LICENSE.MIT")