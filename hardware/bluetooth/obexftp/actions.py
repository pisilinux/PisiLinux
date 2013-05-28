#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("swig/python/Makefile.in", "(setup.py install)", "\\1 --no-compile")
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static \
                         --disable-dependency-tracking \
                         --disable-ruby \
                         --enable-rpath \
                         --enable-rcl \
                         --enable-perl")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.remove("/usr/lib/perl5/5.16.2/x86_64-linux-thread-multi/perllocal.pod")