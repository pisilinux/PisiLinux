#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.dobin("bookman")
    pisitools.dobin("src2man")
    pisitools.dobin("txt2man")

    pisitools.doman("*.1")

    pisitools.dodoc("Changelog", "README")

