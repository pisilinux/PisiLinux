#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "sabishape-%s" % get.srcVERSION().replace("2.2_20", "")

def install():
    for i in ["sabishape", "sabishaperc"]:
        pisitools.dosbin(i)

    for i in ["sabishape.8", "sabishaperc.5"]:
        pisitools.doman(i)

