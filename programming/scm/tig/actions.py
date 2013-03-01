#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    autotools.install(argument="install-doc-man")

    pisitools.insinto("/etc/bash_completion.d", "contrib/tig-completion.bash", "tig")
    pisitools.insinto("/etc", "contrib/tigrc")

    pisitools.dodoc("BUGS", "COPYING", "NEWS", "README", "SITES", "TODO", "manual.txt")
    pisitools.dohtml("*.html")
