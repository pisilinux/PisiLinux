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
    pisitools.remove("/usr/share/akonadi/agents/googlecontactsresource.desktop")
    pisitools.remove("/usr/share/akonadi/agents/googlecalendarresource.desktop")
    pisitools.remove("/usr/bin/akonadi_googlecalendar_resource")
    pisitools.remove("/usr/bin/akonadi_googlecontacts_resource")

    pisitools.dodoc("CHANGELOG", "LICENSE", "README", "TODO")
