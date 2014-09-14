#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("keychain", "/usr/ucb:", "")

def install():
    pisitools.dobin("keychain")
    pisitools.dodoc("ChangeLog", "keychain.pod", "README")
    pisitools.doman("keychain.1")
