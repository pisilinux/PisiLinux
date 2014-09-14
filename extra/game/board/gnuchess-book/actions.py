#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def build():
    shelltools.system("gnuchess --addbook=book_1.02.pgn")

def install():
    pisitools.insinto("/usr/share/games/gnuchess/", "book.bin")
