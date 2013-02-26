#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import rubymodules
from pisi.actionsapi import get

import os

def install():
    pisitools.dobin("bin/gem")
    pisitools.insinto("%s" %rubymodules.get_sitelibdir(), "lib/*")

    for file_name in  ["/rubygems/validator.rb", "/rubygems/custom_require.rb"]:
        shelltools.chmod("%s%s%s" % (get.installDIR(), rubymodules.get_sitelibdir(), file_name), 0644)
