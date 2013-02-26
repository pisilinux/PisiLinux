#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "color-theme-%s" % get.srcVERSION()

def install():
    for data in ['*.el', 'themes']:
        pisitools.insinto('/usr/share/emacs/site-lisp/color-theme/', data)

    pisitools.dodoc('README', 'COPYING', 'BUGS', 'AUTHORS', 'ChangeLog')
