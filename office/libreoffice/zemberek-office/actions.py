#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import glob

WorkDir="."

def install():
    zemberekdir = "/opt/LibreOffice/lib/libreoffice/share/extensions/zemberek-spell-checker"
    pisitools.dodir(zemberekdir)
    zemberekfile = glob.glob("*.oxt")[0]
    shelltools.system("unzip %s -d %s/%s" % (zemberekfile, get.installDIR(), zemberekdir))
