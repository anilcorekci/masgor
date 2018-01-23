#!/usr/bin/python
# -*- coding: utf-8 -*- 
#import gconf
from gi.repository import Gtk as gtk
import os
import iconview
#import conf,gconf

class ayar():
	def __init__(self):
		builder = gtk.Builder()        
		builder.add_from_file("tercihler.glade")	
		self.window = builder.get_object("pencere")
                self.window.connect("delete-event",self.ayarver)
                
 		vbox = builder.get_object("vbox2")
		iconview_ = iconview.iconview() 
		vbox.pack_start(iconview_,True,True,3 )
		
                hbox = gtk.HBox()
                kal = self.rlb( gtk.STOCK_REMOVE ,"Delete ",iconview_.remove,"Delete")
                ekle = self.rlb( gtk.STOCK_ADD ,"Add ",iconview_.ekle,"Add")
		far = self.rlb( gtk.STOCK_SAVE_AS ,"Save As",iconview_.far,"Save As")
                save_ = self.rlb( gtk.STOCK_SAVE ,"Save",iconview_.save_,"Save")
                ac = self.rlb( gtk.STOCK_OPEN ,"Open",iconview_.open,"Open")

                hbox.pack_start(ac,False,True,3); hbox.pack_start(far,False,True,3) 
                hbox.pack_start(save_,False,True,3)

                hbox.pack_start(iconview_.label,True,True,3)
                hbox.pack_start(kal,False,False,3)
                hbox.pack_start(ekle,False,False,3)
                vbox.pack_start(hbox,False,False,3 )
		
		self.sanval = builder.get_object("hscale1")
		self.dakval = builder.get_object("hscale2")
		self.satval = builder.get_object("hscale3")	
		
 		self.saniye =  builder.get_object("checkbutton2")
 		self.saniye.connect("toggled",self.che,"saniye",self.sanval)
 		self.sanval.set_sensitive(False)
		self.dakika =  builder.get_object("checkbutton3")
		self.dakika.connect("toggled",self.che,"dakika",self.dakval)
		self.dakval.set_sensitive(False)
		self.saat =  builder.get_object("checkbutton4")
 		self.saat.connect("toggled",self.che,"saat",self.satval)
 		self.satval.set_sensitive(False)
 
 		self.basla = builder.get_object("checkbutton1")
		self.basla.connect("toggled",self.che,"basla",False)
  		self.ras = builder.get_object("checkbutton5")
		self.ras.connect("toggled",self.che,"rastgele",False)
		
		hbox = builder.get_object("hbox1") 
		vbox = builder.get_object("vbox1")
		buton = gtk.Button("Yardım")
		buton.connect("clicked",self.pes)
		hbbox = gtk.HButtonBox()
		hbbox.add(buton)
		buton = gtk.Button(" Kapat")
		buton.connect("clicked",self.ayarver,False)
	 
		hbbox.add(buton)
		vbox.pack_start(hbbox,False,False,0)
                import conf
                self.ayar = conf.config("tercihler.cfg")
		self.ayaral()
 
		self.window.show_all() 

	def mesaj(self,msj):
		dialog = gtk.MessageDialog()
		dialog.set_markup(msj)
		dialog.show()
					 
		if dialog.run() == gtk.ResponseType.OK:
			dialog.destroy()    
	def pes(self,pes):
	    	self.mesaj("""Biri Buna Basar Demiştim Zaten...
Yardım Almak İçin <a href= "http://forum.ubuntu-tr.net/index.php/topic,18444.90.html" >Ubuntu Türkiye</a> """)	

	def conf(self,key, ing): 
                if ing:
                        return self.ayar.set_conf("tercihler.cfg",key,ing)
                else:
                        return self.ayar._get("tercihler.cfg",key )          
                
	def ayarver(self,w,data):
		self.conf("saatval",str(self.satval.get_value() ))
		self.conf("dakikaval",str(self.dakval.get_value() ))
		self.conf("saniyeval",str(self.sanval.get_value() ))
		self.window.destroy()
	def che(self,buton,conf,widget):
		self.conf(conf,str(buton.get_active() ))
		if widget:
			if buton.get_active():
				widget.set_sensitive(True)
			else:	
				widget.set_sensitive(False)	
	def check(self,buton,conf):
		ayar = self.conf(conf,False)
		if ayar == "True":
			buton.set_active(True)
		elif ayar == "False":
			buton.set_active(False)
	def ayaral(self):
		v1 = self.conf("saniyeval",False)
		self.sanval.set_value(float(v1))
		v2 = self.conf("dakikaval",False)
		self.dakval.set_value(float(v2))
		v3 = self.conf("saatval",False)
		self.satval.set_value(float(v3))
		
		self.check(self.saniye,"saniye")
		self.check(self.dakika,"dakika")
		self.check(self.saat,"saat") 
		self.check(self.basla,"basla")
		self.check(self.ras,"rastgele")
        def rlb(self, stock, label_text,kontak,ed):
                image = gtk.Image()
                image.set_from_stock(stock,2)
                item = gtk.Button()
                hbox = gtk.HBox()
                label = gtk.Label()
                label.set_text(ed)
                hbox.pack_start(image,False,False,3)
                hbox.pack_start(label,False,False,3)
                item.set_relief(gtk.ReliefStyle.NONE)
                item.set_tooltip_text(label_text)
                item.connect('clicked',kontak)
                item.add(hbox)
                item.show_all()
                return item                  
