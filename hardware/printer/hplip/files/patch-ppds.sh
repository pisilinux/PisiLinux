#!/bin/bash

PATCH=$1

# Decompress the relevant PPD files
for ppd_file in $(grep '^diff' $PATCH | cut -d " " -f 4);
do
  gunzip ${ppd_file#*/}.gz
done

# Patch the PPD files
patch -p1 < $PATCH

# Recompress back
for ppd_file in $(grep '^diff' $PATCH | cut -d " " -f 4);
do
  gzip -n ${ppd_file#*/}
done
