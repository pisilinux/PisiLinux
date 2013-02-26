#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def build():
    shelltools.system("gnuchess --addbook=book_1.02.pgn")

def install():
    pisitools.insinto("/usr/share/games/gnuchess/", "book.bin")
