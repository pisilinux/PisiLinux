#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="Gtk2-%s" % get.srcVERSION()
examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())
demo = "%s/%s/demo" % (get.docDIR(), get.srcNAME())

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

#def check():
#    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.insinto(examples, "examples/*")
    pisitools.insinto(demo, "gtk-demo/*")

    pisitools.dodoc("AUTHORS", "NEWS", "README", "TODO")
