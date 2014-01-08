#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def build():
    autotools.make("PREFIX=/usr")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


# You can use these as variables, they will replace GUI values before build.
# Package Name : smtube
# Version : 1.8
# Summary : SMPlayer is a free media player for Windows and Linux with built-in codecs

# For more information, you can look at the Actions API
# from the Help menu and toolbar.

# By PiSiDo 2.0.0
