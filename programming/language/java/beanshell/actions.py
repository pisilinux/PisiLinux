#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

# You can use these as variables, they will replace GUI values before build.
# Package Name : beanshell
# Version : 2.04
# Summary : Small, free, embeddable, source level Java interpreter with object based scripting language features written in Java

# If the project that you are tying to compile is in a sub directory in the 
# source archive, than you can define working directory. For example; 
# WorkDir="beanshell-"+ get.srcVERSION() +"/sub_project_dir/"

#def setup():
#    autotools.configure()

#def build():
#    autotools.make()

def install():
    pisitools.insinto("/usr/share/java", "bsh-2.0b4.jar", "bsh.jar")

# Take a look at the source folder for these file as documentation.
#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")
# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("beanshell")
