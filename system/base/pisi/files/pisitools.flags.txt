for managing CFLAGS, CXXFLAGS and LDFLAGS you can use pisitools
for CFLAGGS -> pisitools.cflags
for LDFLAGGS -> pisitools.ldflags
for CXXFLAGGS -> pisitools.cxxflags
for both CFLAGGS and CXXFLAGS -> pisitools.flags

available operations:

add("param1", "param2", ..., "paramN")
e.g.
pisitools.cxxflags.add("-fpermisive")
  -> shelltools.export("CXXFLAGS", "%s -fpermisive" % get.CXXFLAGS())
pisitools.flags.add("-fno-strict-aliasing", "-fPIC")
  -> shelltools.export("CFLAGS", "%s -fno-strict-aliasing -fPIC" % get.CFLAGS())
  -> shelltools.export("CXXFLAGS", "%s -ffno-strict-aliasing -fPIC" % get.CXXFLAGS())

remove("param1", "param2", ..., "paramN")
e.g.
pisitools.cflags.remove("-fno-strict-aliasing")
  -> shelltools.export("CFLAGS", get.CFLAGS().replace("-fno-strict-aliasing", ""))

replace("old value", "new value")
e.g.
pisitools.cflags.replace("-O2", "-O3")
  -> shelltools.export("CFLAGS", get.CFLAGS().replace("-O2", "-O3"))

sub(pattern, repl, count, flags)
works like re.sub(pattern, repl, string, count, flags) for specified flags
e.g.
pisitools.cflags.replace("-O\d", "-Os")
  -> import re
  -> shelltools.export("CFLAGS", re.sub("-O\d", "-Os", get.CFLAGS()))
