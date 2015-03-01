#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

def build():
    shelltools.cd("tools/perf")
    autotools.make("JOBS=5 WERROR=0 perf HAVE_CPLUS_DEMANGLE=1")

def install():
    shelltools.cd("tools/perf")
    # Build and install the new 'perf' tool
    #pisitools.insinto("/usr/bin", "tools/perf/perf", "perf.%s-%s" % (get.srcNAME(), get.srcVERSION()))
    autotools.install("JOBS=5 WERROR=0 perf HAVE_CPLUS_DEMANGLE=1")
    
    pisitools.domove("/usr/etc/bash_completion.d/perf", "/etc/bash_completion.d")
    pisitools.removeDir("/usr/etc")
    
    #pisitools.domove("/usr/lib64/libperf-gtk.so", "/usr/lib64/")
    #pisitools.removeDir("/usr/lib64")