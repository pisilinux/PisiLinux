#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    #This files are included in Perl 5.14.1
    for locale in ["Currency", "Language", "Codes::Language", "Codes::Changes" , "Script", "Codes::Currency", "Codes::Country", "Codes", "Country", "Codes::Script"]:
        pisitools.remove("/usr/share/man/man3/Locale::%s.3pm" % locale)
        #pisitools.remove("/usr/lib/perl5/vendor_perl/%s/Locale/%s.pm" % (get.curPERL(), locale))
    pisitools.remove("/usr/share/man/man3/Locale::Codes::Language_Codes.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::LangFam_Codes.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::LangExt.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::LangExt_Codes.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::Script_Retired.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::LangVar_Retired.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::LangVar_Codes.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::LangVar.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::Country_Codes.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::Language_Retired.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::Currency_Codes.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::LangFam_Retired.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::Script_Codes.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::Country_Retired.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::LangFam.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::API.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::Constants.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::Currency_Retired.3pm")
    pisitools.remove("/usr/share/man/man3/Locale::Codes::LangExt_Retired.3pm")

    pisitools.dodoc("README", "ChangeLog")

