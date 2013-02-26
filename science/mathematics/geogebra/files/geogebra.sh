#!/bin/sh
# simple script to start GeoGebra

func_usage()
{
cat << _USAGE
Usage: geogebra [Java-options] [GeoGebra-options] [FILE]

GeoGebra - Dynamic mathematics software

Java options:
  -Xms<size>                       set initial Java heap size
  -Xmx<size>                       set maximum Java heap size

GeoGebra options:
  --help                           print this help message
  --language=<iso_code>            set language using locale code, e.g. en, de_AT
  --showAlgebraInput=<boolean>     show/hide algebra input field
  --showAlgebraWindow=<boolean>    show/hide algebra window
  --showSpreadsheet=<boolean>      show/hide spreadsheet
  --fontSize=<number>              set default font size
  --enableUndo=<boolean>           enable/disable Undo
_USAGE
}

# check for option --help and pass memory options to Java, others to GeoGebra
for i in "$@"; do
	case "$i" in
	--help | --hel | --he | --h )
		func_usage; exit 0 ;;
	esac
	if [ $(expr match "$i" ".*-Xm") -eq 0 ]; then
		if [ $(expr match "$i" ".*--") -eq 0 ]; then
			GGB_PATH="$i"
		else
			if [ -z "$GG_OPTS" ]; then
				GG_OPTS="$i"
			else
				GG_OPTS="$GG_OPTS $i"
			fi
		fi
	else
		if [ -z "$JAVA_OPTS" ]; then
			JAVA_OPTS="$i"
		else
			JAVA_OPTS="$JAVA_OPTS $i"
		fi
	fi
done

# if memory not set, change to GeoGebra defaults
if [ $(expr match "$JAVA_OPTS" ".*-Xmx") -eq 0 ]; then
	JAVA_OPTS="$JAVA_OPTS -Xmx512m"
fi

if [ $(expr match "$JAVA_OPTS" ".*-Xms") -eq 0 ]; then
	JAVA_OPTS="$JAVA_OPTS -Xms32m"
fi

# run
if [ -z "$GGB_PATH" ]; then
	exec java $JAVA_OPTS -jar /usr/share/java/geogebra/geogebra.jar --showSplash=false $GG_OPTS
else
	exec java $JAVA_OPTS -jar /usr/share/java/geogebra/geogebra.jar --showSplash=false $GG_OPTS "$GGB_PATH"
fi