#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
	shelltools.cd("styles")
	for d in ["green_tea", "ostrich", "carp"]:
		pisitools.unlinkDir(d)
	
	shelltools.cd("..")
	pisitools.insinto("/usr/share/fluxbox/styles/", "*")
	
	pisitools.dodoc("License")