#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-unicode=yes \
                         --enable-clock=yes \
                         --enable-outputs=yes \
                         --with-taglib=yes \
                         --with-curl=yes")
                         #--enable-visualizer=yes \

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("usr/share/doc")
    pisitools.doman("doc/ncmpcpp.1")
    pisitools.insinto("/etc/bash_completion.d/", "doc/ncmpcpp-completion.bash", "ncmpcpp")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "doc/config", "doc/keys")
