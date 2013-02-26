#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools


def build():
    pisitools.dosed("pc/series60-remote.desktop", "Network;Office;", "Utility;TelephonyTools;")
    pythonmodules.compile()

def install():
    pythonmodules.install()

# By PiSiDo 2.0.0
