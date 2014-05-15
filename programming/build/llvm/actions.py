
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pkgconfig
from pisi.actionsapi import get
from pisi.actionsapi import kde4

WorkDir = "%s-%s.src" % (get.srcNAME(), get.srcVERSION())
libdir = "/usr/lib32/llvm" if get.buildTYPE() == "emul32" else "/usr/lib/llvm"
lib = "lib32" if get.buildTYPE() == "emul32" else "lib"

def setup():
    if not shelltools.isDirectory("tools/clang"):
        pisitools.dosed("tools/cfe-3.4.1.src/lib/Driver/ToolChains.cpp", '"ld"', '"ld.gold"')
        shelltools.move("tools/cfe-%s.src" % get.srcVERSION(), "tools/clang")
        shelltools.move("tools/clang-tools-extra-3.4", "tools/clang/extra")
    if not shelltools.isDirectory("projects/compiler-rt"):
        shelltools.move("projects/compiler-rt-3.4", "projects/compiler-rt")

    pisitools.dosed("utils/llvm-build/llvm-build", "python", "python2.7")
    pisitools.dosed("bindings/ocaml/Makefile.ocaml", '\$\(PROJ_libdir\)', libdir)
    pisitools.dosed("Makefile.config.in", "\$\(PROJ_prefix\)/etc/llvm", "/etc/llvm")
    pisitools.dosed("Makefile.config.in", "\$\(PROJ_prefix\)/lib", "$(PROJ_prefix)/%s/llvm" % lib)
    pisitools.dosed("Makefile.config.in", "\$\(PROJ_prefix\)/docs/llvm", "$(PROJ_prefix)/share/doc/llvm")
    pisitools.dosed("tools/llvm-config/llvm-config.cpp", '(ActiveLibDir\s=\sActivePrefix\s\+\s\"\/lib)(.*)', r'\1/llvm\2')
    pisitools.dosed("autoconf/configure.ac", '\LLVM_LIBDIR="\$\{prefix\}/lib"', 'LLVM_LIBDIR="${prefix}/%s/llvm"' % lib)

    pisitools.dosed("Makefile.rules", "\$\(RPATH\)\s-Wl,\$\(ExmplDir\)\s\$\(DynamicFlag\)", "$(DynamicFlag)")
    pisitools.dosed("Makefile.rules", "\$\(RPATH\)\s-Wl,\$\(ToolDir\)\s\$\(DynamicFlag\)", "$(DynamicFlag)")

    shelltools.export("CPPFLAGS","%s %s" % (get.CXXFLAGS(),pkgconfig.getLibraryCFLAGS("libffi")))

    pic_option = "enable" if get.ARCH() == "x86_64" else "disable"

    options = "--libdir=%s \
               --datadir=/usr/share/llvm \
               --sysconfdir=/etc \
               --enable-shared \
               --enable-libffi \
               --enable-targets=all \
               --disable-expensive-checks \
               --disable-debug-runtime \
               --disable-assertions \
               --enable-jit \
               --enable-threads \
               --disable-assertions \
               --%s-pic \
               --with-binutils-include=/usr/include \
               " % (libdir, pic_option)

    autotools.configure(options)


#def check():
#    autotools.make("check")
#    autotools.make("-C tools/clang test")

def build():
    autotools.make("REQUIRES_RTTI=1")

def install():
    if get.buildTYPE() == "emul32":

        autotools.rawInstall("DESTDIR=%s \
                              PROJ_etcdir=/etc/llvm \
                              PROJ_libdir=/usr/lib32/llvm \
                              PROJ_docsdir=/%s/llvm"
                              % (get.installDIR(),  get.docDIR()))
        shelltools.chmod("%s/usr/lib32/llvm/*.a" % get.installDIR(), mode = 0644)
        pisitools.dosym("llvm/LLVMgold.so", "/usr/lib32/LLVMgold.so")
        pisitools.remove("/usr/lib32/llvm/*LLVMHello.*")
        return
    else:
        autotools.rawInstall("DESTDIR=%s \
                              PROJ_etcdir=/etc/llvm \
                              PROJ_libdir=%s \
                              PROJ_docsdir=/%s/llvm"
                              % (get.installDIR(), libdir, get.docDIR()))


    shelltools.chmod("%s/usr/lib/llvm/*.a" % get.installDIR(), 0644)

    # Install static analyzers which aren't installed by default
    for exe in ("scan-build", "scan-view"):
        pisitools.insinto("/usr/lib/clang-analyzer/%s" % exe, "tools/clang/tools/%s/%s" % (exe, exe))
        pisitools.dosym("/usr/lib/clang-analyzer/%s/%s" % (exe, exe), "/usr/bin/%s" % exe)

    pisitools.dodir("/etc/ld.so.conf.d")
    shelltools.echo("%s/etc/ld.so.conf.d/51-llvm.conf" % get.installDIR(), "/usr/lib/llvm")

    # Symlink the gold plugin where clang expects it
    pisitools.dosym("llvm/LLVMgold.so", "/usr/lib/LLVMgold.so")

    # Remove example file
    pisitools.remove("/usr/lib/llvm/*LLVMHello.*")

    pisitools.remove("/usr/share/doc/llvm/*.tar.gz")
    pisitools.remove("/usr/share/doc/llvm/ocamldoc/html/*.tar.gz")
    pisitools.removeDir("/usr/share/doc/llvm/ps")

    # Install vim syntax files for .ll and .td files
    # llvm.vim additional file add ftdetct vim file to detect .ll and .td as llvm files
    pisitools.insinto("/usr/share/vim/vimfiles/syntax", "utils/vim/*.vim")

    # Install kate syntax file
    pisitools.insinto("%s/katepart/syntax" % kde4.appsdir, "utils/kate/*.xml")

    pisitools.dodoc("CREDITS.TXT", "LICENSE.TXT", "README.txt")
