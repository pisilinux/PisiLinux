#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def install():
    pythonmodules.install()
    
    pisitools.dosed("%s/usr/share/applications/user-manager.desktop" % get.installDIR(), "Categories=Qt;KDE;System;", "Categories=Qt;KDE;X-KDE-settings-system;")