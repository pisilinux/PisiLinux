#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DENABLE_GUILE=OFF")

    # we use only console edition and binary name should be the same with package (weechat-curses -> weechat)
    #pisitools.dosed("doc/weechat-curses.1", "weechat-curses", "weechat")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

   # pisitools.domove("/usr/bin/weechat-curses", "/usr/bin", "weechat")
   # pisitools.domove("/usr/share/man/man1/weechat-curses.1", "/usr/share/man/man1", "weechat.1")

    pisitools.dodoc("AUTHORS.asciidoc", "ChangeLog.asciidoc", "COPYING", "README.asciidoc")
