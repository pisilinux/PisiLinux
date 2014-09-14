#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

amd_version = "2.3.1"
amd_version_major = "2"
btf_version = "1.2.0"
btf_version_major = "1"
camd_version = "2.3.1"
camd_version_major = "2"
ccolamd_version = "2.8.0"
ccolamd_version_major = "2"
cholmod_version = "2.0.1"
cholmod_version_major = "2"
colamd_version = "2.8.0"
colamd_version_major = "2"
csparse_version = "3.1.1"
csparse_version_major = "3"
klu_version = "1.2.1"
klu_version_major = "1"
ldl_version = "2.1.0"
ldl_version_major = "2"
umfpack_version = "5.6.1"
umfpack_version_major = "5"
spqr_version = "1.3.1"
spqr_version_major = "1"
rbio_version = "2.1.1"
rbio_version_major = "2"
SuiteSparse_config_ver = "4.2.0"
SuiteSparse_config_major = "4"

def build():
    shelltools.export("CFLAGS","%s -fPIC -O3" % get.CFLAGS())
    
    for d in ("AMD", "BTF", "CAMD", "CCOLAMD", "CHOLMOD", "COLAMD", "CSparse", "KLU", "LDL", "UMFPACK", "SPQR", "RBio"):
        shelltools.makedirs("Doc/%s" % d)
    shelltools.makedirs("Include")
    shelltools.makedirs("Lib")

    shelltools.cd("SuiteSparse_config")
    autotools.make()
    shelltools.system("ar x libsuitesparseconfig.a")
    shelltools.cd("../Lib")
    shelltools.system("gcc -shared -Wl,-soname,libsuitesparseconfig.so.%s -o \
                       libsuitesparseconfig.so.%s ../SuiteSparse_config/*.o" % (SuiteSparse_config_major, SuiteSparse_config_ver))
    shelltools.sym("libsuitesparseconfig.so.%s" % SuiteSparse_config_ver, "libsuitesparseconfig.so.%s" % SuiteSparse_config_major)
    shelltools.sym("libsuitesparseconfig.so.%s" % SuiteSparse_config_ver, "libsuitesparseconfig.so")
    shelltools.copy("../SuiteSparse_config/*.a", ".")
    shelltools.cd("../SuiteSparse_config")
    shelltools.copy("*.h", "../Include")

    shelltools.cd("../AMD/Lib")
    autotools.make()
    shelltools.cd("../../Lib")
    shelltools.system("gcc -shared -Wl,-soname,libamd.so.%s -o \
                       libamd.so.%s ../AMD/Lib/*.o -lm -lrt" % (amd_version_major, amd_version))
    shelltools.sym("libamd.so.%s" % amd_version, "libamd.so.%s" % amd_version_major)
    shelltools.sym("libamd.so.%s" % amd_version, "libamd.so")
    shelltools.copy("../AMD/Lib/*.a", ".")
    shelltools.cd("../AMD")
    shelltools.copy("Include/*.h", "../Include")
    for d in ("README.txt", "Doc/License", "Doc/ChangeLog", "Doc/*.pdf"):
        shelltools.copy(d, "../Doc/AMD")

    shelltools.cd("../BTF/Lib")
    autotools.make()
    shelltools.cd("../../Lib")
    shelltools.system("gcc -shared -Wl,-soname,libbtf.so.%s -o \
                       libbtf.so.%s ../BTF/Lib/*.o" % (btf_version_major, btf_version))
    shelltools.sym("libbtf.so.%s" % btf_version, "libbtf.so.%s" % btf_version_major)
    shelltools.sym("libbtf.so.%s" % btf_version, "libbtf.so")
    shelltools.copy("../BTF/Lib/*.a", ".")
    shelltools.cd("../BTF")
    shelltools.copy("Include/*.h", "../Include")
    for d in ("README.txt", "Doc/*"):
        shelltools.copy(d, "../Doc/BTF")

    shelltools.cd("../CAMD/Lib")
    autotools.make()
    shelltools.cd("../../Lib")
    shelltools.system("gcc -shared -Wl,-soname,libcamd.so.%s -o \
                       libcamd.so.%s ../CAMD/Lib/*.o -lm" % (camd_version_major, camd_version))
    shelltools.sym("libcamd.so.%s" % camd_version, "libcamd.so.%s" % camd_version_major)
    shelltools.sym("libcamd.so.%s" % camd_version, "libcamd.so")
    shelltools.copy("../CAMD/Lib/*.a", ".")
    shelltools.cd("../CAMD")
    shelltools.copy("Include/*.h", "../Include")
    for d in ("README.txt", "Doc/ChangeLog", "Doc/License", "Doc/*.pdf"):
        shelltools.copy(d, "../Doc/CAMD")

    shelltools.cd("../CCOLAMD/Lib")
    autotools.make()
    shelltools.cd("../../Lib")
    shelltools.system("gcc -shared -Wl,-soname,libccolamd.so.%s -o \
                       libccolamd.so.%s ../CCOLAMD/Lib/*.o -lm" % (ccolamd_version_major, ccolamd_version))
    shelltools.sym("libccolamd.so.%s" % ccolamd_version, "libccolamd.so.%s" % ccolamd_version_major)
    shelltools.sym("libccolamd.so.%s" % ccolamd_version, "libccolamd.so")
    shelltools.copy("../CCOLAMD/Lib/*.a", ".")
    shelltools.cd("../CCOLAMD")
    shelltools.copy("Include/*.h", "../Include")
    for d in ("README.txt", "Doc/*"):
        shelltools.copy(d, "../Doc/CCOLAMD")

    shelltools.cd("../COLAMD/Lib")
    autotools.make()
    shelltools.cd("../../Lib")
    shelltools.system("gcc -shared -Wl,-soname,libcolamd.so.%s -o \
                       libcolamd.so.%s ../COLAMD/Lib/*.o -lm" % (colamd_version_major, colamd_version))
    shelltools.sym("libcolamd.so.%s" % colamd_version, "libcolamd.so.%s" % colamd_version_major)
    shelltools.sym("libcolamd.so.%s" % colamd_version, "libcolamd.so")
    shelltools.copy("../COLAMD/Lib/*.a", ".")
    shelltools.cd("../COLAMD")
    shelltools.copy("Include/*.h", "../Include")
    for d in ("README.txt", "Doc/*"):
        shelltools.copy(d, "../Doc/COLAMD")

    shelltools.cd("../CHOLMOD/Lib")
    autotools.make("-I/usr/include/metis")
    shelltools.cd("../../Lib")
    shelltools.system("gcc -shared -Wl,-soname,libcholmod.so.%s -o \
                       libcholmod.so.%s ../CHOLMOD/Lib/*.o \
                       -L/usr/lib/atlas -llapack libamd.so.%s \
                       libcamd.so.%s libcolamd.so.%s \
                       libccolamd.so.%s \
                       libsuitesparseconfig.so.%s \
                       -lm" % (cholmod_version_major,
                               cholmod_version,
                               amd_version_major,
                               camd_version_major, colamd_version_major,
                               ccolamd_version_major,
                               SuiteSparse_config_major))
    shelltools.sym("libcholmod.so.%s" % cholmod_version, "libcholmod.so.%s" % cholmod_version_major)
    shelltools.sym("libcholmod.so.%s" % cholmod_version, "libcholmod.so")
    shelltools.copy("../CHOLMOD/Lib/*.a", ".")
    shelltools.cd("../CHOLMOD")
    shelltools.copy("Include/*.h", "../Include")
    shelltools.copy("README.txt", "../Doc/CHOLMOD")
    shelltools.copy("Doc/*.pdf", "../Doc/CHOLMOD")
    shelltools.copy("Cholesky/License.txt", "../Doc/CHOLMOD/Cholesky_License.txt")
    shelltools.copy("Core/License.txt", "../Doc/CHOLMOD/Core_License.txt")
    shelltools.copy("MatrixOps/License.txt", "../Doc/CHOLMOD/MatrixOps_License.txt")
    shelltools.copy("Partition/License.txt", "../Doc/CHOLMOD/Partition_License.txt")
    shelltools.copy("Supernodal/License.txt", "../Doc/CHOLMOD/Supernodal_License.txt")

    shelltools.cd("../CSparse/Include")
    shelltools.copy("cs.h", "../../Include")
    shelltools.cd("../Lib")
    autotools.make()
    shelltools.cd("../../Lib")
    shelltools.system("gcc -shared -Wl,-soname,libcsparse.so.%s -o \
                       libcsparse.so.%s ../CSparse/Lib/*.o -lm" % (csparse_version_major, csparse_version))
    shelltools.sym("libcsparse.so.%s" % csparse_version, "libcsparse.so.%s" % csparse_version_major)
    shelltools.sym("libcsparse.so.%s" % csparse_version, "libcsparse.so")
    shelltools.copy("../CSparse/Lib/*.a", ".")
    shelltools.cd("../CSparse")
    shelltools.copy("Doc/*", "../Doc/CSparse")

    shelltools.cd("../KLU/Lib")
    autotools.make()
    shelltools.cd("../../Lib")
    shelltools.system("gcc -shared -Wl,-soname,libklu.so.%s -o \
                       libklu.so.%s ../KLU/Lib/*.o \
                       libamd.so.%s libcolamd.so.%s \
                       libbtf.so.%s libcholmod.so.%s \
                       libsuitesparseconfig.so.%s \
                       " % (klu_version_major,
                            klu_version,
                            amd_version_major, colamd_version_major,
                            btf_version_major, cholmod_version_major,
                            SuiteSparse_config_major))
    shelltools.sym("libklu.so.%s" % klu_version, "libklu.so.%s" % klu_version_major)
    shelltools.sym("libklu.so.%s" % klu_version, "libklu.so")
    shelltools.copy("../KLU/Lib/*.a", ".")
    shelltools.cd("../KLU")
    shelltools.copy("Include/*.h", "../Include")
    for d in "README.txt Doc/lesser.txt".split(" "):
        shelltools.copy(d, "../Doc/KLU")

    shelltools.cd("../LDL/Lib")
    autotools.make()
    shelltools.cd("../../Lib")
    shelltools.system("gcc -shared -Wl,-soname,libldl.so.%s -o \
                       libldl.so.%s ../LDL/Lib/*.o" % (ldl_version_major, ldl_version))
    shelltools.sym("libldl.so.%s" % ldl_version, "libldl.so.%s" % ldl_version_major)
    shelltools.sym("libldl.so.%s" % ldl_version, "libldl.so")
    shelltools.copy("../LDL/Lib/*.a", ".")
    shelltools.cd("../LDL")
    shelltools.copy("Include/*.h", "../Include")
    for d in "README.txt Doc/ChangeLog Doc/lesser.txt Doc/*.pdf".split(" "):
        shelltools.copy(d, "../Doc/LDL")

    shelltools.cd("../UMFPACK/Lib")
    autotools.make()
    shelltools.cd("../../Lib")
    shelltools.system("gcc -shared -Wl,-soname,libumfpack.so.%s -o \
                       libumfpack.so.%s ../UMFPACK/Lib/*.o \
                       -L/usr/lib/atlas -llapack libamd.so.%s \
                       libcholmod.so.%s \
                       libsuitesparseconfig.so.%s \
                       -lm" % (umfpack_version_major, 
                               umfpack_version,
                               amd_version_major,
                               cholmod_version_major,
                               SuiteSparse_config_major))
    shelltools.sym("libumfpack.so.%s" % umfpack_version, "libumfpack.so.%s" % umfpack_version_major)
    shelltools.sym("libumfpack.so.%s" % umfpack_version, "libumfpack.so")
    shelltools.copy("../UMFPACK/Lib/*.a", ".")
    shelltools.cd("../UMFPACK")
    shelltools.copy("Include/*.h", "../Include")
    for d in "README.txt Doc/License Doc/ChangeLog Doc/gpl.txt Doc/*.pdf".split(" "):
        shelltools.copy(d, "../Doc/UMFPACK")

    shelltools.cd("../SPQR/Lib")
    autotools.make('CXXFLAS="%s -DNPARTITION -fPIC -O3"' % get.CXXFLAGS())
    shelltools.cd("../../Lib")
    shelltools.system("g++ -shared -Wl,-soname,libspqr.so.%s -o \
                       libspqr.so.%s ../SPQR/Lib/*.o \
                       -L/usr/lib/atlas -L/usr/lib -llapack \
                       libcholmod.so.%s \
                       libsuitesparseconfig.so.%s \
                       -lm" % (spqr_version_major,
                               spqr_version,
                               cholmod_version_major,
                               SuiteSparse_config_major))
    shelltools.sym("libspqr.so.%s" % spqr_version, "libspqr.so.%s" % spqr_version_major)
    shelltools.sym("libspqr.so.%s" % spqr_version, "libspqr.so")
    shelltools.copy("../SPQR/Lib/*.a", ".")
    shelltools.cd("../SPQR")
    shelltools.copy("Include/*.h*", "../Include")
    shelltools.copy("README.txt", "README_SPQR.txt")
    shelltools.copy("README_SPQR.txt", "../Doc/SPQR")
    shelltools.copy("Doc/*", "../Doc/SPQR")

    shelltools.cd("../RBio/Lib")
    autotools.make()
    shelltools.cd("../../Lib")
    shelltools.system("gcc -shared -Wl,-soname,librbio.so.%s -o \
                       librbio.so.%s ../RBio/Lib/*.o \
                       libsuitesparseconfig.so.%s" % (rbio_version_major, rbio_version, SuiteSparse_config_major))
    shelltools.sym("librbio.so.%s" % rbio_version, "librbio.so.%s" % rbio_version_major)
    shelltools.sym("librbio.so.%s" % rbio_version, "librbio.so")
    shelltools.copy("../RBio/Lib/*.a", ".")
    shelltools.cd("../RBio")
    shelltools.copy("Include/*.h", "../Include")
    for d in "README.txt Doc/ChangeLog Doc/License.txt".split(" "):
        shelltools.copy(d, "../Doc/RBio")

def install():
    pisitools.insinto("/usr/include/%s" % get.srcNAME().lower(), "Include/*.h")
    pisitools.dodoc("README.txt")
    shelltools.copy("Doc/*", "%s/usr/share/doc/%s" % (get.installDIR(), get.srcNAME()))
    shelltools.cd("Lib")
    for l in shelltools.ls("*.so*"):
        pisitools.insinto("/usr/lib", l)
    for l in shelltools.ls("*.a"):
        pisitools.insinto("/usr/lib", l)
