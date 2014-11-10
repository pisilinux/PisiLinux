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
    pisitools.remove("/usr/share/texmf-dist/doc/man/")
    pisitools.remove("/usr/share/texmf-dist/web2c/updmap.cfg")
    pisitools.removeDir("/usr/share/texmf-dist/scripts/context/stubs/mswin/")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/lang/german/tex.xdy")
    pisitools.remove("/usr/share/texmf-dist/web2c/mktexdir")
    pisitools.remove("/usr/share/texmf-dist/scripts/context/stubs/unix/texmfstart")
    pisitools.remove("/usr/share/texmf-dist/scripts/a2ping/a2ping.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/pdfjam/pdf90")
    pisitools.remove("/usr/share/texmf-dist/fonts/sfd/ttf2pk/Big5.sfd")
    pisitools.remove("/usr/share/texmf-dist/scripts/pkfix/pkfix.pl")
    pisitools.remove("/usr/share/texmf-dist/dvips/gsftopk/render.ps")
    pisitools.remove("/usr/share/texmf-dist/xdvi/pixmap/toolbar2.xpm")
    #pisitools.remove("/usr/share/texmf-dist/scripts/oberdiek/pdfatfi.pl")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/rules/isolatin1-exchange.xdy")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/ord/letorder.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/accfonts/mkt1font")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/word-order.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/texdirflatten/texdirflatten")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/dvi2fax.sh")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/rules/latin-exchange.xdy")
    pisitools.remove("/usr/share/texmf-dist/fonts/sfd/ttf2pk/UGB.sfd")
    pisitools.remove("/usr/share/texmf-dist/scripts/xindy/xindy.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/pdfjam/pdfjam-slides3up")
    pisitools.remove("/usr/share/texmf-dist/scripts/latexdiff/latexrevise.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/ctanify/ctanify")
    pisitools.remove("/usr/share/texmf-dist/fonts/sfd/ttf2pk/UBig5.sfd")
    pisitools.remove("/usr/share/texmf-dist/scripts/texdoctk/texdoctk.pl")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/lang/german/din5007.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/accfonts/vpl2ovp")
    pisitools.remove("/usr/share/texmf-dist/fonts/sfd/ttf2pk/Unicode.sfd")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/lang/latin/caseisrt.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/context/stubs/unix/mtxrun")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/fmtutil.sh")
    pisitools.remove("/usr/share/texmf-dist/scripts/fontools/ot2kpx")
    pisitools.remove("/usr/share/texmf-dist/bibtex/csf/base/88591lat.csf")
    pisitools.remove("/usr/share/texmf-dist/scripts/pdfjam/pdf180")
    pisitools.remove("/usr/share/texmf-dist/web2c/mktexdir.opt")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/ps2frag.sh")
    pisitools.remove("/usr/share/texmf-dist/fonts/sfd/ttf2pk/SJIS.sfd")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/texconfig-sys.sh")
    pisitools.remove("/usr/share/texmf-dist/scripts/pdfcrop/pdfcrop.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/fontinst.sh")
    pisitools.remove("/usr/share/texmf-dist/scripts/context/perl/mptopdf.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/match_parens/match_parens")
    pisitools.remove("/usr/share/texmf-dist/fonts/sfd/ttf2pk/UKS.sfd")
    pisitools.remove("/usr/share/texmf-dist/texconfig/tcfmgr.map")
    pisitools.remove("/usr/share/texmf-dist/scripts/fontools/autoinst")
    pisitools.remove("/usr/share/texmf-dist/dvips/base/texps.pro")
    pisitools.remove("/usr/share/texmf-dist/xdvi/XDvi")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/texconfig-dialog.sh")
    pisitools.remove("/usr/share/texmf-dist/scripts/xindy/texindy.pl")
    #pisitools.remove("/usr/share/texmf-dist/scripts/context/stubs/unix/pstopdf")
    pisitools.remove("/usr/share/texmf-dist/scripts/mkjobtexmf/mkjobtexmf.pl")
    pisitools.remove("/usr/share/texmf-dist/dvips/base/special.pro")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/letter-order.xdy")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/numeric-sort.xdy")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/tex.xdy")
    pisitools.remove("/usr/share/texmf-dist/dvips/base/texc.pro")
    #pisitools.remove("/usr/share/texmf-dist/scripts/texlive/fmtutil-sys.sh")
    pisitools.remove("/usr/share/texmf-dist/scripts/pdfjam/pdfflip")
    pisitools.remove("/usr/share/texmf-dist/scripts/checkcites/checkcites.lua")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/kpsewhere.sh")
    pisitools.remove("/usr/share/texmf-dist/scripts/context/stubs/unix/luatools")
    pisitools.remove("/usr/share/texmf-dist/scripts/texdiff/texdiff")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/ff-ranges.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/sty2dtx/sty2dtx.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/pfarrei/pfarrei.tlu")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/tlmgr.pl")
    pisitools.remove("/usr/share/texmf-dist/fonts/sfd/ttf2pk/KS-HLaTeX.sfd")
    pisitools.remove("/usr/share/texmf-dist/fonts/sfd/ttf2pk/EUC.sfd")
    pisitools.remove("/usr/share/texmf-dist/fonts/sfd/ttf2pk/UGBK.sfd")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/e2pall.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/dtxgen/dtxgen")
    pisitools.remove("/usr/share/texmf-dist/scripts/texdoc/texdoc.tlu")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/lang/german/duden.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/luaotfload/luaotfload-tool.lua")
    pisitools.remove("/usr/share/texmf-dist/scripts/pfarrei/a5toa4.tlu")
    pisitools.remove("/usr/share/texmf-dist/scripts/dosepsbin/dosepsbin.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/pdfjam/pdfnup")
    pisitools.remove("/usr/share/texmf-dist/texconfig/tcfmgr")
    pisitools.remove("/usr/share/texmf-dist/scripts/latexdiff/latexdiff.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/fragmaster/fragmaster.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/findhyph/findhyph")
    pisitools.remove("/usr/share/texmf-dist/scripts/listings-ext/listings-ext.sh")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/rules/latin-tolower.xdy")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/german-sty.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/latexpand/latexpand")
    pisitools.remove("/usr/share/texmf-dist/scripts/simpdftex/simpdftex")
    pisitools.remove("/usr/share/texmf-dist/web2c/texmfcnf.lua")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/kpsetool.sh")
    pisitools.remove("/usr/share/texmf-dist/web2c/fmtutil.cnf")
    pisitools.remove("/usr/share/texmf-dist/scripts/thumbpdf/thumbpdf.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/context/stubs/unix/texexec")
    pisitools.remove("/usr/share/texmf-dist/dvips/base/hps.pro")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/ignore-punctuation.xdy")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/latex.xdy")
    pisitools.remove("/usr/share/texmf-dist/web2c/mktex.opt")
    pisitools.remove("/usr/share/texmf-dist/bibtex/csf/base/cp850sca.csf")
    pisitools.remove("/usr/share/texmf-dist/fonts/enc/ttf2pk/base/T1-WGL4.enc")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/ignore-hyphen.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/pdfjam/pdfjoin")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/keep-blanks.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/texloganalyser/texloganalyser")
    pisitools.remove("/usr/share/texmf-dist/scripts/bundledoc/bundledoc")
    #pisitools.remove("/usr/share/texmf-dist/scripts/context/stubs/unix/ctxtools")
    pisitools.remove("/usr/share/texmf-dist/scripts/ltxfileinfo/ltxfileinfo")
    pisitools.remove("/usr/share/texmf-dist/web2c/mktexupd")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/class/pagenums.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/allneeded.sh")
    pisitools.remove("/usr/share/texmf-dist/dvips/base/finclude.pro")
    pisitools.remove("/usr/share/texmf-dist/web2c/mktexnam")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/book-order.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/installfont/installfont-tl")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/texlinks.sh")
    pisitools.remove("/usr/share/texmf-dist/scripts/dviasm/dviasm.py")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/texconfig.sh")
    pisitools.remove("/usr/share/texmf-dist/scripts/epstopdf/epstopdf.pl")
    pisitools.remove("/usr/share/texmf-dist/fonts/sfd/ttf2pk/UJIS.sfd")
    pisitools.remove("/usr/share/texmf-dist/scripts/purifyeps/purifyeps")
    pisitools.remove("/usr/share/texmf-dist/bibtex/csf/base/cp866rus.csf")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/styles/basic.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/latexdiff/latexdiff-vc.pl")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/page-ranges.xdy")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/rules/isolatin1-tolower.xdy")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/latex-loc-fmts.xdy")
    pisitools.remove("/usr/share/texmf-dist/ttf2pk/VPS.rpl")
    pisitools.remove("/usr/share/texmf-dist/scripts/typeoutfileinfo/typeoutfileinfo.sh")
    pisitools.remove("/usr/share/texmf-dist/bibtex/csf/base/88591sca.csf")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/updmap.pl")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/texindy.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/pdfjam/pdfjam-slides6up")
    pisitools.remove("/usr/share/texmf-dist/fonts/sfd/ttf2pk/UKS-HLaTeX.sfd")
    pisitools.remove("/usr/share/texmf-dist/scripts/de-macro/de-macro")
    #pisitools.remove("/usr/share/texmf-dist/scripts/texlive/updmap-sys.sh")
    pisitools.remove("/usr/share/texmf-dist/scripts/pdfjam/pdfbook")
    pisitools.remove("/usr/share/texmf-dist/bibtex/csf/base/cp437lat.csf")
    pisitools.remove("/usr/share/texmf-dist/scripts/latexmk/latexmk.pl")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/lang/latin/letgroup.xdy")
    pisitools.remove("/usr/share/texmf-dist/fonts/sfd/ttf2pk/UBg5plus.sfd")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/makeindex.xdy")
    pisitools.remove("/usr/share/texmf-dist/bibtex/csf/base/csfile.txt")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/rungs.tlu")
    pisitools.remove("/usr/share/texmf-dist/scripts/bundledoc/arlatex")
    pisitools.remove("/usr/share/texmf-dist/scripts/adhocfilelist/adhocfilelist.sh")
    pisitools.remove("/usr/share/texmf-dist/dvips/base/color.pro")
    pisitools.remove("/usr/share/texmf-dist/scripts/latexfileversion/latexfileversion")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/pslatex.sh")
    pisitools.remove("/usr/share/texmf-dist/xdvi/pixmap/toolbar.xpm")
    #pisitools.remove("/usr/share/texmf-dist/scripts/lua2dox/lua2dox")
    pisitools.remove("/usr/share/texmf-dist/scripts/accfonts/vpl2vpl")
    pisitools.remove("/usr/share/texmf-dist/scripts/fontools/afm2afm")
    pisitools.remove("/usr/share/texmf-dist/scripts/context/stubs/unix/context")
    pisitools.remove("/usr/share/texmf-dist/dvips/base/crop.pro")
    pisitools.remove("/usr/share/texmf-dist/scripts/texcount/texcount.pl")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/styles/makeidx.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/pdfjam/pdfjam")
    pisitools.remove("/usr/share/texmf-dist/scripts/pkfix-helper/pkfix-helper")
    pisitools.remove("/usr/share/texmf-dist/scripts/texliveonfly/texliveonfly.py")
    pisitools.remove("/usr/share/texmf-dist/bibtex/csf/base/cp850lat.csf")
    pisitools.remove("/usr/share/texmf-dist/web2c/mktexnam.opt")
    pisitools.remove("/usr/share/texmf-dist/xindy/VERSION")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/allcm.sh")
    pisitools.remove("/usr/share/texmf-dist/scripts/texdef/texdef.pl")
    pisitools.remove("/usr/share/texmf-dist/bibtex/csf/base/ascii.csf")
    pisitools.remove("/usr/share/texmf-dist/scripts/pdfjam/pdfpun")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/ff-ranges-only.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/latex2man/latex2man")
    pisitools.remove("/usr/share/texmf-dist/fonts/sfd/ttf2pk/HKSCS.sfd")
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/dvired.sh")
    pisitools.remove("/usr/share/texmf-dist/scripts/mf2pt1/mf2pt1.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/ctanupload/ctanupload.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/pdfjam/pdfjam-pocketmod")
    pisitools.remove("/usr/share/texmf-dist/dvips/base/tex.pro")
    pisitools.remove("/usr/share/texmf-dist/scripts/pdfjam/pdf270")
    pisitools.remove("/usr/share/texmf-dist/ttf2pk/ttf2pk.cfg")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/latin-lettergroups.xdy")
    pisitools.remove("/usr/share/texmf-dist/scripts/arara/arara.sh")
    # remove conflicts with texlive-bin
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/b5ka12.cfg") 
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/b5kr12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/b5so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/c1so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/c2so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/c3so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/c4so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/c5so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/c6so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/c7so12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/csso12.cfg") 
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/gsfs14.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/j2so12.cfg") 
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/jsso12.cfg")
    pisitools.remove("/usr/share/texmf-dist/hbf2gf/ksso17.cfg") 
    pisitools.remove("/usr/share/texmf-dist/scripts/context/stubs/unix/contextjit") 
    pisitools.remove("/usr/share/texmf-dist/scripts/context/stubs/unix/mtxrunjit")
    pisitools.remove("/usr/share/texmf-dist/scripts/latex-git-log/latex-git-log")
    pisitools.remove("/usr/share/texmf-dist/scripts/latexindent/latexindent.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/ltximg/ltximg.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/pythontex/depythontex.py")
    pisitools.remove("/usr/share/texmf-dist/scripts/pythontex/pythontex.py")
    pisitools.remove("/usr/share/texmf-dist/scripts/texfot/texfot.pl")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/lang/korean/utf8-lang.xdy")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/lang/korean/utf8.xdy")
    
    