#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools


def install():
    pisitools.insinto("/usr/share/icons", "Faenza")
    pisitools.insinto("/usr/share/icons", "Faenza-Ambiance")
    pisitools.insinto("/usr/share/icons", "Faenza-Dark")
    pisitools.insinto("/usr/share/icons", "Faenza-Darker")
    pisitools.insinto("/usr/share/icons", "Faenza-Darkest")
    pisitools.insinto("/usr/share/icons", "Faenza-Radiance")
