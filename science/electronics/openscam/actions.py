#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import scons
from pisi.actionsapi import get


def build():
    scons.make("-C cbang compiler=gnu")
    scons.make("compiler=gnu")
    
def install():
    scons.install("install compiler=gnu install_prefix=%s/usr" % get.installDIR()) 

 
