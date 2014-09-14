#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir = "kiki-extra"
datadir = "/usr/share/kiki/sound"

def install():
    pisitools.dodir(datadir)
    pisitools.insinto(datadir, "title_song.mp3")

