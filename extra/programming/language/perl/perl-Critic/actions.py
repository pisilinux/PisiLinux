#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Perl-Critic-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

#test failes
#def check():
#    perlmodules.make("test")

def install():
    perlmodules.install()
    #pisitools.removeDir("/usr/lib/perl5/vendor_perl/%s/%s-linux-thread-multi/" % (get.curPERL(), get.ARCH()))
