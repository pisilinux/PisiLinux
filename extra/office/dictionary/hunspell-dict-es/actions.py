#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/hunspell", "es_ANY.dic", "es_ES.dic")
    pisitools.insinto("/usr/share/hunspell", "es_ANY.aff", "es_ES.aff")

    for lang in ("es_AR", "es_BO", "es_CL", "es_CO", "es_CR", "es_CU", "es_DO", "es_EC", "es_GT", "es_HN", "es_MX", "es_NI", "es_PA", "es_PE", "es_PR", "es_PY", "es_SV", "es_US", "es_UY", "es_VE"):
        pisitools.dosym("es_ES.dic", "/usr/share/hunspell/%s.dic" % lang)
        pisitools.dosym("es_ES.aff", "/usr/share/hunspell/%s.aff" % lang)

    pisitools.dodoc("*.txt")
