#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.cd("../")
    shelltools.makedirs("gst-next")
    shelltools.copy("gstreamer-vaapi-0.5.8/*", "gst-next")
    shelltools.cd("gst-next")
    autotools.configure("--prefix=/usr --disable-static")
    
    shelltools.cd("../")
    shelltools.cd("gstreamer-vaapi-0.5.8")
    autotools.configure("--with-gstreamer-api=0.10")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    shelltools.cd("../")
    shelltools.cd("gst-next")
    autotools.make()
    
    shelltools.cd("../")
    shelltools.cd("gstreamer-vaapi-0.5.8")
    autotools.make()

def install():
    shelltools.cd("../")
    shelltools.cd("gst-next")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("../")
    shelltools.cd("gstreamer-vaapi-0.5.8")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "NEWS", "README")