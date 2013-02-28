#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="%s-%s%s" % (get.srcNAME(), get.srcVERSION()[:-2], get.srcVERSION()[-2:].replace(".", "-"))

def setup():
    shelltools.cd("src")
    autotools.autoreconf("-fi")
    autotools.configure("--enable-jack \
                         --enable-alsa \
                         --enable-fftw \
                         --enable-portaudio \
                         --enable-portmidi")

def build():
    shelltools.cd("src")
    autotools.make()

def install():
    shelltools.cd("src")
    autotools.install()

    pisitools.dodoc("../LICENSE.txt", "../README.txt", "*.txt")
