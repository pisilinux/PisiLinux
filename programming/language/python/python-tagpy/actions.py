#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "tagpy-%s" % get.srcVERSION()
examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def setup():
    pythonmodules.run('configure.py \
                       --boost-python-libname=boost_python \
                       --taglib-inc-dir=/usr/include/taglib')

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.removeDir("/usr/lib/python2.7/site-packages/tagpy-2013*")
    pisitools.dodoc("LICENSE")

    shelltools.chmod("test/*", 0644)
    pisitools.insinto(examples, "test/*")

