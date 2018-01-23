#!/usr/bin/env python
#! coding:utf-8 -*-
from gi.repository import Gtk as gtk
from gi.repository import GdkPixbuf as gdkpixbuf
import os 
USER = os.environ["HOME"].strip("\n")
 
class area(object):
    def __init__(self):
        self.statusIcon = gtk.StatusIcon()
        pix =  gdkpixbuf.Pixbuf.new_from_file_at_size("./masgor.svg",48,48)
        self.statusIcon.set_from_pixbuf(pix)
        self.statusIcon.set_visible(True)
        self.statusIcon.set_tooltip_text("MASGOR")

	self.menu = gtk.Menu()
        
	self.Item = gtk.CheckMenuItem("Başlat",None)
        self.Item.connect('activate', self.komut, self.statusIcon)           
        self.menu.append(self.Item)
        
	self.Item1 = gtk.ImageMenuItem(gtk.STOCK_PREFERENCES)
	self.Item1.connect('activate', self.tercihler, self.statusIcon)           
        self.menu.append(self.Item1)
        
        self.Item3 = gtk.ImageMenuItem(gtk.STOCK_ABOUT)
	self.Item3.connect('activate', self.komut2, self.statusIcon)           
        self.menu.append(self.Item3)
        
        self.Item2 = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        self.Item2.connect('activate', self.komut1, self.statusIcon)           
        self.menu.append(self.Item2)
 
 

        self.menu.show_all()
        self.statusIcon.connect('popup-menu', self.popup_menu_cb, self.menu)
        self.statusIcon.set_visible(1)
    def komut1(self,w,data):
	os.system("killall masgor  &")    
	gtk.main_quit()
    def tercihler(self,w,data):
	import tercihler
	ayar = tercihler.ayar()
    def komut(self,w,data):
    	if self.Item.get_active():
    		os.system("./masgor  1 &")     
	else:
		os.system("killall masgor &")    
    def komut2(self,w,data):
        import hakkinda
        hakkinda.hakkinda()   		
    def popup_menu_cb(self,w,x,time,data):
  #  self.popup_for_device(None, parent_menu_shell, parent_menu_item, func, data, button, activate_time)
        
        data.popup(None, None, None, self.statusIcon, 3, time)
if __name__ == "__main__":
    area()
    gtk.main()
