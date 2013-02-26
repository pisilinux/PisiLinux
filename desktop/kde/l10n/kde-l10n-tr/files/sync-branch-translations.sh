#!/bin/bash

ARCHIVE=`grep "<Archive.*>" pspec.xml | sed 's/.*<Archive.*>\(.*\)<\/Archive>/\1/'`
BRANCH="/home/ozan/svn/l10n-tr"

pisi bi pspec.xml --fetch
tar xvf /var/cache/pisi/archives/`basename $ARCHIVE`
cd kde-l10n-tr-4*
quilt new BRANCH.patch
find messages -name "*.po" | xargs quilt add
for i in $(find messages -name "*.po"); do
    \cp -f $BRANCH/$i $i
done

quilt refresh
cd ..

\cp kde-l10n-tr-4*/patches/BRANCH.patch files/
svn add files/BRANCH.patch
