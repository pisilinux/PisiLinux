#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

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

    #This files are included in Perl 5.18.1
    for locale in ["Codes::LangExt", "Codes::LangVar", "Codes::API", "Codes::LangFam", "Codes::Constants", "Codes::LangFam_Retired", "Currency", "Language", "Codes::Language", "Codes::Changes" , "Script", "Codes::Currency", "Codes::Country", "Codes", "Country", "Codes::Script"]:
        pisitools.remove("/usr/share/man/man3/Locale::%s.3pm" % locale)

    pisitools.dodoc("README", "Changes")

