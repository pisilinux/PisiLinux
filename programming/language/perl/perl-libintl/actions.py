#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "libintl-perl-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

# FIXME: needs glibc-locale packages to work
def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("ChangeLog","NEWS", "COPYING.LESSER", "README", "TODO", "THANKS", "FAQ")
