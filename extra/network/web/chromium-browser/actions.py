#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

#ARCH = "x64" if get.ARCH() == "x86_64" else "ia32"
#PARSED_OPT_FLAGS="echo \'%{optflags} -D_GNU_SOURCE\' | sed 's/ /',/g' | sed 's/',/', '/g'"

def setup():

    #shelltools.system("sh -x ./clean-source.sh")
    #shelltools.system("sed -i 's|'-O<(release_optimize)'|$PARSED_OPT_FLAGS|g' build/common.gypi")
    #shelltools.system("build/linux/unbundle/remove_bundled_libraries.py --do-remove")
    
    shelltools.export("LC_ALL", "C")
    shelltools.system("sed -i 's|icu)|icu-i18n)|g' build/linux/system.gyp")
    #pisitools.flags.add("-fno-stack-protector","-fno-ipa-cp")
    shelltools.system("export -n CFLAGS CXXFLAGS")

    
    options = "\
               -Duse_system_expat=1 \
               -Duse_system_flac=1 \
               -Duse_system_harfbuzz=0 \
               -Duse_system_icu=0 \
               -Duse_system_jsoncpp=1 \
               -Duse_system_libevent=1 \
               -Duse_system_libjpeg=1 \
               -Duse_system_libpng=1 \
               -Duse_system_libvpx=0 \
               -Duse_system_libwebp=1 \
               -Duse_system_opus=1 \
               -Duse_system_snappy=1 \
               -Duse_system_speex=1 \
               -Duse_system_zlib=1 \
               -Duse_gconf=0 \
               -Dlinux_use_bundled_gold=0 \
               -Dlinux_use_bundled_binutils=0 \
               -Dlinux_link_gsettings=1 \
               -Dlinux_link_kerberos=1 \
               -Dlinux_link_libbrlapi=1 \
               -Dlinux_link_libgps=1 \
               -Dlinux_link_libpci=1 \
               -Dlinux_link_libspeechd=1 \
               -Dlinux_link_pulseaudio=1 \
               -Dlibspeechd_h_prefix=speech-dispatcher/ \
               -Dclang=0 \
               -Dwerror= \
               -Ddisable_nacl=1 \
               -Ddisable_fatal_linker_warnings=1 \
               -Dtarget_arch=x64 \
               -Dffmpeg_branding=Chromium \
               -Dpython_arch=x64 \
               -Dlogging_like_official_build=1 \
               -Dlinux_sandbox_chrome_path=/usr/lib/chromium-browser/chromium-browser \
               -Dlinux_sandbox_path=/usr/lib/chromium-browser/chromium-sandbox \
               -Dusb_ids_path=/usr/share/misc/usb.ids \
               -Dgoogle_api_key=AIzaSyBINKL31ZYd8W5byPuwTXYK6cEyoceGh6Y \
               -Dgoogle_default_client_id=879512332529.apps.googleusercontent.com \
               -Dgoogle_default_client_secret=RmQPJJeL1cNJ8iETnoVD4X17 "
   

    shelltools.system("build/linux/unbundle/replace_gyp_files.py  %s" % options)
   
    shelltools.export("GYP_GENERATORS","ninja")
    shelltools.system("build/gyp_chromium build/all.gyp --depth=.  %s" % options)
    
#    shelltools.system("build/download_nacl_toolchains.py --packages \
#                      nacl_x86_glibc,nacl_x86_newlib,pnacl_newlib,pnacl_translator")
  
  
def build():
   
    shelltools.system("ninja -C out/Release chrome")
    shelltools.system("ninja -C out/Release chrome_sandbox")
    shelltools.system("ninja -C out/Release chromedriver")

def install():
  
    shelltools.cd("out/Release")

    shelltools.makedirs("%s/usr/lib/chromium-browser" % get.installDIR())
    
    binaries_for_inst=["chrome", "chrome_sandbox", "chromedriver", "natives_blob.bin", "snapshot_blob.bin"]
    libraries_for_inst=["libffmpegsumo.so", "icudtl.dat"]
   
    # install and strip binaries
    for mybin in binaries_for_inst:
        pisitools.insinto("/usr/lib/chromium-browser", mybin)
       
    # install and strip shared libs  
    for mylib in libraries_for_inst:
        pisitools.insinto("/usr/lib/chromium-browser", mylib)
        #use it if pisi skips stripping
        #shelltools.system("strip --strip-unneeded %s/usr/lib/chromium-browser/%s" % ( get.installDIR(), mylib))                                    
        
    pisitools.dosym("/usr/lib/chromium-browser/chrome", "/usr/lib/chromium-browser/chromium-browser")
    pisitools.rename("/usr/lib/chromium-browser/chrome_sandbox", "chrome-sandbox")
    shelltools.chmod("%s/usr/lib/chromium-browser/chrome-sandbox" % get.installDIR(), 04755)
    
     # install rest of needed files
    pisitools.insinto("/usr/lib/chromium-browser", "*.pak")
    pisitools.insinto("/usr/lib/chromium-browser", "locales")
    pisitools.insinto("/usr/lib/chromium-browser", "resources")
    
    pisitools.newman("chrome.1", "chromium-browser.1")
    
    shelltools.cd("../..")
    for size in ["22", "24", "48", "64", "128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" %(size, size), "chrome/app/theme/chromium/product_logo_%s.png" % size, "chromium-browser.png")
        
    #shelltools.copytree("PepperFlash", "%s/usr/lib/chromium-browser/" % get.installDIR())
			
    pisitools.dosym("/usr/share/icons/hicolor/256x256/apps/chromium-browser.png", "/usr/share/pixmaps/chromium-browser.png")
    
    pisitools.dodoc("LICENSE")


    