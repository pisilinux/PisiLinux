# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."
revnr = get.srcVERSION().split(".")[1]

def setup():
    # Unpack and prepare files
    for tar_file in shelltools.ls(get.workDIR()):
        if tar_file.endswith("xz"):
            shelltools.system("tar Jxfv %s" % tar_file)

def build():
    for folder in ["tlpkg", "doc", "source"]:
        shelltools.unlinkDir(folder)

def install():
    # prepare and install installed packs list
    pisitools.dodir("/var/lib/texmf/pisilinux/installedpacks")
    pisitools.dosed("CONTENTS", "^#", deleteLine=True)
    pisitools.insinto("/var/lib/texmf/pisilinux/installedpacks", "CONTENTS", "%s_%s.list" % (get.srcNAME(), revnr))

    for i in shelltools.ls("texmf-dist"):
        shelltools.copytree("texmf-dist/%s/" % i, "%s/usr/share/texmf-dist/" % get.installDIR())
    shelltools.system("find texmf-dist -type f -executable -exec chmod 755 %s/usr/share/{} \;" % get.installDIR())

    for i in shelltools.ls("."):
        if shelltools.isDirectory(i) and not i.startswith("texmf"):
            shelltools.copytree(i, "%s/usr/share/texmf-dist/" % get.installDIR())

    # clean config files
    pisitools.dosed("tex/generic/config", "DO NOT EDIT", deleteLine=True, filePattern="language\.d..$")
    pisitools.dosed("texmf-dist/web2c/updmap.cfg", "^(#!\s*)?(Map|MixedMap)", deleteLine=True)
    pisitools.dosed("%s/usr/share/texmf-dist/web2c/fmtutil.cnf" % get.installDIR(), "aleph", deleteLine=True)

    # install config files
    cfs = ["chktex/chktexrc",
           "web2c/mktex.cnf",
           "web2c/updmap.cfg",
           "web2c/fmtutil.cnf",
           "dvips/config/config.ps",
           "dvipdfmx/dvipdfmx.cfg",
           "tex/generic/config/language.dat",
           "tex/generic/config/language.def",
           "tex/generic/config/pdftexconfig.tex",
           "ttf2pk/ttf2pk.cfg",
           "xdvi/XDvi"]
    for cf in cfs:
        d = "/".join(cf.split("/")[:-1])
        p = cf if shelltools.isFile(cf) else "texmf-dist/%s" % cf
        pisitools.insinto("/etc/texmf/%s" % d, p)
    #pisitools.dosym("/etc/texmf/web2c/texmf.cnf", "/usr/share/texmf-dist/web2c/texmf.cnf")

    # fix sandbox violations
    #pisitools.dosed("texmf-dist/scripts/texlive/texlinks.sh", '"\$symlinkdir', r'"%s/$symlinkdir' % get.installDIR())

    # create symlinks
    pisitools.dodir("/usr/bin")
    #shelltools.system("texmf-dist/scripts/texlive/texlinks.sh -f %s/usr/share/texmf-dist/web2c/fmtutil.cnf %s/usr/bin" % ((get.installDIR(), ) * 2))

    # remove upstream updmap.cfg: it contains too many maps
    pisitools.remove("/usr/share/texmf-dist/web2c/updmap.cfg")

    # manpages already in texlive-bin
    pisitools.removeDir("/usr/share/texmf-dist/doc/man")

    # remove unneeded dir
    pisitools.removeDir("/usr/share/texmf-dist/scripts/context/stubs/mswin")

    # link programs from /usr/share/texmf-dist/scripts
    linked_scripts="""
a2ping/a2ping.pl
accfonts/mkt1font
accfonts/vpl2ovp
accfonts/vpl2vpl
adhocfilelist/adhocfilelist.sh
arara/arara.sh
bundledoc/arlatex
bundledoc/bundledoc
checkcites/checkcites.lua
chktex/chkweb.sh
chktex/deweb.pl
context/perl/mptopdf.pl
context/stubs/unix/context
context/stubs/unix/ctxtools
context/stubs/unix/luatools
context/stubs/unix/mtxrun
context/stubs/unix/pstopdf
context/stubs/unix/texexec
context/stubs/unix/texmfstart
ctanify/ctanify
ctanupload/ctanupload.pl
de-macro/de-macro
dosepsbin/dosepsbin.pl
dtxgen/dtxgen
dviasm/dviasm.py
epstopdf/epstopdf.pl
findhyph/findhyph
fontools/afm2afm
fontools/autoinst
fontools/ot2kpx
fragmaster/fragmaster.pl
installfont/installfont-tl
latex2man/latex2man
latexdiff/latexdiff-vc.pl
latexdiff/latexdiff.pl
latexdiff/latexrevise.pl
latexfileversion/latexfileversion
latexmk/latexmk.pl
latexpand/latexpand
ltxfileinfo/ltxfileinfo
lua2dox/lua2dox_filter
luaotfload/luaotfload-tool.lua
match_parens/match_parens
mf2pt1/mf2pt1.pl
mkjobtexmf/mkjobtexmf.pl
oberdiek/pdfatfi.pl
pdfcrop/pdfcrop.pl
pdfjam/pdf180
pdfjam/pdf270
pdfjam/pdf90
pdfjam/pdfbook
pdfjam/pdfflip
pdfjam/pdfjam
pdfjam/pdfjam-pocketmod
pdfjam/pdfjam-slides3up
pdfjam/pdfjam-slides6up
pdfjam/pdfjoin
pdfjam/pdfnup
pdfjam/pdfpun
pfarrei/a5toa4.tlu
pfarrei/pfarrei.tlu
pkfix-helper/pkfix-helper
pkfix/pkfix.pl
ps2eps/ps2eps.pl
purifyeps/purifyeps
simpdftex/simpdftex
sty2dtx/sty2dtx.pl
texcount/texcount.pl
texdef/texdef.pl
texdiff/texdiff
texdirflatten/texdirflatten
texdoc/texdoc.tlu
texdoctk/texdoctk.pl
texlive/allcm.sh
texlive/allneeded.sh
texlive/dvi2fax.sh
texlive/dvired.sh
texlive/e2pall.sh
texlive/fmtutil-sys.sh
texlive/fmtutil.sh
texlive/fontinst.sh
texlive/kpsetool.sh
texlive/kpsewhere.sh
texlive/ps2frag.sh
texlive/pslatex.sh
texlive/rungs.tlu
texlive/texconfig-dialog.sh
texlive/texconfig-sys.sh
texlive/texconfig.sh
texlive/texlinks.sh
texlive/updmap-sys.sh
texlive/updmap.pl
texliveonfly/texliveonfly.py
texloganalyser/texloganalyser
thumbpdf/thumbpdf.pl
typeoutfileinfo/typeoutfileinfo.sh
xindy/texindy.pl
xindy/xindy.pl
"""
    for p in linked_scripts.split():
        bn = shelltools.baseName(p).split(".")[0]
        if shelltools.isFile("%s/usr/share/texmf-dist/scripts/%s" % (get.installDIR(), p)):
            pisitools.dosym("/usr/share/texmf-dist/scripts/%s" % p, "/usr/bin/%s" % bn)
    pisitools.dosym("/usr/share/texmf-dist/scripts/listings-ext/listings-ext.sh", "/usr/bin/listings-ext.sh")
    pisitools.dosym("allcm", "/usr/bin/allec")
    pisitools.dosym("fmtutil", "/usr/bin/mktexfmt")
    pisitools.dosym("kpsetool", "/usr/bin/kpsexpand")
    pisitools.dosym("kpsetool", "/usr/bin/kpsepath")
    pisitools.dosym("epstopdf", "/usr/bin/repstopdf")
    pisitools.dosym("pdfcrop", "/usr/bin/rpdfcrop")
    pisitools.dosym("luaotfload-tool", "/usr/bin/mkluatexfontdb")
