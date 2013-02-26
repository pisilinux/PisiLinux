/*
 * Simple event sound player through libcanberra
 *
 * Ozan Çağlayan <ozan_at_pardus.org.tr>
 * Fatih Aşıcı <fatih_at_pardus.org.tr>
 *
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation; either version 2 of the License, or (at your
 * option) any later version. Please read the COPYING file.
 *
 * */

#include <stdio.h>

#include <glib.h>
#include <canberra.h>

static int ret = 0;
static ca_proplist *proplist = NULL;
static ca_context *ccontext = NULL;
static GMainLoop* mainloop = NULL;


static void error(int line, int errno) {
    fprintf(stderr, "error %s at line %d\n", ca_strerror(errno), line);
}

static void callback(ca_context *c, uint32_t id, int errno, void *userdata) {
    if (errno < 0) {
        error(__LINE__, errno);
        ret = 1;
    }

    g_main_loop_quit(mainloop);
}

int main(int argc, char *argv[]) {

    if (argc < 2) {
        fprintf(stdout, "Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    /* Initialize threading system */
    g_thread_init(NULL);

    /* Create mainloop */
    mainloop = g_main_loop_new(NULL, FALSE);

    /* Create context */
    if ((ret = ca_context_create(&ccontext)) < 0)
        error(__LINE__-1, ret);

    /* Allocate proplist */
    if ((ret = ca_proplist_create(&proplist)) < 0)
        error(__LINE__-1, ret);

    /* Set application data */
    ca_context_change_props(ccontext,
                            CA_PROP_APPLICATION_NAME, "canberra-event-play",
                            CA_PROP_APPLICATION_ID, "tr.org.pardus.CanberraEventPlay", NULL);

    /* Set properties */
    ca_proplist_sets(proplist, CA_PROP_MEDIA_FILENAME, argv[1]);
    ca_proplist_sets(proplist, CA_PROP_CANBERRA_CACHE_CONTROL, "volatile");
    ca_proplist_sets(proplist, CA_PROP_MEDIA_ROLE, "event");


    if ((ret = ca_context_play_full(ccontext, 1, proplist, callback, NULL)) < 0)
        error(__LINE__-1, ret);

    /* Run the mainloop */
    g_main_loop_run(mainloop);

    /* Cleanup */
    ca_proplist_destroy(proplist);
    ca_context_destroy(ccontext);

    /* Return */
    return ret;
}
