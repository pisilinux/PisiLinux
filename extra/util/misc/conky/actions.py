#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
    
def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --enable-curl \
                         --enable-weather-xoap \
                         --enable-rss \
                         --enable-weather-metar \
                         --enable-imlib2 \
                         --enable-wlan \
                         --enable-ibm \
                         --enable-lua \
                         --enable-lua-cario \
                         --enable-hddtemp \
                         --enable-x11 \
                         --enable-xdamage \
	                 --enable-xft \
                         --enable-alsa ")
 
def build():
  autotools.make()
  
def install():
  autotools.rawInstall("DESTDIR=%s"%get.installDIR())
  
  pisitools.dodoc("AUTHORS","COPYING","README")