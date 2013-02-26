#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    scons.make("prefix='/usr'")

def install():
    scons.install("prefix='/usr' destdir='%s' install" % get.installDIR())

    pisitools.removeDir("/usr/man")
    pisitools.doman("ffmpeg2theora.1")

    pisitools.dodoc("AUTHORS", "COPYING", "TODO", "ChangeLog", "README", "subtitles.txt")
