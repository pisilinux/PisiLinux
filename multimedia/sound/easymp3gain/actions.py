 #!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pisitools.dosed('make.sh', '^(lazbuild)', r'\1 --cpu=%s --pcp=%s' % (get.ARCH().replace('i6', 'i3'), get.workDIR()))
    autotools.make('WIDGET=qt4')

def install():
    autotools.rawInstall('DESTDIR=%s WIDGET=qt4' % get.installDIR())
    pisitools.dodoc('AUTHORS', 'COPYING', '*.txt')
    
    pisitools.insinto("/usr/share/pixmaps/", "icons/easymp3gain-48.png", "easymp3gain.png")
