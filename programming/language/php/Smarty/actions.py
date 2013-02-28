#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/php5/smarty/", "libs/*")

    pisitools.dodoc("COPYING.lib", "SMARTY2_BC_NOTES",  "README")
