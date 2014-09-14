#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="."

def install():
    shelltools.chmod("*.otf",0644)

    pisitools.insinto("/usr/share/fonts/inconsolata","*.otf")

    pisitools.dosym("../conf.avail/inconsolata-fonts-fontconfig.conf", "/etc/fonts/conf.d/inconsolata-fonts-fontconfig.conf")
