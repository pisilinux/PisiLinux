#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())
examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def setup():
    perlmodules.configure()
    shelltools.chmod("examples/*", 0644)

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.insinto(examples, "examples/*")
    pisitools.dodoc("ChangeLog", "README")
