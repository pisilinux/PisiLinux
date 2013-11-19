from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def build():
    autotools.make()


def install():
    pisitools.dobin("id3v2")
    pisitools.dobin("id3v2.1")  
