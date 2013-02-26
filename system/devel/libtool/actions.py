#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# WorkDir = "libtool-2.2.6b"
configTemplateDir = "/usr/share/libtool/config"

# FIXME: do we still need this ?
pathFixList = {"libpath1": ["sys_lib_search_path_spec=.*", "sys_lib_search_path_spec=\"/lib /usr/lib /usr/local/lib\""], \
               "libpath2": ["sys_lib_dlsearch_path_spec=.*", "sys_lib_dlsearch_path_spec=\"/lib /usr/lib /usr/local/lib\""], \
               "gccpath1": ["predep_objects=.*", "predep_objects=\"\""], \
               "gccpath2": ["postdep_objects=.*", "postdep_objects=\"\""], \
               "gccpath3": ["compiler_lib_search_path=.*", "compiler_lib_search_path=\"\""]}

def setup():
    # Fix all linkage problems :(((
    # pisi now exports GCC and CXX correctly, so the libtool shall obey it too
    # if you want to use plain gcc or g++ you must modify your packages build system
    # due to it
    # shelltools.export("CC", "gcc")
    # shelltools.export("C", "g++")
    # shelltools.export("F77", "gfortran")

    cflags = "%s -fPIC" % get.CFLAGS()
    options = "--enable-static=no"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        cflags += " -m32"

    shelltools.export("CFLAGS", cflags)
    autotools.configure(options)

def build():
    autotools.make()

# fails in some tests, requires binutils > 2.19.51 which has relaxed as-needed behaviour
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for f in ["config.sub", "config.guess"]:
        pisitools.remove("%s/%s" % (configTemplateDir, f))
        pisitools.dosym("/usr/share/gnuconfig/%s" % f, "%s/%s" % (configTemplateDir, f))

    # Fix default lib paths and don't let gcc paths sneak in
    for i in pathFixList.keys():
        pisitools.dosed("%s/usr/bin/libtool" % get.installDIR(), pathFixList[i][0], pathFixList[i][1])

    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "NEWS", "README", "THANKS", "doc/PLATFORMS")

