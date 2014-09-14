#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="."

def install():

    pisitools.insinto("/usr/share/fonts/stix","STIX-MathJax/otf/*.otf")

    pisitools.dosym("../conf.avail/stix-fonts-fontconfig.conf", "/etc/fonts/conf.d/stix-fonts-fontconfig.conf")
    pisitools.dosym("../conf.avail/stix-fonts-integrals-fontconfig.conf", "/etc/fonts/conf.d/stix-fonts-integrals-fontconfig.conf")
    pisitools.dosym("../conf.avail/stix-fonts-pua-fontconfig.conf", "/etc/fonts/conf.d/stix-fonts-pua-fontconfig.conf")
    pisitools.dosym("../conf.avail/stix-fonts-sizes-fontconfig.conf", "/etc/fonts/conf.d/stix-fonts-sizes-fontconfig.conf")
    pisitools.dosym("../conf.avail/stix-fonts-variants-fontconfig.conf", "/etc/fonts/conf.d/stix-fonts-variants-fontconfig.conf")
    
    pisitools.dodoc("*.pdf","License/*.pdf")
