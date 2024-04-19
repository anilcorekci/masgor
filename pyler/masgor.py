#!/usr/bin/env python
#! coding:utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from gi.repository import Gdk as gdk 
from gi.repository import Gtk as gtk
from gi.repository import GdkPixbuf as gdkpixbuf
import os 
USER = os.environ["HOME"].strip("\n")

import tercihler
from hakkinda import hakkinda

 
class area(object):
    def __init__(self):
        self.statusIcon = gtk.StatusIcon()
        pix =  gdkpixbuf.Pixbuf.new_from_file_at_size("./masgor.svg",48,48)
        self.statusIcon.set_from_pixbuf(pix)
        self.statusIcon.set_visible(True)
        self.statusIcon.set_tooltip_text("MASGOR")
      #  print(dir(self.statusIcon))

        self.menu = gtk.Menu()
        
        self.Item = gtk.CheckMenuItem(label="Başlat")
        self.Item.connect('activate',
            lambda *x:
                os.system("./masgor 1 &") if self.Item.get_active()\
                else os.system("killall masgor &"))                           
        
        self.menu.append(self.Item)
        
        self.Item1 = gtk.ImageMenuItem(label=gtk.STOCK_PREFERENCES)
        self.Item1.connect('activate', 
                lambda *x: tercihler.ayar() )           
        self.menu.append(self.Item1)
        
        self.Item3 = gtk.ImageMenuItem(label=gtk.STOCK_ABOUT)
        self.Item3.connect('activate',
                lambda *x: hakkinda() )           
        self.menu.append(self.Item3)
        
        self.Item2 = gtk.ImageMenuItem(label=gtk.STOCK_QUIT)
        self.Item2.connect('activate',
                lambda *x: [os.system("killall masgor &"),\
                gtk.main_quit() ])   
          
        self.menu.append(self.Item2)
 
        self.menu.show_all()

        self.statusIcon.connect('popup-menu', self.popup_menu_cb, self.menu)
        self.statusIcon.set_visible(1)

    def popup_menu_cb(self,w,x,time,data):
  #  self.popup_for_device(None, parent_menu_shell, parent_menu_item, func, data, button, activate_time)
        data.popup(None, None, None, self.statusIcon, 3, time)
        
if __name__ == "__main__":
    area()
    gtk.main()
