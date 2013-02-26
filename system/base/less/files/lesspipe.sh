#!/bin/sh
#
# To use this filter with less, define LESSOPEN:
# export LESSOPEN="|/usr/bin/lesspipe.sh %s"
#
# The script should return zero if the output was valid and non-zero
# otherwise, so less could detect even a valid empty output
# (for example while uncompressing gzipped empty file).
# For backward-compatibility, this is not required by default. To turn
# this functionality there should be another vertical bar (|) straight
# after the first one in the LESSOPEN environment variable:
# export LESSOPEN="||/usr/bin/lesspipe.sh %s"

if [ ! -e "$1" ] ; then
	exit 1
fi

if [ -d "$1" ] ; then
	ls -alF -- "$1"
	exit $?
fi

exec 2>/dev/null

case "$1" in
*.[1-9n].bz2|*.[1-9]x.bz2|*.man.bz2|*.[1-9n].[gx]z|*.[1-9]x.[gx]z|*.man.[gx]z|*.[1-9n].lzma|*.[1-9]x.lzma|*.man.lzma)
	case "$1" in
	*.gz)		DECOMPRESSOR="gzip -dc" ;;
	*.bz2)		DECOMPRESSOR="bzip2 -dc" ;;
	*.xz|*.lzma)	DECOMPRESSOR="xz -dc" ;;
	esac
	if [ -n "$DECOMPRESSOR" ] && $DECOMPRESSOR -- "$1" | file - | grep -q troff; then
		$DECOMPRESSOR -- "$1" | groff -Tascii -mandoc -
		exit $?
	fi ;;&
*.[1-9n]|*.[1-9]x|*.man)
	if file "$1" | grep -q troff; then
		man -l "$1" | cat -s
		exit $?
	fi ;;&
*.tar) tar tvvf "$1" ;;
*.tgz|*.tar.gz|*.tar.[zZ]) tar tzvvf "$1" ;;
*.tar.xz) tar Jtvvf "$1" ;;
*.xz|*.lzma) xz -dc -- "$1" ;;
*.tar.bz2|*.tbz2) bzip2 -dc -- "$1" | tar tvvf - ;;
*.[zZ]|*.gz) gzip -dc -- "$1" ;;
*.bz2) bzip2 -dc -- "$1" ;;
*.zip|*.jar|*.nbm) zipinfo -- "$1" ;;
*.rpm) rpm -qpivl --changelog -- "$1" ;;
*.cpi|*.cpio) cpio -itv < "$1" ;;
*.gif|*.jpeg|*.jpg|*.pcd|*.png|*.tga|*.tiff|*.tif)
	if [ -x /usr/bin/identify ]; then
		identify "$1"
	elif [ -x /usr/bin/gm ]; then
		gm identify "$1"
	else
		echo "No identify available"
		echo "Install ImageMagick or GraphicsMagick to browse images"
		exit 1
	fi ;;
*)
	if [ -x /usr/bin/file ] && [ -x /usr/bin/iconv ] && [ -x /usr/bin/cut ]; then
		case `file -b "$1"` in
		*UTF-16*) conv='UTF-16' ;;
		*UTF-32*) conv='UTF-32' ;;
		esac
		if [ -n "$conv" ]; then
			env=`echo $LANG | cut -d. -f2`
			if [ -n "$env" -a "$conv" != "$env" ]; then
				iconv -f $conv -t $env "$1"
				exit $?
			fi
		fi
	fi
	exit 1
esac
exit $?

