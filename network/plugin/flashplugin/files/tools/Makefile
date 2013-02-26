# Create a custom tarball from original flashplugin archives

package = flashplugin
version = 11.2.202.251
archs = i386 x86_64
archive_name = install_flash_player_11_linux
tarname = $(package)
distdir = $(tarname)-$(version)
tarballdir = $(archs:%=$(distdir)-%)

all: dist
	@echo -e "\nThe files \"$(tarballdir).tar.gz\" are created and ready to distribute"

dist: $(tarballdir)

$(tarballdir): $(archs)
	@echo -e "\n** Creating tarball $@.tar.gz from distdir\n"
	tar -zcvf $@.tar.gz $@
	rm -rf $@

$(archs): distclean
	@echo -e "\n** Creating distdir $(distdir)-$@\n"
	mkdir -p $(distdir)-$@
	tar -zxvf $(archive_name).$@.tar.gz -C $(distdir)-$@
	# Our patched desktop file
	cp ../kcm_adobe_flash_player.desktop  $(distdir)-$@/usr/share/kde4/services/

distclean:
	@echo -e "** Removing old distdir files\n"
	rm -f $(tarballdir:%=%.tar.gz) > /dev/null 2>&1
	rm -rf $(tarballdir) > /dev/null 2>&1

.PHONY: all dist distclean
