#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools


def install():
    pisitools.dobin("inxi")
    pisitools.doman("inxi.1.gz")
    pisitools.dodoc("inxi.changelog")