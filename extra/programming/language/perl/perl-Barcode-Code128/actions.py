#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
    #Skip broken PNG/GIF tests in make check
    #http://www.mail-archive.com/pld-cvs-commit@lists.pld-linux.org/msg63124.html

    shelltools.move("t/png.t", "t/png.t.broken")
    shelltools.move("t/gif.t", "t/gif.t.broken")

    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

