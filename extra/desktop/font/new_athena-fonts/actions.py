#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools

WorkDir="NAU3_502"

def install():
    pisitools.insinto("/usr/share/fonts/new_athena","newathu.ttf", "new_athena.ttf");
    pisitools.dodoc("*.pdf","*.rtf");

