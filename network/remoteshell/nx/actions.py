#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# This actions.py is written with information obtained from:
# http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/net-misc/nx/nx-3.4.0.ebuild?view=markup
# http://svn.mandriva.com/svn/packages/cooker/nx/pristine/SPECS/nx.spec

WorkDir = "."

def setup():

    # it is necessary to rerun autoreconf in each directory
    for dir in ("nxcomp", "nxcompext", "nxcompshad", "nxproxy"):
        shelltools.cd(dir)
        autotools.autoreconf("-fvi")
        shelltools.cd("..")

    # Add Pardus specific CC, CFLAGS and CXXFLAGS settings for nx-X11 compilation
    fileHandle = open ('nx-X11/config/cf/host.def', 'a' )
    fileHandle.write('#define CcCmd %s\n' % get.CC())
    fileHandle.write('#define OptimizedCDebugFlags %s GccAliasingArgs\n' % get.CFLAGS())
    fileHandle.write('#define OptimizedCplusplusDebugFlags %s GccAliasingArgs\n' % get.CXXFLAGS())
    fileHandle.close()

    # run configure in each directory seperately
    for dir in ("nxcomp", "nxcompshad",  "nxproxy", "nxcompext"):
        shelltools.cd(dir)
        autotools.configure()
        shelltools.cd("..")

def build():
    # run make in each directory seperately, except nxcompext
    for dir in ("nxcomp", "nxcompshad",  "nxproxy"):
        shelltools.cd(dir)
        autotools.make()
        shelltools.cd("..")

    # nx-x11 is more tricky, needs certain environment variables before compilation
    shelltools.cd("nx-X11")
    shelltools.export("WORLDOPTS", "")
    shelltools.export("FAST", "1")
    autotools.make("-j1 World")
    shelltools.cd("..")

    # build nxcompext
    shelltools.cd("nxcompext")
    autotools.make()
    shelltools.cd("..")


def install():

    # as we are using the libdir library suffix patch, we don't need a wrapper, we can install binaries into /usr/bin
    pisitools.dobin("nx-X11/programs/Xserver/nxagent")
    pisitools.dobin("nx-X11/programs/nxauth/nxauth")
    pisitools.dobin("nxproxy/nxproxy")

    # now install libraries and their symlinks
    pisitools.insinto("/usr/lib", "nx-X11/lib/X11/libX11-nx.so*")
    pisitools.insinto("/usr/lib", "nx-X11/lib/Xext/libXext-nx.so*")
    pisitools.insinto("/usr/lib", "nx-X11/lib/Xrender/libXrender-nx.so*")
    pisitools.insinto("/usr/lib", "nxcomp/libXcomp.so*")
    pisitools.insinto("/usr/lib", "nxcompext/libXcompext.so*")
    pisitools.insinto("/usr/lib", "nxcompshad/libXcompshad.so*")
