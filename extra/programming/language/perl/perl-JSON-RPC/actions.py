#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("perl Build.PL")

def build():
    shelltools.system("perl Build")

def check():
    shelltools.system("perl Build test")

def install():
    pisitools.insinto("/usr/lib/perl5/site_perl/5.20.0/", "lib/*")
    
    perlmodules.removePodfiles()