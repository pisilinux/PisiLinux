#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-lilv \
                         --enable-suil  \
                         --enable-librubberband \
                         --enable-libsamplerate \
                         --enable-lv2 \
                         --enable-nsm \
                         --enable-dssi \
                         --enable-vestige \
                         --enable-ladspa \
                         --enable-liblo")
#                         --localedir=/usr/share/locale")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "AUTHORS", "TODO", "ChangeLog")
