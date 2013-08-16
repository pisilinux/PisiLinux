Index: funguloids/sed.sh
===================================================================
--- /dev/null
+++ funguloids/sed.sh
@@ -0,0 +1,15 @@
+#!/bin/bash
+ sed -i -e 's;cp bootstrap.mpk "@gameinstalldir@";cp bootstrap.mpk "$(DESTDIR)@gameinstalldir@";' -e 's;funguloids.mpk "@gameinstalldir@";funguloids.mpk "$(DESTDIR)@gameinstalldir@";' bin/Makefile.in
+ sed -i -e 's;cp MarylandInMay.ogg "@musicinstalldir@";cp MarylandInMay.ogg "$(DESTDIR)@musicinstalldir@";' bin/music/Makefile.in
+ sed -i -e 's;-llua5.1;-llua;' -e 's;share/games/funguloids;share/funguloids;' \
+  	-e 's;bininstalldir="${prefix}/games;bininstalldir="${prefix}/bin;' configure.ac
+
+chmod +x ./mpak.py
+  ./mpak.py -e -f bin/bootstrap.mpk -p _bootstrap 
+  ./mpak.py -e -f bin/funguloids.mpk -p _gamedata 
+  sed -ri '/^[A-Z]/ s/(.*)/overlay \1/' _bootstrap/*.overlay _gamedata/*.overlay
+  sed -ri '/^[A-Z]/ s/(.*)/particle_system \1/' _gamedata/*.particle
+  sed -ri 's/^(\t\t\t)(texture_unit) 1/\1\2\n\1{\n\1}\n\1\2/' _gamedata/materials.material
+  ./mpak.py -c -f bin/bootstrap.mpk _bootstrap/* 
+  ./mpak.py -c -f bin/funguloids.mpk _gamedata/* 
+  rm -rf _bootstrap _gamedata
