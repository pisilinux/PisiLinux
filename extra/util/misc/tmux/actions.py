#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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

    pisitools.dodoc("CHANGES", "FAQ")
