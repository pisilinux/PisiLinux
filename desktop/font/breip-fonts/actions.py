#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools

WorkDir="Breip"

def install():
    pisitools.insinto("/usr/share/fonts/breip/", "*.ttf");
    pisitools.dodoc("COPYING","Breip.sfd","Font test.doc",);

