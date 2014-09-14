#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def install():
  #  pisitools.dosed("cherrypy/test/test.py", "raw_input", "")
  #  pisitools.dosed("cherrypy/test/test.py", "'test_cache_filter',", "")

    pythonmodules.install()

    pisitools.dodoc("README.txt")
