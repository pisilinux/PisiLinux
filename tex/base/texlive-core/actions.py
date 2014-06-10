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

    
    ## chmod of script files
    script_dir = get.installDIR() + "/usr/share/texmf-dist/scripts"
    if shelltools.can_access_directory(script_dir):
        for root, dirs, files in os.walk(script_dir):
            for name in files:
                shelltools.chmod(os.path.join(root, name), 0755)

    
    linked_scripts=[  "a2ping/a2ping.pl",
		      "accfonts/mkt1font",
		      "accfonts/vpl2ovp",
		      "accfonts/vpl2vpl",
		      "adhocfilelist/adhocfilelist.sh",
		      "arara/arara.sh",
		      "bundledoc/arlatex",
		      "bundledoc/bundledoc",
		      "checkcites/checkcites.lua",
		      "chktex/chkweb.sh",
		      "chktex/deweb.pl",
		      "context/perl/mptopdf.pl",
		      "context/stubs/unix/context",
		      "context/stubs/unix/ctxtools",
		      "context/stubs/unix/luatools",
		      "context/stubs/unix/mtxrun",
		      "context/stubs/unix/pstopdf",
		      "context/stubs/unix/texexec",
		      "context/stubs/unix/texmfstart",
		      "ctanify/ctanify",
		      "ctanupload/ctanupload.pl",
		      "de-macro/de-macro",
		      "dosepsbin/dosepsbin.pl",
		      "dtxgen/dtxgen",
		      "dviasm/dviasm.py",
		      "epstopdf/epstopdf.pl",
		      "findhyph/findhyph",
		      "fontools/afm2afm",
		      "fontools/autoinst",
		      "fontools/ot2kpx",
		      "fragmaster/fragmaster.pl",
		      "installfont/installfont-tl",
		      "latex2man/latex2man",
		      "latexdiff/latexdiff-vc.pl",
		      "latexdiff/latexdiff.pl",
		      "latexdiff/latexrevise.pl",
		      "latexfileversion/latexfileversion",
		      "latexmk/latexmk.pl",
		      "latexpand/latexpand",
		      "ltxfileinfo/ltxfileinfo",
		      "lua2dox/lua2dox_filter",
		      "luaotfload/luaotfload-tool.lua",
		      "match_parens/match_parens",
		      "mf2pt1/mf2pt1.pl",
		      "mkjobtexmf/mkjobtexmf.pl",
		      "pdfcrop/pdfcrop.pl",
		      "pdfjam/pdf180",
		      "pdfjam/pdf270",
		      "pdfjam/pdf90",
		      "pdfjam/pdfbook",
		      "pdfjam/pdfflip",
		      "pdfjam/pdfjam",
		      "pdfjam/pdfjam-pocketmod",
		      "pdfjam/pdfjam-slides3up",
		      "pdfjam/pdfjam-slides6up",
		      "pdfjam/pdfjoin",
		      "pdfjam/pdfnup",
		      "pdfjam/pdfpun",
		      "pfarrei/a5toa4.tlu",
		      "pfarrei/pfarrei.tlu",
		      "pkfix-helper/pkfix-helper",
		      "pkfix/pkfix.pl",
		      "ps2eps/ps2eps.pl",
		      "purifyeps/purifyeps",
		      "simpdftex/simpdftex",
		      "sty2dtx/sty2dtx.pl",
		      "texcount/texcount.pl",
		      "texdef/texdef.pl",
		      "texdiff/texdiff",
		      "texdirflatten/texdirflatten",
		      "texdoc/texdoc.tlu",
		      "texdoctk/texdoctk.pl",
		      "texlive/allcm.sh",
		      "texlive/allneeded.sh",
		      "texlive/dvi2fax.sh",
		      "texlive/dvired.sh",
		      "texlive/fmtutil-sys.sh",
		      "texlive/fmtutil.sh",
		      "texlive/fontinst.sh",
		      "texlive/kpsetool.sh",
		      "texlive/kpsewhere.sh",
		      "texlive/ps2frag.sh",
		      "texlive/pslatex.sh",
		      "texlive/rungs.tlu",
		      "texlive/texconfig-dialog.sh",
		      "texlive/texconfig-sys.sh",
		      "texlive/texconfig.sh",
		      "texlive/texlinks.sh",
		      "texlive/updmap-sys.sh",
		      "texlive/updmap.pl",
		      "texliveonfly/texliveonfly.py",
		      "texloganalyser/texloganalyser",
		      "thumbpdf/thumbpdf.pl",
		      "typeoutfileinfo/typeoutfileinfo.sh",
		      "xindy/texindy.pl",
		      "xindy/xindy.pl"]
 
    for folder in linked_scripts:
        pisitools.insinto("/usr/bin/", "/usr/share/texmf-dist/scripts/%s" % folder, sym = True)
    pisitools.dosym("/usr/share/texmf-dist/scripts/listings-ext/listings-ext.sh", "/usr/bin/listings-ext.sh")
  
    
    # old packages, we will not provide them
    
    pisitools.remove("/usr/share/texmf-dist/web2c/texmf.cnf")