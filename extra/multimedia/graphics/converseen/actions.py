#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure("-DImageMagick_Magick++_INCLUDE_DIR=/usr/include/ImageMagick-6 \
						  -DImageMagick_MagickCore_INCLUDE_DIR=/usr/include/ImageMagick-6 \
						  -DImageMagick_MagickWand_INCLUDE_DIR=/usr/include/ImageMagick-6 \
						  -DImageMagick_Magick++_LIBRARY=/usr/lib/libMagick++-6.Q16HDRI.so \
						  -DImageMagick_MagickCore_LIBRARY=/usr/lib/libMagickCore-6.Q16HDRI.so \
						  -DImageMagick_MagickWand_LIBRARY=/usr/lib/libMagickWand-6.Q16HDRI.so")
    
def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    pisitools.dodoc("COPYING", "INSTALL")
