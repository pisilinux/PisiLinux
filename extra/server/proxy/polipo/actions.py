#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("all")

def install():
    autotools.install("TARGET=%s" % get.installDIR())
    pisitools.insinto("/etc/polipo", "config.sample", "config")
    pisitools.insinto("/etc/polipo", "forbidden.sample", "forbidden")
