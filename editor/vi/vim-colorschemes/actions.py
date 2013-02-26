#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "vim-colorschemes-%s" % get.srcVERSION().split("_")[1]
NoStrip = "/"

vimdir = "/usr/share/vim/vimfiles/colors"
DoNotAdd = ["blue.vim",
            "darkblue.vim",
            "default.vim",
            "delek.vim",
            "desert.vim",
            "elflord.vim",
            "evening.vim",
            "koehler.vim",
            "morning.vim",
            "murphy.vim",
            "pablo.vim",
            "peachpuff.vim",
            "redstring.vim",
            "ron.vim",
            "shine.vim",
            "slate.vim",
            "torte.vim",
            "zellner.vim"]

def setup():
    for f in shelltools.ls("./"):
        shelltools.chmod(f, 0644)

def install():
    for f in shelltools.ls("./"):
        if f not in DoNotAdd:
            pisitools.insinto(vimdir, f)

