#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/old-licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s" % get.ARCH()

def setup():
        # Define bits variable for 32-bit and 64-bit architectures
    bits = "amd64" if get.ARCH() == "x86_64" else "i386"

    # Extract Debian package
    shelltools.system("ar -xv google-talkplugin_current_%s.deb" % bits)

    # Extract data.tar.gz, we use some exclude parameters here
    # because otherwise we get fchownat related sandbox errors
    shelltools.system("tar -xzvf data.tar.gz --exclude 'usr/lib/*' --exclude 'usr/lib'")
    
    shelltools.system("rm -rf opt/google/talkplugin/cron")
    
    # Extract changelog file
    shelltools.system("gzip -dfq usr/share/doc/google-talkplugin/changelog.Debian.gz")
    

def install():

    # Copying all needed stuff to /opt
    pisitools.insinto("/opt/google/talkplugin", "opt/google/talkplugin/*")

    # All doc files go to proper directory
    pisitools.domove("/opt/google/talkplugin/attributions.txt", "/usr/share/doc/google-talkplugin")
    pisitools.dodoc("usr/share/doc/google-talkplugin/changelog.Debian")

    # I don't sure whether only these two symlinks enough
    pisitools.dosym("/opt/google/talkplugin/libnpgoogletalk.so", "/usr/lib/browser-plugins/libnpgoogletalk.so")
    pisitools.dosym("/opt/google/talkplugin/libnpgtpo3dautoplugin.so", "/usr/lib/browser-plugins/libnpgtpo3dautoplugin.so")
