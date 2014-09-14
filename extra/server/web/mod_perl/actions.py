#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules

def setup():
    pisitools.cflags.add("-fpic")
    shelltools.system("sed -i -e 's:^Apache-\(Reload\|SizeLimit\|Test\).*::' lib/Bundle/Apache2.pm") 
    perlmodules.configure("MP_APR_CONFIG=/usr/bin/apr-1-config MP_APU_CONFIG=/usr/bin/apu-1-config MP_USE_DSO=1 \
                           MP_APXS=/usr/bin/apxs")

    #pisitools.dosed("WrapXS/Apache2/Connection/Connection.xs", "remote_addr;", "remote_ip;")
    shelltools.system("sed -i -e 's:^Apache-\(Reload\|SizeLimit\|Test\).*::' lib/Bundle/Apache2.pm") 

def build():
    perlmodules.make()

def check():
    # Tests fail without LC_ALL=C. This is achieved with fix-tests.patch
    # but still running test through pisi hangs. Type make test in workDIR.
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodir("/var/www/localhost/cgi-perl")

    # remove conflicted files
    pisitools.remove("/usr/share/man/man3/Apache::Test*")
    pisitools.remove("/usr/share/man/man3/Bundle::ApacheTest.3pm")
