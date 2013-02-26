#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

unifontfile_path="/usr/share/fonts/unifont/unifont-5.1.20080820.pcf"
pf2_fonts=["dejavu_10.pf2","dejavu_12.pf2","dejavu_14.pf2","dejavu_16.pf2","dejavu_bold_14.pf2"]

def setup():
    shelltools.export("GRUB_CONTRIB", "%s/grub-%s/grub-extras" % (get.workDIR(), get.srcVERSION()))
    CFLAGS = get.CFLAGS().replace(" -fstack-protector","").replace(" -fasynchronous-unwind-tables","").replace(" -O2", "")
    shelltools.export("CFLAGS", CFLAGS)
    shelltools.system("./autogen.sh")
    autotools.configure("--disable-werror \
                         --with-grubdir=grub2 \
                         --program-transform-name='s,grub,grub2,'\
                         --program-prefix= \
                         --htmldir='/usr/share/doc/${PF}/html' ")

def build():
    autotools.make()
    

def install():
    # Install unicode.pf2 using installed font source. 
    # Do not touch installation path, grub2 needs it exactly in /boot/grub2.
    cmd="./grub-mkfont -o unicode.pf2 %s" % unifontfile_path
    shelltools.system(cmd)
    pisitools.dodir("/boot/grub2")
    pisitools.insinto("/boot/grub2", "unicode.pf2")
    
    #Install dejavu.pf2 fonts to /usr/share/grub/fonts
    pisitools.dodir("/usr/share/grub/fonts")
    for i in pf2_fonts:
        pisitools.insinto("/usr/share/grub/fonts", i)
    
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #Remove default starfiled theme. Use Anka's brillant one :) 
    pisitools.removeDir("/usr/share/grub/themes/starfield")
    
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "BUGS", "ChangeLog", "COPYING", "TODO", "README")
    
