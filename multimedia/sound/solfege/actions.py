#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure('--disable-pygtk-test \
                         --disable-oss-sound \
                         --enable-docbook-stylesheet')

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc('README', 'FAQ', 'COPYING', 'ChangeLog', 'AUTHORS')
