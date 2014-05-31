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

    pisitools.dosym("/usr/share/texmf-dist/scripts/authorindex/authorindex" ,"/usr/bin/authorindex")
    pisitools.dosym("/usr/share/texmf-dist/scripts/glossaries/makeglossaries" ,"/usr/bin/makeglossaries")
    pisitools.dosym("/usr/share/texmf-dist/scripts/pax/pdfannotextractor.pl" ,"/usr/bin/pdfannotextractor")
    pisitools.dosym("/usr/share/texmf-dist/scripts/ppower4/pdfthumb.tlu" ,"/usr/bin/pdfthumb")
    pisitools.dosym("/usr/share/texmf-dist/scripts/perltex/perltex.pl" ,"/usr/bin/perltex")
    pisitools.dosym("/usr/share/texmf-dist/scripts/pst-pdf/ps4pdf" ,"/usr/bin/ps4pdf")
    pisitools.dosym("/usr/share/texmf-dist/scripts/splitindex/perl/splitindex.pl" ,"/usr/bin/splitindex")
    pisitools.dosym("/usr/share/texmf-dist/scripts/svn-multi/svn-multi.pl" ,"/usr/bin/svn-multi")
    pisitools.dosym("/usr/share/texmf-dist/scripts/vpe/vpe.pl" ,"/usr/bin/vpe")

    pisitools.remove("/usr/share/texmf-dist/scripts/glossaries/makeglossaries.bat")
    pisitools.remove("/usr/share/texmf-dist/scripts/pst-pdf/ps4pdf.bat*")
    pisitools.remove("/usr/share/texmf-dist/scripts/shipunov/biokey2html.bat")
