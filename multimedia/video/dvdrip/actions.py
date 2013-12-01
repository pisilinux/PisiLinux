#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()
    pisitools.insinto("/usr/share/applications", "dvdrip.desktop")
    pisitools.insinto("/usr/share/pixmaps", "lib/Video/DVDRip/icon.xpm", "dvdrip.xpm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Loader.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Menu.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Image.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Widget.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::GtkWidget.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::CheckButton.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Entry.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::DialogButtons.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Expander.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::VBox.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::VSeparator.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Container.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Intro.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::HBox.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Table.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Window.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Label.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Button.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Popup.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::YesNo.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::ToggleButton.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::VPaned.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::RadioButton.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::List.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Context.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Rules.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::CheckButtonGroup.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::HSeparator.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::ProxyBuffered.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Combo.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Notebook.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Timestamp.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Form.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::TextView.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Layout.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::Proxy.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::ExecFlow.3pm")
    pisitools.remove("/usr/share/man/man3/Gtk2::Ex::FormFactory::ProgressBar.3pm")

    pisitools.dodoc("Changes*", "COPYRIGHT", "Credits", "README", "TODO")
