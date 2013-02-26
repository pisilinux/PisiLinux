#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# FIXME: Bump this version when needed
perlVersion = "5.12.2"
vendor_lib_path = "/usr/lib/perl5/vendor_perl/%s" % perlVersion

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # Register XML::SAX::PurePerl
    os.system("/usr/bin/perl -MXML::SAX -e 'XML::SAX->add_parser(q(XML::SAX::PurePerl))->save_parsers()' 2>/dev/null")

def preRemove():
    # Unregister XML::SAX::PurePerl
    os.system("/usr/bin/perl -MXML::SAX -e 'XML::SAX->remove_parser(q(XML::SAX::PurePerl))->save_parsers()'")
