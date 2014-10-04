# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os
from distutils.dir_util import copy_tree

WorkDir = "." 

def setup():
    # Unpack and prepare files
    for tar_file in shelltools.ls('.'):
        if tar_file.endswith("xz"):
            shelltools.system("tar Jxfv %s" % tar_file)

def build():
    for folder in ["tlpkg"]:
        shelltools.unlinkDir(folder)

def install():
    pisitools.dodir("/usr/share")

    wanteddirs = []
    for file_ in shelltools.ls('.'):
        if shelltools.isDirectory(file_) and not "texmf" in file_:
            wanteddirs.append(file_)

    for folder in wanteddirs:
        pisitools.insinto("/usr/share/texmf-dist", folder)

    if shelltools.can_access_directory("texmf-dist"):
        # Recursively copy on directory on top of another, overwrite duplicate files too
        copy_tree("texmf-dist", "%s/usr/share/texmf-dist" % get.installDIR())

    ## chmod of script files
    script_dir = get.installDIR() + "/usr/share/texmf-dist/scripts"
    if shelltools.can_access_directory(script_dir):
        for root, dirs, files in os.walk(script_dir):
            for name in files:
                shelltools.chmod(os.path.join(root, name), 0755)
 
    pisitools.remove("/usr/share/texmf-dist/scripts/ptex2pdf/ptex2pdf.lua")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/ksso17.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/j2so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/scripts/convbkmk/convbkmk.rb")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/c1so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/b5ka12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/c4so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/scripts/jfontmaps/kanji-config-updmap.pl")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/b5so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/csso12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/c7so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/jsso12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/c3so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/c6so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/b5kr12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/c5so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/c2so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/scripts/jfontmaps/kanji-config-updmap-sys.sh")
    pisitools.remove("/usr/share/texmf-dist/scripts/jfontmaps/kanji-fontmap-creator.pl")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/gsfs14.cfg")
