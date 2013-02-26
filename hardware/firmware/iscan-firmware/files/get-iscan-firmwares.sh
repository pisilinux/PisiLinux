#!/bin/bash

URL="http://linux.avasys.jp/drivers/iscan-plugins/"

if [ ! -d iscan-firmware ]; then
    wget -nd -np -r -e robots=off -P iscan-firmware --accept=i386.rpm,x86_64.rpm $URL
fi

cd iscan-firmware
for fwrpm in $(ls *.rpm 2>/dev/null); do
    rpm2targz $fwrpm
    rm -f $fwrpm
done

for fwtargz in $(ls *.tar.gz); do
    tar xvf $fwtargz
done

cat /dev/null > fwlist

for f in $(ls *i386*tar.gz); do
    echo $f >> fwlist
    libs=$(tar tvf $f | grep 'lib/.*\/lib[-a-zA-Z0-9]*\.so\.[0-9]\.[0-9]\.[0-9]' | gawk '{print $6}')
    for lib in $libs; do
        echo "library is: $lib" >> fwlist
        echo "firmware is: `strings $lib | grep 'esfw.*bin'`" >> fwlist
    done
    echo >> fwlist
done

