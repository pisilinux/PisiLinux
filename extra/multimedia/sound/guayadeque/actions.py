
#!/usr/bin/python

#Created For PisiLinux

from pisi.actionsapi import shelltools, get, cmaketools, pisitools


def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release \
                          -DwxWidgets_CONFIG_EXECUTABLE=/usr/bin/wxconfig \
                          -DwxWidgets_wxrc_EXECUTABLE=/usr/bin/wxrc", installPrefix="/usr")


def build():
    cmaketools.make()


def install():
    cmaketools.rawInstall("DESTDIR=" + get.installDIR())
    pisitools.dodoc("changelog", "LICENSE", "README")
