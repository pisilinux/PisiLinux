#!/bin/bash

# Generate nss.pc from nss.pc.in
# Ozan Caglayan, 2010
#
# Generate nspr.pc from nspr.pc.in
# Metin Akdere, 2012

LIBDIR="/usr/lib/nspr"
PREFIX="/usr"
EXEC_PREFIX="/usr"
INCLUDEDIR="/usr/include/nspr"

PKGCONFIG="nspr/config/nspr.pc.in"

NSPR_VERSION=`./config/nspr-config --version`
NSPR_LIBS=`./config/nspr-config --libs`
NSPR_CFLAGS=`./config/nspr-config --cflags`

echo "NSPR_VERSION: $NSPR_VERSION"
echo "NSPR_LIBS: $NSPR_LIBS"
echo "NSPR_CFLAGS: $NSPR_CFLAGS"

# Setup pkgconfig file
cat $PKGCONFIG | sed    -e "s,%libdir%,$LIBDIR,g" \
                        -e "s,%prefix%,$PREFIX,g" \
                        -e "s,%exec_prefix%,$EXEC_PREFIX,g" \
                        -e "s,%includedir%,$INCLUDEDIR,g" \
                        -e "s,%NSPR_VERSION%,$NSPR_VERSION,g" \
                        -e "s,%FULL_NSPR_LIBS%,$NSPR_LIBS,g" \
                        -e "s,%FULL_NSPR_CFLAGS%,$NSPR_CFLAGS,g" \
                        > config/nspr.pc


# Clear .in files
rm -rf $PKGCONFIG
