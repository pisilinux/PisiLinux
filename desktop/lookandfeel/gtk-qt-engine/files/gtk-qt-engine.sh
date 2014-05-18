kcmgtk=`kde4-config --path module --locate kcm_gtk4.so`

if [ "x$kcmgtk" != "x" ] && [ -f $kcmgtk ]; then
    export SAL_GTK_USE_PIXMAPPAINT=1
fi
