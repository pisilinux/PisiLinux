#!/usr/bin/env python
import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
	# For every package that ships GSettings schemas, we must recompile
	# the system's schemas
	os.system ("glib-compile-schemas /usr/share/glib-2.0/schemas")
	
