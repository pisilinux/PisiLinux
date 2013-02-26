#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "emms-%s" % get.srcVERSION()

def build():
    autotools.make()
    shelltools.system("makeinfo --no-split emms.texinfo")

def install():
    pisitools.dobin("gst-wrapper")
    pisitools.insinto("/usr/share/emacs/site-lisp/emms/", "*.el")

    pisitools.doinfo("emms.info")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "NEWS", "FAQ")
