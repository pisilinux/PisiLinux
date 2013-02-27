#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().partition("_")[0])

def setup():
    cmaketools.configure('-DCMAKE_SKIP_RPATH:BOOL=YES')

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
