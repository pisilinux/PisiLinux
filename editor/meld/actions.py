#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/Meld/work/ and:
# WorkDir="Meld-"+ get.srcVERSION() +"/sub_project_dir/"

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "INSTALL")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("Meld")

# You can use these as variables, they will replace GUI values before build.
# Package Name : Meld
# Version : 1.8.4
# Summary : Meld is a visual diff and merge tool.

# For more information, you can look at the Actions API
# from the Help menu and toolbar.

# By PiSiDo 2.0.0
