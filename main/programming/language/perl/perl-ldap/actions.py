#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules

def setup():
    perlmodules.configure()

def build():
    perlmodules.make("PERL_MM_USE_DEFAULT=1")

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

