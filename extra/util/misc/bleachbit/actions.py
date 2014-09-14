#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    for lc in shelltools.ls("po/*.po"): pisitools.domo(lc, lc[3:-3], 'bleachbit.mo')
    shelltools.chmod('%s/usr/lib/python2.7/site-packages/bleachbit/CLI.py' % get.installDIR(), mode = 0755)
    pisitools.dosym('/usr/lib/python2.7/site-packages/bleachbit/CLI.py', '/usr/bin/bleachbit_cli')
    shelltools.chmod('%s/usr/lib/python2.7/site-packages/bleachbit/GUI.py' % get.installDIR(), mode = 0755)
    pisitools.dosym('/usr/lib/python2.7/site-packages/bleachbit/GUI.py', '/usr/bin/bleachbit')
    pisitools.insinto('/usr/share/applications/', 'bleachbit.desktop')
    pisitools.insinto('/usr/share/pixmaps/', 'bleachbit.png')
    pisitools.insinto('/usr/share/bleachbit/cleaners', 'cleaners/*.xml')
