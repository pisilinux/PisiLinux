# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os
import re
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
		      "texliveonfly/texliveonfly.py",
		      "texloganalyser/texloganalyser",
		      "thumbpdf/thumbpdf.pl",
		      "typeoutfileinfo/typeoutfileinfo.sh",
		      "xindy/texindy.pl",
		      "xindy/xindy.pl"]
 
    for folder in linked_scripts:
        #pisitools.insinto("/usr/bin/", "/usr/share/texmf-dist/scripts/%s" % folder, sym = True)
        split = re.split('[/]',folder)
        pisitools.dosym("/usr/share/texmf-dist/scripts/%s" % folder,"/usr/bin/%s" % split[1])
    pisitools.dosym("/usr/share/texmf-dist/scripts/listings-ext/listings-ext.sh", "/usr/bin/listings-ext.sh")
    
    texlive_scripts=[ "allcm.sh",
		      "allneeded.sh",
		      "dvi2fax.sh",
		      "dvired.sh",
		      "fmtutil-sys.sh",
		      "fmtutil.sh",
		      "fontinst.sh",
		      "kpsetool.sh",
		      "kpsewhere.sh",
		      "ps2frag.sh",
		      "pslatex.sh",
		      "rungs.tlu",
		      "texconfig-dialog.sh",
		      "texconfig-sys.sh",
		      "texconfig.sh",
		      "texlinks.sh",
		      "updmap-sys.sh",
		      "updmap.pl"]
    
    for folder in texlive_scripts:
        pisitools.dosym("/usr/share/texmf-dist/scripts/texlive/%s" % folder, "/usr/bin/%s" % folder)
        
    pdfjam_scripts=[  "pdf180",
		      "pdf270",
		      "pdf90",
		      "pdfbook",
		      "pdfflip",
		      "pdfjam",
		      "pdfjam-pocketmod",
		      "pdfjam-slides3up",
		      "pdfjam-slides6up",
		      "pdfjoin",
		      "pdfnup",
		      "pdfpun"]
    
    for folder in pdfjam_scripts:
        pisitools.dosym("/usr/share/texmf-dist/scripts/pdfjam/%s" % folder, "/usr/bin/%s" % folder)
        
    context_scripts=[ "context",
		      "ctxtools",
		      "luatools",
		      "mtxrun",
		      "pstopdf",
		      "texexec",
		      "texmfstart"]
    for folder in context_scripts:
        pisitools.dosym("/usr/share/texmf-dist/scripts/context/stubs/unix/%s" % folder, "/usr/bin/%s" % folder)
    # old packages, we will not provide them
    
    pisitools.remove("/usr/share/texmf-dist/web2c/texmf.cnf")
    pisitools.remove("/usr/bin/lua2dox_filter")
    pisitools.remove("/usr/bin/pkfix-helper")
    pisitools.remove("/usr/bin/latexfileversion") 
    pisitools.remove("/usr/bin/texloganalyser") 
    pisitools.remove("/usr/bin/luatools") 
    pisitools.remove("/usr/bin/pdfnup") 
    pisitools.remove("/usr/bin/mtxrun") 
    pisitools.remove("/etc/texmf/dvipdfmx/dvipdfmx.cfg") 
    pisitools.remove("/usr/bin/vpl2vpl") 
    pisitools.remove("/usr/bin/pdfjam") 
    pisitools.remove("/usr/bin/arlatex") 
    pisitools.remove("/usr/bin/latex2man") 
    pisitools.remove("/usr/bin/pstopdf") 
    pisitools.remove("/usr/bin/ctxtools") 
    pisitools.remove("/usr/bin/pdfjam-pocketmod")
    pisitools.remove("/usr/bin/pdfjam-slides6up") 
    pisitools.remove("/usr/bin/installfont-tl") 
    pisitools.remove("/usr/bin/pdfbook") 
    pisitools.remove("/usr/bin/pdf180") 
    pisitools.remove("/usr/bin/ctanify") 
    pisitools.remove("/etc/texmf/xdvi/XDvi") 
    pisitools.remove("/usr/bin/bundledoc") 
    pisitools.remove("/usr/bin/listings-ext.sh") 
    pisitools.remove("/etc/texmf/web2c/fmtutil.cnf") 
    pisitools.remove("/etc/texmf/chktex/chktexrc") 
    pisitools.remove("/usr/bin/perl")
    pisitools.remove("/usr/bin/pdfpun") 
    pisitools.remove("/usr/bin/ot2kpx") 
    pisitools.remove("/etc/texmf/ttf2pk/ttf2pk.cfg") 
    pisitools.remove("/usr/bin/vpl2ovp") 
    pisitools.remove("/usr/bin/afm2afm") 
    pisitools.remove("/usr/bin/pdfjam-slides3up") 
    pisitools.remove("/usr/bin/simpdftex") 
    pisitools.remove("/usr/bin/texexec") 
    pisitools.remove("/usr/bin/ltxfileinfo") 
    pisitools.remove("/usr/bin/findhyph") 
    pisitools.remove("/usr/bin/texdirflatten") 
    pisitools.remove("/usr/bin/pdfjoin") 
    pisitools.remove("/usr/bin/texmfstart") 
    pisitools.remove("/usr/bin/match_parens") 
    pisitools.remove("/usr/bin/pdf270") 
    pisitools.remove("/usr/bin/texdiff") 
    pisitools.remove("/usr/bin/dtxgen") 
    pisitools.remove("/usr/bin/mkt1font") 
    pisitools.remove("/usr/bin/context") 
    pisitools.remove("/usr/bin/autoinst") 
    pisitools.remove("/usr/bin/pdfflip") 
    pisitools.remove("/usr/bin/pdf90") 
    pisitools.remove("/usr/bin/purifyeps") 
    pisitools.remove("/usr/bin/latexpand") 
    pisitools.remove("/usr/bin/de-macro")
