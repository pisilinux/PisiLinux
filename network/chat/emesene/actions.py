#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

# The tarball is created automatically from github servers.  Download it,
# upload to cekirdek.pardus.org.tr and get the folder name by extracting the
# tarball (It's actually the first seven characters of a git hash)
WorkDir = "emesene-%s" % (get.srcVERSION())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    # Use /usr/share instead of /usr/lib
    from distutils.dir_util import copy_tree
    copy_tree("%s/usr/lib/python2.7/site-packages/emesene" % get.installDIR(), "%s/usr/share/emesene" % get.installDIR())

    pisitools.removeDir("/usr/lib")



