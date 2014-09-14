#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4

def setup():
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()
    # remove conlicks with kdepim  
    pisitools.remove("/usr/lib/kde4/akonadi_serializer_socialfeeditem.so")
    pisitools.remove("/usr/share/kde4/apps/akonadi/plugins/serializer/akonadi_serializer_socialfeeditem.desktop")
    pisitools.remove("/usr/share/mime/packages/x-vnd.akonadi.socialfeeditem.xml")
