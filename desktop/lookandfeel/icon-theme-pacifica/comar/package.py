#/usr/bin/python

import os
import re

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("chmod 755 /usr/share/icons/Pacifica/16x16")
    os.system("chmod 755 /usr/share/icons/Pacifica/22x22")
    os.system("chmod 755 /usr/share/icons/Pacifica/24x24")
    os.system("chmod 755 /usr/share/icons/Pacifica/32x32")
    os.system("chmod 755 /usr/share/icons/Pacifica/48x48")
    os.system("chmod 755 /usr/share/icons/Pacifica/64x64")
    os.system("chmod 755 /usr/share/icons/Pacifica/96x96")
    os.system("chmod 755 /usr/share/icons/Pacifica/256x256")
    os.system("chmod 755 /usr/share/icons/Pacifica/scalable")
    

    os.system("chown -R root:root /usr/share/icons/Pacifica") 
