
#!/usr/bin/python

#Created For PisiLinux

from pisi.actionsapi import shelltools, get, cmaketools, pisitools


def setup():
    cmaketools.configure()


def build():
    cmaketools.make()


def install():
    cmaketools.rawInstall("DESTDIR=" + get.installDIR())
    pisitools.dodoc("changelog", "LICENSE", "README")
