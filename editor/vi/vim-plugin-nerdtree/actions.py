#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    for folder in ["plugin", "doc", "nerdtree_plugin"]:
        pisitools.insinto("/usr/share/vim/vimfiles/", folder)

    pisitools.dodoc("license.txt")
