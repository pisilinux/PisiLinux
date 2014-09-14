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
    
    pisitools.flags.add("-std=c++11")    
    shelltools.system("./autogen.sh")
    autotools.configure('--enable-npapi \
                         --with-gtk \
                         --disable-static \
                         --enable-shared')


def build():
    autotools.make('LIBTOOL="/usr/bin/libtool --tag=CC"')

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/lib/mozilla/plugins/*", "/usr/lib/browser-plugins")
    pisitools.removeDir("/usr/lib/mozilla/")

    pisitools.dodoc("AUTHORS", "NEWS", "README", "COPYING")

