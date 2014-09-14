#!/bin/bash

## Copyright (C) 2010 Red Hat, Inc.
## Authors:
##  Tim Waugh <twaugh@redhat.com>

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

## Purpose: Update hpcups PPDs when necessary.

sock=/var/run/cups/cups.sock
running=$(LC_ALL=C lpstat -h "$sock" -r 2>/dev/null)
if [ "$?" -ne 0 ]
then
    # No lpstat in path
    exit 0
fi

if [ -z "${running##*not*}" ]
then
    # scheduler is not running
    exit 0
fi

trap 'rm -f "$tmpdir"/models; rmdir "$tmpdir"; exit 0' \
    0 HUP INT QUIT ILL ABRT PIPE TERM

debug=true
tmpdir="$(mktemp -d)"
for ppd in /etc/cups/ppd/*.ppd
do
    [ -r "$ppd" ] || continue
    queue="${ppd#/etc/cups/ppd/}"
    queue="${queue%.ppd}"
    lpstat -h "$sock" -p "$queue" &>/dev/null || continue

    # We have PPD associated with a queue.  Find out its NickName
    $debug && echo "Examining $queue"
    nickname="$(grep '^\*NickName:' "$ppd")"
    nickname="${nickname#*\"}" # strip text up to and incl first double quote
    nickname="${nickname%\"*}" # strip final double quote
    $debug && echo "NickName is: $nickname"

    # Is it an hpcups PPD?
    [ -z "${nickname##*, hpcups*}" ] || continue
    $debug && echo "hpcups: true"

    # No: need to regenerate the PPD.
    if [ ! -f "$tmpdir/models" ]
    then
	# Get list of driver URIs and NickNames
	lpinfo -h "$sock" --include-schemes=drv -m 2>/dev/null >"$tmpdir/models"
    fi

    # Strip hpcups version from NickName
    nickname="${nickname%, hpcups*}"
    $debug && echo "Stripped NickName: $nickname"
    while read line
    do
	uri=${line%% *}
	nn="${line#$uri }"
	[ -z "${nn##*, hpcups*}" ] || continue

	nn="${nn%, hpcups*}"
	if [ "$nn" == "$nickname" ]
	then
	    $debug && echo "Match found, URI: $uri"

	    # Unfortunately CUPS will reset the page size when we
	    # change the PPD, due to the weird page size names that
	    # HPLIP uses.  Try to maintain the existing page size.
	    size="$(grep '^\*DefaultPageSize:' "$ppd")"
	    size="${size##* }" # strip until after first ' '
	    size="${size%% *}" # strip after any ' '
	    $debug && echo "PageSize is $size"

	    if [ -z "${size#*Duplex}" ]
	    then
		# Special handling for duplex sizes because HPLIP
		# broke backwards compatibility with *that* too!
		size="${size%Duplex}.Duplex"
	    fi

	    null=/dev/null
	    $debug && null=/dev/stdout
	    lpadmin -h "$sock" -p "$queue" -m "$uri" &>"$null" || :
	    $debug && echo "PPD regenerated"

	    lpadmin -h "$sock" -p "$queue" -o PageSize="$size" &>"$null" || :
	    $debug && echo "PageSize restored to $size"
	    break
	fi
    done <"$tmpdir/models"
done
exit 0
