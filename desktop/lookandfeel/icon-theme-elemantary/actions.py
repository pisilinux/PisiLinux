#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools


def install():
    pisitools.insinto("/usr/share/icons", "elementary")
    pisitools.insinto("/usr/share/icons", "elementary-mono-dark")
    pisitools.insinto("/usr/share/icons", "elementary-gato")
    
    pisitools.dodoc("elementary/AUTHORS", "elementary/COPYING", "elementary/CONTRIBUTORS")