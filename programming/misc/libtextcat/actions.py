#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def clearlmname(lm):
    mapping = {"irish": "irish_gaelic", "manx": "manx_gaelic", "amharic-utf": "amharic_utf", "yiddish-utf": "yiddish_utf", "serbian-ascii": "serbian_ascii", "slovak-ascii": "slovak_ascii", "rumantsch": "romansh"}
    if lm[:-3] in mapping.keys():
        return mapping[lm[:-3]] + ".lm"

    if "-" in lm:
        return lm.split("-")[0] + ".lm"
    else:
        return lm

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/libtextcat")

    #install some lm files directly to datadir
    directCopy = ["amharic-utf.lm", "yiddish-utf.lm", "afrikaans.lm", "basque.lm", "bosnian.lm", "croatian-ascii.lm", "drents.lm", "dutch.lm", "english.lm", "icelandic.lm", "indonesian.lm", "latin.lm", "malay.lm", "manx.lm", "marathi.lm", "nepali.lm", "romanian.lm", "sanskrit.lm", "scots.lm", "serbian-ascii.lm", "slovak-ascii.lm", "swahili.lm", "tagalog.lm", "welsh.lm"]

    for lm in directCopy:
        pisitools.insinto("/usr/share/libtextcat", "langclass/LM/%s" % lm, clearlmname(lm))

    convert = {"arabic-windows1256.lm": "WINDOWS-1256", "albanian.lm": "ISO-8859-1", "belarus-windows1251.lm": "WINDOWS-1251", "breton.lm": "ISO-8859-1", "catalan.lm": "ISO-8859-1", "czech-iso8859_2.lm": "ISO-8859-2", "danish.lm": "ISO-8859-1", "esperanto.lm": "ISO-8859-3", "estonian.lm": "ISO-8859-15", "finnish.lm": "ISO-8859-1", "french.lm": "ISO-8859-1", "frisian.lm": "ISO-8859-1", "georgian.lm": "ISO-8859-1", "german.lm": "ISO-8859-1", "greek-iso8859-7.lm": "ISO-8859-7", "hebrew-iso8859_8.lm": "ISO-8859-8", "hungarian.lm": "ISO-8859-2", "irish.lm": "ISO-8859-1", "italian.lm": "ISO-8859-1", "latvian.lm": "ISO-8859-13", "lithuanian.lm": "ISO-8859-13", "malay.lm": "ISO-8859-1", "middle_frisian.lm": "ISO-8859-1", "mingo.lm": "ISO-8859-1", "norwegian.lm": "ISO-8859-1", "polish.lm": "ISO-8859-2", "portuguese.lm": "ISO-8859-1", "quechua.lm": "ISO-8859-1", "rumantsch.lm": "ISO-8859-1", "russian-iso8859_5.lm": "ISO-8859-5", "scots_gaelic.lm": "ISO-8859-1", "slovenian-iso8859_2.lm": "ISO-8859-2", "spanish.lm": "ISO-8859-1", "swedish.lm": "ISO-8859-1", "turkish.lm": "ISO-8859-9", "ukrainian-koi8_r.lm": "KOI8-R", "hindi.lm": "ISO-8859-1", "persian.lm": "ISO-8859-1", "korean.lm": "ISO-8859-1", "tamil.lm": "ISO-8859-1", "thai.lm": "ISO-8859-1", "vietnamese.lm": "ISO-8859-1"}

    #fix encodings of lm files
    for f in convert.keys():
        shelltools.system("iconv -f %s -t UTF-8 langclass/LM/%s > %s/usr/share/libtextcat/%s" % (convert[f], f, get.installDIR(), clearlmname(f)))

    pisitools.dodoc("ChangeLog", "LICENSE", "README", "TODO")
