#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    shelltools.system("python bootstrap.py")
    shelltools.system("asciidoc doc/manual.asciidoc")

def check():
    #needs new package gtest -> ignore it for now
    shelltools.system("python ./configure.py --with-gtest=/usr/share/gtest")
    shelltools.system("./ninja ninja_test")
    shelltools.system("./ninja_test --gtest_filter=-SubprocessTest.SetWithLots")

def install():
    pisitools.dobin("ninja", "/usr/bin")

    pisitools.insinto("/usr/share/bash-completion/completions", "misc/bash-completion", "ninja")

    pisitools.dodoc("HACKING.md", "COPYING", "RELEASING", "README", "doc/manual.asciidoc")

    pisitools.dohtml("doc/manual.html")