# -*- coding: utf-8 -*- 
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
import iconview
import conf 

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
		

		self.basla = builder.get_object("checkbutton1")
		self.basla.connect("toggled",self.che,"basla",False)
		self.ras = builder.get_object("checkbutton5")
		self.ras.connect("toggled",self.che,"rastgele",False)
		
		hbox = builder.get_object("hbox1") 
		vbox = builder.get_object("vbox1")

		buton = gtk.Button("Yardım")
		buton.connect("clicked",
				lambda x: self.mesaj("HELLO WORLD\n Hello again..")	)
		
		hbbox = gtk.HButtonBox()
		hbbox.add(buton)
		buton = gtk.Button(" Kapat")
		buton.connect("clicked",self.ayarver,False)
	 
		hbbox.add(buton)
		vbox.pack_start(hbbox,False,False,0)
		
		
		self.ayar = conf.config("tercihler.cfg")
		
		i=0
		for val in self.ayar.dict_: # order in cfg file matters...
			if "val" in val:
				i+=1
				self.ayar.dict_[val] = [ 
					self.ayar.dict_[val],
					builder.get_object("hscale%s" %(i) ),
					builder.get_object("checkbutton%s" %(i+1) ),
				]
				self.ayar.dict_[val][2].connect(
					"toggled", self.che,
					val.replace("val",""), self.ayar.dict_[val][1]
				)

		self.ayaral()

		self.window.show_all() 

	def mesaj(self,msj):
		dialog = gtk.MessageDialog(type=gtk.MessageType.INFO, buttons=gtk.ButtonsType.OK)
		dialog.set_markup(msj)
		dialog.show()
					 
		if dialog.run() == gtk.ResponseType.OK:
			dialog.destroy()    
		
	def conf(self,key, ing=False): 
		if ing:
			return self.ayar.set_conf("tercihler.cfg",key,ing)
		else:
			return self.ayar._get("tercihler.cfg",key )          
                
	def ayarver(self,w,data):

		for val in self.ayar.dict_:
			if "val" in val:
				self.conf(val,self.ayar.dict_[val][1].get_value() )

		self.window.destroy()

	def che(self,buton,conf,widget):
		self.conf(conf,str(buton.get_active() ))
		if widget:
			if buton.get_active():
				widget.set_sensitive(True)
			else:	
				widget.set_sensitive(False)	

	def check(self,buton,conf):
		ayar = self.conf(conf)
		buton.set_active(eval(ayar))

	def ayaral(self):
		for val in self.ayar.dict_:
			if "val" in val:
				widgets_ = self.conf(val)
				widgets_[1].set_value(float(widgets_[0])) #0 is the value #1 is the hscale # 2 is the checkbutton
				check_value = self.conf(val.replace("val",""))
				widgets_[2].set_active(eval(check_value))

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
