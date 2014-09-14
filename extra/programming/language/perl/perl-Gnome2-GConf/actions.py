#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    perlmodules.configure()
    pisitools.dosed("Makefile", "^OTHERLDFLAGS.*$", "OTHERLDFLAGS = %s" % get.LDFLAGS())

def build():
    perlmodules.make('GTK2_PERL_CFLAGS="%s"' % get.CFLAGS())

# tries to reach root/.gconf , some GCONF related parameter should be exported
# skip till we find a solution for this.
#def check():
#    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "examples")
    pisitools.dodoc("ChangeLog", "NEWS", "README")

