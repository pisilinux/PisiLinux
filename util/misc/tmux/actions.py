#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("PREFIX=/%s DESTDIR=%s" % (get.defaultprefixDIR(), get.installDIR()))

    # we love vim
    pisitools.insinto("/usr/share/vim/vimfiles/syntax/", "examples/tmux.vim", "tmux.vim")
    pisitools.insinto("/usr/share/doc/tmux/examples", "examples/*")
    pisitools.remove("/usr/share/doc/tmux/examples/tmux.vim")

    # Bash completion
    pisitools.domove("/usr/share/doc/tmux/examples/bash_completion_tmux.sh", "/etc/bash_completion.d", "tmux")

    pisitools.dodoc("CHANGES", "FAQ", "NOTES")
