#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dobin("urlview")
    pisitools.dobin("url_handler.sh")

    pisitools.dosed("sample.urlview", "url_handler.sh", "/usr/bin/url_handler.sh")

    pisitools.insinto("/etc/urlview/", "sample.urlview", "system.urlview")

    pisitools.newman("urlview.man", "urlview.1")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
