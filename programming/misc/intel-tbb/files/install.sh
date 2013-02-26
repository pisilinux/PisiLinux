#!/bin/bash

DESTDIR=$1

mkdir -p $DESTDIR/usr/{lib,include}

pushd build/obj_release
    for file in libtbb{,malloc}; do
        install -p -D -m 755 ${file}.so.2 $DESTDIR/usr/lib/
        ln -s $file.so.2 $DESTDIR/usr/lib/$file.so
    done
popd

pushd include
    find tbb -type f -name \*.h -exec \
        install -p -D -m 644 {} $DESTDIR/usr/include/{} \
    \;
popd

