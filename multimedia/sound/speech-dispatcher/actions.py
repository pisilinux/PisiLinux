#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

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

    # Rename generically named binaries
    pisitools.rename("/usr/bin/long_message", "spd_long_message")
    pisitools.rename("/usr/bin/run_test", "spd_run_test")

    # Remove configuration files from /usr/share
    pisitools.removeDir("/usr/share/speech-dispatcher")

    # Set executable bit
    shelltools.chmod("%s/usr/lib/%s/site-packages/speechd/_test.py" % (get.installDIR(), get.curPYTHON()), 0755)

    # Create log directory, it should be world unreadable
    pisitools.dodir("/var/log/speech-dispatcher")
    shelltools.chmod("%s/var/log/speech-dispatcher" % get.installDIR(), 0700)

    pisitools.dodoc("AUTHORS", "COPYING", "README")
