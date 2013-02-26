#!/usr/bin/python

import os

FW_DATA = {
            "0x04b8:0x083f"     : ["iscan-plugin-cx4400",  "libesint7E", ""],
            "0x04b8:0x0133"     : ["iscan-plugin-gt-1500", "libesint86", "esfw86.bin"],
            "0x04b8:0x0130"     : ["iscan-plugin-gt-x770", "libesint7C", "esfw7C.bin"],
            # Not supported with iscan >= 2.11.x
            # http://avasys.jp/eng/linux_driver/faq/id000591.php
            #"0x04b8:0x0121"     : ["iscan-plugin-gt-f500", "", ""],
            #"0x04b8:0x0122"     : ["iscan-plugin-gt-f520", "", ""],
            #"0x04b8:0x0118"     : ["iscan-plugin-gt-f600", "", ""],
            #"0x04b8:0x010f"     : ["iscan-plugin-gt-7200", "", ""],
            #"0x04b8:0x011d"     : ["iscan-plugin-gt-7300", "", ""],
            #"0x04b8:0x0116"     : ["iscan-plugin-gt-9400", "", ""],
            "0x04b8:0x0119"     : ["iscan-plugin-gt-x750", "libesint54", "esfw54.bin"],
            "0x04b8:0x012f"     : ["iscan-plugin-gt-f700", "libesint68", "esfw68.bin"],
            "0x04b8:0x013a"     : ["iscan-plugin-gt-x820", "libesintA1", "esfwA1.bin"],
            "0x04b8:0x012d"     : ["iscan-plugin-gt-s600", "libesint66", "esfw66.bin"],
            "0x04b8:0x012e"     : ["iscan-plugin-gt-f670", "libesint7A", "esfw7A.bin"],
            # gt-s50 is shipped with gt-s80 tarball, both without binary blobs
            "0x04b8:0x0136"     : ["esci-interpreter-gt-s80", "libesci-interpreter-gt-s80", ""],
            "0x04b8:0x0137"     : ["esci-interpreter-gt-s50", "libesci-interpreter-gt-s50", ""],
            "0x04b8:0x0131"     : ["esci-interpreter-gt-f720", "libesci-interpreter-gt-f720", "esfw8b.bin"],
            "0x04b8:0x0142"     : ["esci-interpreter-perfection-v330", "libesci-interpreter-perfection-v330", "esfwad.bin"],
          }

# Register the scanners which requires plugins
for key, value in FW_DATA.items():
    vid,pid = key.split(":")
    fwpath = None

    # /usr/lib/{iscan,esci} decision
    libpath = os.path.join("/usr/lib/%s" % value[0].split("-")[0], value[1])

    # /usr/share/{iscan,esci} decision
    if value[2]:
        fwpath = os.path.join("/usr/share/%s" % value[0].split("-")[0], value[2])

    actual_cmd = "interpreter usb %s %s %s" % (vid, pid, libpath)

    if fwpath:
        actual_cmd = "%s %s" % (actual_cmd, fwpath)

    print actual_cmd
