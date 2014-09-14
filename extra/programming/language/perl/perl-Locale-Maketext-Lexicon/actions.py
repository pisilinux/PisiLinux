#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

# Disable tests temporarily:
#   Failed test 'no warnings on blank lines'
#   at t/1-basic.t line 25.
#
def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("README", "AUTHORS", "Changes")

