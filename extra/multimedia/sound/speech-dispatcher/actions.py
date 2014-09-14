#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --without-ibmtts \
                         --without-nas \
                         --with-ivona \
                         --with-alsa \
                         --with-espeak \
                         --with-libao \
                         --with-pulse")

def build():
    autotools.make()

def install():
    autotools.install()

    # Conflicts with openTTS
    pisitools.remove("/usr/share/info/ssip.info")

    # Set executable bit
    shelltools.chmod("%s/usr/lib/python3.4/site-packages/speechd/_test.py" % get.installDIR(), 0755)

    # Create log directory, it should be world unreadable
    pisitools.dodir("/var/log/speech-dispatcher")
    shelltools.chmod("%s/var/log/speech-dispatcher" % get.installDIR(), 0700)

    pisitools.dodoc("AUTHORS", "COPYING", "README")
