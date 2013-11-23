#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
#from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/fife/work/ and:
#WorkDir="fife-"+ get.srcVERSION() 

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()


# Take a look at the source folder for these file as documentation.
#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("fife")

# You can use these as variables, they will replace GUI values before build.
# Package Name : fife
# Version : 0.3.5
# Summary : Flexible Isometric Free Engine is a cross platform game creation framework

# For more information, you can look at the Actions API
# from the Help menu and toolbar.

# By PiSiDo 2.0.0
