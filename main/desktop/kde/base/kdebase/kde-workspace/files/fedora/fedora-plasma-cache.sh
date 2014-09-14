#!/bin/sh

if [ "`kreadconfig --file fedora-plasma-cacherc --group General --key FirstRun --default true`" = "true" ]; then
  rm -fv "`kde4-config --path cache`/"*.kcache
  rm -fv "`kde4-config --path cache`/"plasma-svgelements-*
  #rm -fv ${XDG_CONFIG_HOME-${HOME}/.config}/Trolltech.conf
  kwriteconfig --file fedora-plasma-cacherc --group General --key FirstRun --type bool false
fi
