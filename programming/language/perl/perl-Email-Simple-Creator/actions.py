#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()
    pisitools.remove("/usr/share/man/man3/Email::Simple::Creator.3pm")
    pisitools.remove("/usr/lib/perl5/vendor_perl/5.16.2/Email/Simple/Creator.pm")
    pisitools.remove("/usr/share/man/man3/Email::Simple::Header.3pm")
    pisitools.remove("/usr/lib/perl5/vendor_perl/5.16.2/Email/Simple.pm")
    pisitools.remove("/usr/lib/perl5/vendor_perl/5.16.2/Email/Simple/Header.pm")
    pisitools.remove("/usr/share/man/man3/Email::Simple.3pm")

    pisitools.dodoc("Changes", "README")
