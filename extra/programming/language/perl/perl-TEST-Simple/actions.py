#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.remove("/usr/share/man/man3/Test::Builder::Module.3pm")
    pisitools.remove("/usr/share/man/man3/Test::Builder::Tester::Color.3pm")
    pisitools.remove("/usr/share/man/man3/Test::Simple.3pm")
    pisitools.remove("/usr/share/man/man3/Test::Tutorial.3pm")
    pisitools.remove("/usr/share/man/man3/Test::More.3pm")
    pisitools.remove("/usr/share/man/man3/Test::Builder::Tester.3pm")
    pisitools.remove("/usr/share/man/man3/Test::Builder.3pm")

    pisitools.dodoc("Changes", "MANIFEST", "README")
