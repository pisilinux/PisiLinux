#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("docs/reference/gck/Makefile.am", "DOC_MODULE=gck", "DOC_MODULE=mate-gck")
    autotools.autoreconf("-fi")
    libtools.libtoolize("-c -f")
    autotools.configure("--disable-static \
                         --with-gtk=2.0   \
                         --disable-gtk-doc \
                         --disable-schemas-compile \
                         --with-pam-dir=/lib/security \
                         --with-root-certs=/etc/pki/tls/certs")
    
    # fix unused-direct-shlib-dependency
    pisitools.dosed("libtool", "( -shared )", " -Wl,-O1,--as-needed\\1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # remove needless gsettings convert file to avoid slow session start
    pisitools.removeDir("/usr/share/MateConf")

    pisitools.dodoc("COPYING", "README", "NEWS", "AUTHORS", "ChangeLog")
