#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "wordlist"

def build():
    #unzip -LL in Makefile, convert DICT-hede filename to dIct-hede, this should be language neutral
    shelltools.export("LC_ALL", "C")
    autotools.make("-j1")

    shelltools.cd("scowl/speller")
    autotools.make("hunspell")

def install():
    pisitools.insinto("/usr/share/hunspell/", "en_*.dic")
    pisitools.insinto("/usr/share/hunspell/", "en_*.aff")

    pisitools.insinto("/usr/share/hunspell/", "scowl/speller/en_*.dic")
    pisitools.insinto("/usr/share/hunspell/", "scowl/speller/en_*.aff")

    for f in ("en_AU", "en_BS", "en_BW", "en_BZ", "en_DK", "en_GH", "en_HK", "en_IE", "en_IN", "en_JM", "en_NA", "en_NG", "en_NZ", "en_SG", "en_TT", "en_ZA", "en_ZW"):
        pisitools.dosym("en_GB.dic", "/usr/share/hunspell/%s.dic" % f)
        pisitools.dosym("en_GB.aff", "/usr/share/hunspell/%s.aff" % f)

    pisitools.dosym("en_US.dic", "/usr/share/hunspell/en_PH.dic")
    pisitools.dosym("en_US.aff", "/usr/share/hunspell/en_PH.aff")

    pisitools.dodoc("README*", "scowl/speller/README*")
