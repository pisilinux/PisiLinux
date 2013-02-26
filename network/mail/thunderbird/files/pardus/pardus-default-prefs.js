pref("mail.content_disposition_type", 1);
pref("mail.shell.checkDefaultClient", false);

// Enable threaded view by default and always sort by date
pref("mailnews.default_sort_type", 18); // By date
pref("mailnews.default_sort_order", 1); // Ascending
pref("mailnews.default_view_flags", 1); // ThreadedView

// Check all folders for new e-mails by default
pref("mail.check_all_imap_folders_for_new", true);

pref("mail.compose.max_recycled_windows", 1);
pref("browser.display.show_image_placeholders", false);
pref("mailnews.customHeaders", "List-Id");

// Fill user-agent informations during build
pref("general.useragent.vendor", "DISTRIB_ID");
pref("general.useragent.vendorSub", "DISTRIB_RELEASE");

// Disable global indexing by default as it slows down Thunderbird a lot
pref("mailnews.database.global.indexer.enabled", false);

// Change the default sound to a shipped .wav file and disable the sound by default
pref("mail.biff.play_sound", "false");
pref("mail.biff.play_sound_type", "1");
pref("mail.biff.play_sound.url", "file://usr/lib/MozillaThunderbird/sound.wav");

pref("font.name.monospace.null", "DejaVu Sans Mono");
pref("font.name.monospace.tr", "DejaVu Sans Mono");
pref("font.name.monospace.x-central-euro", "DejaVu Sans Mono");
pref("font.name.monospace.x-unicode", "DejaVu Sans Mono");
pref("font.name.monospace.x-user-def", "DejaVu Sans Mono");
pref("font.name.monospace.x-western", "DejaVu Sans Mono");
pref("font.name.sans-serif.null", "DejaVu Sans");
pref("font.name.sans-serif.tr", "DejaVu Sans");
pref("font.name.sans-serif.x-central-euro", "DejaVu Sans");
pref("font.name.sans-serif.x-unicode", "DejaVu Sans");
pref("font.name.sans-serif.x-user-def", "DejaVu Sans");
pref("font.name.sans-serif.x-western", "DejaVu Sans");
pref("font.name.serif.tr", "DejaVu Sans");
pref("font.name.serif.x-central-euro", "DejaVu Sans");
pref("font.name.serif.x-unicode", "DejaVu Sans");
pref("font.name.serif.x-user-def", "DejaVu Sans");
pref("font.name.serif.x-western", "DejaVu Sans");
pref("font.minimum-size.null", 12);
pref("font.minimum-size.x-central-euro", 12);
pref("font.minimum-size.x-unicode", 12);
pref("font.minimum-size.x-user-def", 12);
pref("font.minimum-size.x-western", 12);
pref("font.minimum-size.tr", 12);
pref("font.size.fixed.null", 12);
pref("font.size.variable.x-unicode", 12);
pref("font.size.variable.null", 12);
pref("font.size.variable.x-western", 12);
pref("font.size.variable.tr", 12);
pref("print.print_edge_top", 14); // 1/100 of an inch
pref("print.print_edge_left", 16); // 1/100 of an inch
pref("print.print_edge_right", 16); // 1/100 of an inch
pref("print.print_edge_bottom", 14); // 1/100 of an inch
pref("intl.locale.matchOS", true);
