#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # https://bugs.freedesktop.org/show_bug.cgi?id=70366
    shelltools.export("ac_cv_func_fdatasync", "no")

    autotools.configure("--disable-update-mimedb")

def build():
    autotools.make('-j1')

def check():
    autotools.make("check")

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "NEWS", "README")
