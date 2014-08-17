#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.dobin("src/command-not-found")

    pisitools.insinto("/var/db/command-not-found", "data/packages.db")

    for lang in ["da", "de", "es", "fr", "hr", "hu", "it", "nl", "pl", "pt_BR", "ru", "sv", "tr"]:
        pisitools.domo("po/%s.po" % lang, lang, "command-not-found.mo")

    pisitools.dodoc("AUTHORS", "COPYING", "README")