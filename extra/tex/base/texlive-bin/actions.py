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

    #install biber
    pisitools.dobin("../../biber")

    #pisitools.dodir("/usr/share/tlpkg/TeXLive")
    #shelltools.move("%s/source/utils/biber/TeXLive/*.pm" % get.workDIR(), "%s/usr/share/tlpkg/TeXLive" % get.installDIR())


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

     
    bibtexextra_scripts=["bibexport", "listbib" ,"multibibliography", "urlbst"]

    core_scripts=["a2ping","a5toa4", "adhocfilelist", "afm2afm", "allcm", "allec", "allneeded", "arara","arlatex"
    ,"autoinst", "bundledoc", "checkcites", "chkweb", "context", "ctanify", "ctanupload", "ctxtools", "de-macro", "deweb"
    ,"dosepsbin", "dtxgen", "dvi2fax", "dviasm", "dvired", "e2pall", "epstopdf", "findhyph", "fmtutil", "fmtutil-sys"
    ,"fontinst", "fragmaster", "installfont-tl", "kpsepath", "kpsetool", "kpsewhere", "kpsexpand", "latex2man", "latexdiff"
    ,"latexdiff-vc", "latexfileversion", "latexmk", "latexpand", "latexrevise", "listings-ext.sh", "ltxfileinfo", "lua2dox_filter"
    ,"luaotfload-tool", "luatools", "match_parens", "mf2pt1", "mkjobtexmf", "mkluatexfontdb", "mkt1font", "mktexfmt", "mptopdf"
    ,"mtxrun", "ot2kpx", "pdf180", "pdf270", "pdf90", "pdfatfi", "pdfbook", "pdfcrop", "pdfflip", "pdfjam", "pdfjam-pocketmod"
    ,"pdfjam-slides3up", "pdfjam-slides6up", "pdfjoin", "pdfnup", "pdfpun", "pfarrei", "pkfix", "pkfix-helper", "ps2eps", "ps2frag"
    ,"pslatex", "pstopdf", "purifyeps", "repstopdf", "rpdfcrop", "rungs", "simpdftex", "sty2dtx", "texconfig", "texconfig-dialog"
    ,"texconfig-sys", "texcount", "texdef", "texdiff", "texdirflatten", "texdoc", "texdoctk", "texexec", "texindy", "texlinks"
    ,"texliveonfly", "texloganalyser", "texmfstart", "thumbpdf", "typeoutfileinfo", "updmap", "updmap-sys", "vpl2ovp", "vpl2vpl", "xindy"]

    htmlxml_scripts=["ht", "htcontext", "htlatex", "htmex", "httex", "httexi", "htxelatex", "htxetex", "mk4ht"]

    langcyrillic_scripts=["rubibtex", "rumakeindex"]

    langcjk_scripts=["convbkmk", "ptex2pdf", "kanji-fontmap-creator", "kanji-config-updmap", "kanji-config-updmap-sys"]

    langextra_scripts=["ebong"]

    langgreek_scripts=["mkgrkindex"]

    latexextra_scripts=["authorindex", "exceltex", "makeglossaries", "pdfannotextractor", "perltex", "ps4pdf", "splitindex" ,"svn-multi", "vpe"]

    music_scripts=["m-tx", "musixtex", "musixflx", "pmx2pdf"]

    pictures_scripts=["cachepic", "epspdf", "epspdftk", "fig4latex", "mathspic"]

    pstricks_scripts=["pedigree", "pst2pdf"]

    science_scripts=["ulqda"]

    # remove unneeded files and symlinks
    dirs = []
    for g in [bibtexextra_scripts, core_scripts, htmlxml_scripts, \
              langcjk_scripts, langcyrillic_scripts, langextra_scripts, \
              langgreek_scripts, latexextra_scripts, music_scripts, \
              pictures_scripts, pstricks_scripts, science_scripts, \
              ["tlmgr"]]:
        for s in g:
            if shelltools.isLink("%s/usr/bin/%s" % (get.installDIR(), s)):
                realpath = shelltools.realPath("%s/usr/bin/%s" % (get.installDIR(), s))
                dirname = shelltools.dirName(realpath)
                if not dirname in dirs: dirs.append(dirname)
                if not dirname == "%s/usr/bin" % get.installDIR():
                    if shelltools.isFile(realpath): shelltools.unlink(realpath)
                pisitools.remove("/usr/bin/%s" % s)

    # remove empty dirs
    while dirs:
        tmpdirs = dirs[:]
        for d in tmpdirs:
            if not shelltools.ls(d):
                shelltools.unlinkDir(d)
                dirname = shelltools.dirName(d)
                if not dirname in dirs: dirs.append(dirname)
            dirs.remove(d)

    pdftexsymlinks=["amstex", "cslatex", "csplain", "eplain", "etex", "jadetex", "latex", "mex", "mllatex", "mltex"
          ,"pdfetex", "pdfcslatex", "pdfcsplain", "pdfjadetex", "pdflatex", "pdfmex", "pdfxmltex", "texsis", "utf8mex", "xmltex"]

    for symlink in pdftexsymlinks:
        pisitools.dosym("pdftex", "/usr/bin/%s" % symlink)

    luatexsymlinks=["dvilualatex", "dviluatex", "lualatex"]

    for symlink in luatexsymlinks:
        pisitools.dosym("pdftex", "/usr/bin/%s" % symlink)


    pisitools.dosym("eptex", "/usr/bin/platex")
    pisitools.dosym("euptex", "/usr/bin/uplatex")
    pisitools.dosym("xetex", "/usr/bin/xelatex")

    pisitools.removeDir("/usr/share/texmf-dist")