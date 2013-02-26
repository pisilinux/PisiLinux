#!/bin/bash

# remove adjacent blank lines
sed -i 's/^[\t\ ]*$//;/./,/^$/!d' man/man*/*.[58]

#sed -i 's/sntp\.1/sntp\.8/' man/man1/sntp.1
#mv man/man1/sntp.1 man/man8/sntp.8

# fix section numbers
sed -i 's/\(\.TH[a-zA-Z ]*\)[1-9]\(.*\)/\18\2/' man/man8/*.8
