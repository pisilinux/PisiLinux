#!/bin/bash
#
# A small script to create a tarball of kicad including 
# kicad, kicad-doc and kicad-library sub-packages.
# Acquired from Ubuntu kicad package

d=kicad-0.0.$(date +%Y%m%d).orig
tgz=kicad_0.0.$(date +%Y%m%d).orig.tar.gz
dd=${d/.orig/}
mkdir $d
bzr export $d/kicad lp:kicad/stable 
bzr export $d/kicad-doc lp:~kicad-developers/kicad/doc
bzr export $d/kicad-library lp:~kicad-lib-committers/kicad/library
cp -a $d $dd
tar czf $tgz $d && rm -rf $d

# remove any unwanted stuff
rm -rf $dd/kicad/kicad/minizip
#rm -rf $dd/kicad-doc/doc/help/{de,es,it}
rm -rf $dd/kicad-doc/presentations

