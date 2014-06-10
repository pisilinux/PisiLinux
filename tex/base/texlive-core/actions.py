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
    for tar_file in shelltools.ls(get.workDIR()):
        if tar_file.endswith("xz"):
            shelltools.system("tar Jxfv %s" % tar_file)
#    for folder in ["tlpkg", "doc", "source", "omega"]:
def build():
    for folder in ["tlpkg", "doc", "source"]:
        shelltools.unlinkDir("%s/%s" %(get.workDIR() , folder))

def install():
    pisitools.dodir("/usr/share")

    wanteddirs = []
    for file_ in shelltools.ls(get.workDIR()):
        if shelltools.isDirectory(file_) and not "texmf" in file_:
            wanteddirs.append(file_)
    #for folder in wanteddirs:
    
    pisitools.insinto("/usr/share/", "%s/texmf-dist" % get.workDIR())
    
 
 # copy config file to texmf-config
    pisitools.dodir("/etc/texmf/chktex")
    pisitools.dodir("/etc/texmf/web2c")
    pisitools.dodir("/etc/texmf/dvips/config")
    pisitools.dodir("/etc/texmf/dvipdfmx")
    pisitools.dodir("/etc/texmf/tex/generic/config")
    pisitools.dodir("/etc/texmf/ttf2pk")
    pisitools.dodir("/etc/texmf/xdvi")
    shelltools.copy("%s/usr/share/texmf-dist/chktex/chktexrc" % get.installDIR(), \
                    "%s/etc/texmf/chktex" % get.installDIR())
    shelltools.copy("%s/usr/share/texmf-dist/web2c/mktex.cnf" % get.installDIR(), \
                    "%s/etc/texmf/web2c" % get.installDIR())
    shelltools.copy("%s/usr/share/texmf-dist/web2c/mktex.cnf" % get.installDIR(), \
                    "%s/etc/texmf/web2c" % get.installDIR())
    shelltools.copy("%s/usr/share/texmf-dist/web2c/updmap.cfg" % get.installDIR(), \
                    "%s/etc/texmf/web2c" % get.installDIR())
    shelltools.copy("%s/usr/share/texmf-dist/web2c/fmtutil.cnf" % get.installDIR(), \
                    "%s/etc/texmf/web2c" % get.installDIR())
    shelltools.copy("%s/usr/share/texmf-dist/dvips/config/config.ps" % get.installDIR(), \
                    "%s/etc/texmf/dvips/config" % get.installDIR())
    shelltools.copy("%s/usr/share/texmf-dist/dvipdfmx/dvipdfmx.cfg" % get.installDIR(), \
                    "%s/etc/texmf/dvipdfmx" % get.installDIR())
    shelltools.copy("%s/usr/share/texmf-dist/tex/generic/config/pdftexconfig.tex" % get.installDIR(), \
                    "%s/etc/texmf/tex/generic/config" % get.installDIR())
    shelltools.copy("%s/usr/share/texmf-dist/tex/generic/config/pdftex-dvi.tex" % get.installDIR(), \
                    "%s/etc/texmf/tex/generic/config" % get.installDIR())
    shelltools.copy("%s/usr/share/texmf-dist/tex/generic/config/luatexiniconfig.tex" % get.installDIR(), \
                    "%s/etc/texmf/tex/generic/config" % get.installDIR())
    shelltools.copy("%s/usr/share/texmf-dist/ttf2pk/ttf2pk.cfg" % get.installDIR(), \
                    "%s/etc/texmf/ttf2pk" % get.installDIR())
    shelltools.copy("%s/usr/share/texmf-dist/xdvi/XDvi" % get.installDIR(), \
                    "%s/etc/texmf/xdvi" % get.installDIR())
    pisitools.remove("/usr/share/texmf-dist/web2c/updmap.cfg")
    pisitools.remove("/usr/share/texmf-dist/scripts/context/stubs/mswin")
    
    if shelltools.can_access_directory("texmf-dist"):
        # Recursively copy on directory on top of another, overwrite duplicate files too
        copy_tree("texmf-dist", "%s/usr/share/texmf-dist" % get.installDIR())

# copy config file to texmf-config
    #pisitools.dodir("/usr/bin")
    pisitools.dosym("/usr/share/texmf-dist/scripts/texlive/texlinks.sh", "/usr/bin/texlinks.sh")
    #shelltools.cd("%s/usr/bin" % get.installDIR())
    #shelltools.system("./texlinks.sh -f %s/usr/share/texmf-dist/web2c/fmtutil.cnf %s/usr/bin/"  % (get.installDIR(), get.installDIR()))

    ## chmod of script files
    script_dir = get.installDIR() + "/usr/share/texmf-dist/scripts"
    if shelltools.can_access_directory(script_dir):
        for root, dirs, files in os.walk(script_dir):
            for name in files:
                shelltools.chmod(os.path.join(root, name), 0755)
 
    
    pisitools.dosym("/usr/share/texmf-dist/scripts/listings-ext/listings-ext.sh", "/usr/bin/listings-ext.sh")
  
    # old packages, we will not provide them
    
    pisitools.remove("/usr/share/texmf-dist/web2c/texmf.cnf")
    #pisitools.remove("/usr/share/texmf-dist/tex/plain/config/aleph.ini")
    #pisitools.removeDir("/usr/share/texmf-dist/scripts/context/stubs/mswin/")
