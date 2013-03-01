#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

import os

def setup():
    autotools.configure()

def build():
    autotools.make("bash_completion.sh")

def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())

    blacklist = ["mplayer", "mount", "service"]
    for comp in blacklist:
        pisitools.remove("/etc/bash_completion.d/%s" % comp)

    pisitools.dodoc("AUTHORS", "CHANGES", "COPYING", "README", "TODO")
