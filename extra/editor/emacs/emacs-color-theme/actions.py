#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "color-theme-%s" % get.srcVERSION()

def install():
    for data in ['*.el', 'themes']:
        pisitools.insinto('/usr/share/emacs/site-lisp/color-theme/', data)

    pisitools.dodoc('README', 'COPYING', 'BUGS', 'AUTHORS', 'ChangeLog')
