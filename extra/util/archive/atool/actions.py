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

    pisitools.insinto("/etc/bash_completion.d/", "extra/bash-completion-atool_0.1-1", "atool")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "NEWS", "TODO")
