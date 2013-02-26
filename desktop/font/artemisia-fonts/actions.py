#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools

WorkDir="ttf-gfs-artemisia-1.1"

def install():
    pisitools.insinto("/usr/share/fonts/artemisia","*.otf");
    pisitools.dodoc("*.txt");

