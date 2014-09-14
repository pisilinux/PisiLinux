#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # Force swig to regenerate the wrapper
    shelltools.system("rm -f php/redland_wrap.c")
    shelltools.system("rm -f perl/CORE_wrap.c")
    
    shelltools.export("LDFLAGS", "")

    autotools.configure("--disable-dependency-tracking \
                         --disable-static \
                         --with-python \
                         --with-python-ldflags='-shared -lrdf' \
                         --with-perl \
                         --with-php \
                         --with-ruby")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING*", "NEWS", "README", "TODO")
    pisitools.dohtml("*.html")

    pisitools.remove("/usr/lib/perl5/5.20.0/x86_64-linux-thread-multi/perllocal.pod")

