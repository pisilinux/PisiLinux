#!/bin/bash

if [ "x$2" == "xclean" ]; then
    find $1 -type d -name "pdf" -exec rm -rf {} \;
fi

# Generate empty pdf files for workarounding missing fop
for fo in $(find -name "*.fo"); do
    pdf=`echo $fo | sed 's/\.fo/.pdf/g'`
    echo "Dummy PDF to fake the build system" > $pdf
done
