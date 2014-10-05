#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import texlivemodules

import os

WorkDir = "."

def setup():
    
    shelltools.makedirs("%s/source/build" % get.workDIR())
    shelltools.cd("%s/source/build" % get.workDIR())
    shelltools.sym("../configure", "configure")
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --datarootdir=/usr/share \
                         --datadir=/usr/share \
                         --mandir=/usr/share/man \
                         --disable-native-texlive-build \
                         --with-banner-add=/PisiLinux \
                         --disable-multiplatform \
                         --disable-dialog \
                         --disable-psutils \
                         --disable-t1utils \
                         --disable-bibtexu \
                         --disable-xz \
                         --disable-web2c \
                         --enable-shared \
                         --disable-static \
                         --with-system-zlib \
                         --with-system-zziplib \
                         --with-system-pnglib \
                         --with-system-ncurses \
                         --with-system-t1lib \
                         --with-system-gd \
                         --with-system-poppler \
                         --with-system-xpdf \
                         --with-system-freetype2 \
                         --with-system-pixman \
                         --with-system-cairo \
                         --with-system-harfbuzz \
                         --with-system-graphite \
                         --with-system-icu \
                         --with-freetype2-libdir=/usr/lib \
                         --with-freetype2-include=/usr/include/freetype2 \
                         --with-xdvi-x-toolkit=xaw \
                         --disable-dump-share \
                         --disable-aleph \
                         --enable-luatex \
                         --with-clisp-runtime=default \
                         --enable-xindy \
                         --disable-xindy-rules \
                         --disable-xindy-docs ")

def build():
  
    shelltools.cd("%s/source/build/" % get.workDIR())
    autotools.make()
 
def install():
        
    shelltools.cd("%s/source/build/" % get.workDIR())
    autotools.rawInstall("prefix=/usr DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/tlpkg/TeXLive")
    shelltools.move("%s/source/utils/biber/TeXLive/*.pm" % get.workDIR(), "%s/usr/share/tlpkg/TeXLive" % get.installDIR())
    
    
    # install texmf tree
    folders = ["/usr/share",
	       "/etc/texmf/chktex",
	       "/etc/texmf/tex/",
               "/etc/texmf/web2c",
               "/etc/texmf/dvips/config",
               "/etc/texmf/dvipdfm",
               "/etc/texmf/texconfig",
               "/etc/texmf/ttf2pk",
               "/etc/texmf/xdvi",
               "/etc/fonts/conf.avail",
               "/etc/texmf/dvipdfmx"]

    for dirs in folders:
        pisitools.dodir(dirs)

    # remove aleph from fmtutil.cnf
    pisitools.dosed("%s/usr/share/texmf-dist/web2c/fmtutil.cnf" % get.installDIR(), "^.*aleph.*$")
    
    pisitools.insinto("/etc/texmf/chktex", "%s/usr/share/texmf-dist/chktex/chktexrc" % get.installDIR(), sym=True) 
    #pisitools.insinto("/etc/texmf/web2c", "%s/usr/share/texmf-dist/web2c/texmf.cnf" % get.installDIR(), sym=True)
    pisitools.insinto("/etc/texmf/web2c", "%s/usr/share/texmf-dist/web2c/fmtutil.cnf" % get.installDIR(), sym=True)
    pisitools.insinto("/etc/texmf/texconfig", "%s/usr/share/texmf-dist/texconfig/tcfmgr.map" % get.installDIR(), sym=True)
    pisitools.insinto("/etc/texmf/dvipdfmx", "%s/usr/share/texmf-dist/dvipdfmx/dvipdfmx.cfg" % get.installDIR(), sym=True)
    pisitools.insinto("/etc/texmf/ttf2pk", "%s/usr/share/texmf-dist/ttf2pk/ttf2pk.cfg" % get.installDIR(), sym=True)
    pisitools.insinto("/etc/texmf/xdvi", "%s/usr/share/texmf-dist/xdvi/XDvi" % get.installDIR(), sym=True)

    # fix symlinks, some are incorrect
    # makefile patching is another way, but there ar/dvipdfmx.cfge lot of scripts
    # pathing each makefile makes it much harder, for now this is a "simpler" solution
    for binary in shelltools.ls(get.installDIR() + "/usr/bin"):
        real_path = shelltools.realPath(get.installDIR() + "/usr/bin/" + binary)
        if "texmf" in real_path and not os.path.exists(real_path): # modify only if it is broken
            base_path = real_path.replace(get.installDIR() + "/usr", "")
            new_path = "/usr/share" + base_path
            shelltools.unlink(get.installDIR() + "/usr/bin/" + binary)
            pisitools.dosym(new_path, "/usr/bin/" + binary)

    # create symlinks for formats
    # shelltools.export("PATH", get.installDIR() + "/usr/bin")
    #shelltools.system("PATH=\"$PATH:%s/usr/bin\" texlinks -f %s/usr/share/texmf-dist/web2c/fmtutil.cnf %s/usr/bin/" % (get.installDIR(), get.installDIR(), get.installDIR()))

    # remove files form disabled packages
    # we copy all man and info files into mandir. Disabling packages just remove binaries.
    # the remaining man and info files should be deleted manually
    
    pisitools.remove("/usr/share/texmf-dist/fonts/map/dvipdfmx/cid-x.map")
    pisitools.remove("/usr/share/texmf-dist/fonts/map/glyphlist/texglyphlist.txt")
    pisitools.remove("/usr/share/texmf-dist/scripts/chktex/chkweb.sh")
    pisitools.remove("/usr/share/texmf-dist/fonts/enc/dvips/base/7t.enc")
    pisitools.remove("/usr/share/texmf-dist/fonts/map/glyphlist/pdfglyphlist.txt")
    pisitools.remove("/usr/share/texmf-dist/scripts/chktex/deweb.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/ps2eps/ps2eps.pl")
    pisitools.remove("/usr/share/texmf-dist/fonts/cmap/dvipdfmx/EUC-UCS2")
    pisitools.remove("/usr/share/texmf-dist/chktex/chktexrc")
    pisitools.remove("/usr/share/texmf-dist/dvipdfmx/dvipdfmx.cfg")
    pisitools.remove("/usr/share/texmf-dist/fonts/map/glyphlist/glyphlist.txt")
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/lang/german/tex.xdy") 
    pisitools.remove("/usr/share/texmf-dist/web2c/mktexdir")
    pisitools.remove("/usr/share/texmf-dist/scripts/context/stubs/unix/texmfstart")
    pisitools.remove("/usr/share/texmf-dist/scripts/a2ping/a2ping.pl") 
    pisitools.remove("/usr/share/texmf-dist/scripts/pdfjam/pdf90")
    pisitools.remove("/usr/share/texmf-dist/fonts/sfd/ttf2pk/Big5.sfd") 
    pisitools.remove("/usr/share/texmf-dist/scripts/pkfix/pkfix.pl") 
    pisitools.remove("/usr/share/texmf-dist/dvips/gsftopk/render.ps") 
    pisitools.remove("/usr/share/texmf-dist/xdvi/pixmap/toolbar2.xpm") 
    pisitools.remove("/usr/share/texmf-dist/scripts/oberdiek/pdfatfi.pl") 
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
    pisitools.remove("/usr/share/texmf-dist/scripts/context/stubs/unix/pstopdf")
    pisitools.remove("/usr/share/texmf-dist/scripts/mkjobtexmf/mkjobtexmf.pl") 
    pisitools.remove("/usr/share/texmf-dist/dvips/base/special.pro") 
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/letter-order.xdy") 
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/numeric-sort.xdy") 
    pisitools.remove("/usr/share/texmf-dist/xindy/modules/base/tex.xdy") 
    pisitools.remove("/usr/share/texmf-dist/dvips/base/texc.pro") 
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/fmtutil-sys.sh") 
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
    pisitools.remove("/usr/share/texmf-dist/web2c/texmf.cnf")
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
    pisitools.remove("/usr/share/texmf-dist/scripts/context/stubs/unix/ctxtools")
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
    pisitools.remove("/usr/share/texmf-dist/scripts/texlive/updmap-sys.sh") 
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
    pisitools.remove("/usr/share/texmf-dist/scripts/lua2dox/lua2dox_filter")
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
