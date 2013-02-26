#!/usr/bin/python
import os
import re
import sys
if len (sys.argv) < 3:
    print "Specify hpcups.drv and hpijs.drv pathnames"
    sys.exit (1)

hpcups_drv = sys.argv[1]
hpijs_drv = sys.argv[2]

# Match e.g.      Attribute "ShortNickName" "" "blah"
# and catch 'blah' in group 0
snn_re = re.compile ('^\s*Attribute\s+"ShortNickName"\s+""\s+"(.*)"\s*$')

# Match e.g.      Attribute "1284DeviceID" "" "blah"
# and catch everything before 'blah' in group 0, 'blah' in group 1,
# trailing characters in group 2
devid_re = re.compile ('^(\s*Attribute\s+"1284DeviceID"\s+""\s+")(.*)("\s*)$')

# Match e.g.   }
end_re = re.compile ('^\s*}')

devid_by_snn = dict()

hpcups_lines = file (hpcups_drv, "r").readlines ()
current_snn = None
for line in hpcups_lines:
    if current_snn == None:
        match = snn_re.match (line)
        if match == None:
            continue

        current_snn = match.groups ()[0]
    else:
        match = devid_re.match (line)
        if match:
            devid_by_snn[current_snn] = match.groups ()[1]
            continue

    if end_re.match (line):
        current_snn = None

print >>sys.stderr, \
    "%d IEEE 1284 Device IDs loaded from %s" % (len (devid_by_snn),
                                                os.path.basename (hpcups_drv))

replaced = 0
hpijs_lines = file (hpijs_drv, "r").readlines ()
current_snn = None
for line in hpijs_lines:
    if current_snn == None:
        match = snn_re.match (line)
        if match:
            current_snn = match.groups ()[0]
            if current_snn.endswith (" hpijs"):
                current_snn = current_snn[:-6]
    else:
        match = devid_re.match (line)
        if match:
            devid = devid_by_snn.get (current_snn)
            if devid:
                line = (match.groups ()[0] + devid + match.groups ()[2])
                replaced += 1

    if end_re.match (line):
        current_snn = None

    print line.rstrip ("\n")

print >>sys.stderr, \
    "%d IEEE 1284 Device IDs replaced in %s" % (replaced,
                                                os.path.basename (hpijs_drv))
