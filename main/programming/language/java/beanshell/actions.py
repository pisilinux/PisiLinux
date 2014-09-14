#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/java", "bsh-2.1.7.jar", "bsh.jar")
