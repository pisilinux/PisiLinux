#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get



def setup():
    shelltools.system("./autogen.sh")
    #autotools.autoreconf("-fiv")
    autotools.configure("--disable-doxygen-doc \
                         --with-pic \
                         --with-zlib \
                         --with-bzlib \
                         --with-openssl \
                         --with-log4cpp")

def build():
    autotools.make()
    
def check():
    autotools.make("check")    

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
