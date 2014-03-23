#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import glob

WorkDir="."

def install():
    zemberekdir = "/usr/lib/libreoffice/share/extensions/zemberek-spell-checker"
    pisitools.dodir(zemberekdir)
    zemberekfile = glob.glob("*.oxt")[0]
    shelltools.system("unzip %s -d %s/%s" % (zemberekfile, get.installDIR(), zemberekdir))
