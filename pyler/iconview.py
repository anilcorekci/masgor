#!/usr/bin/python
# -*- coding: utf-8 -*- 
from gi.repository import GdkPixbuf as gdkpixbuf
from gi.repository import Gtk  as gtk
from gi.repository import Gdk  as gdk
import os,mimetypes


home = os.environ["HOME"].strip("\n")
class iconview(gtk.ScrolledWindow):
        def __init__(self):
                gtk.ScrolledWindow.__init__(self)
                self.store = gtk.ListStore( str,gdkpixbuf.Pixbuf,bool)
                self.store.set_sort_column_id(0, gtk.SortType.ASCENDING)
                self.iconview = gtk.IconView(self.store)
                self.iconview.set_selection_mode(gtk.SelectionMode.MULTIPLE)
                self.iconview.connect("item-activated", self.on_item_activated)
#                self.iconview.set_text_column(0)		
                self.iconview.set_pixbuf_column(1)		
                self.iconview.connect_object("button-press-event", self.button_press, self.menu(["Open","Selecet All","Delete"]) )
                self.iconview.connect_object("motion-notify-event",self.monotify,self.iconview)
                self.sozluk = {}
                self.hata = [] 
                
 		self.ac(home+"/.cache/masgor")
                self.iconview.set_selection_mode(gtk.SelectionMode.MULTIPLE)      
                self.iconview.grab_focus()
 
                self.label = gtk.Label()
 
                self.set_policy(gtk.PolicyType.AUTOMATIC, gtk.PolicyType.AUTOMATIC)
                self.add(self.iconview)
 
 
        def monotify(self, iv, event) :
                pos = iv.get_path_at_pos(int(event.x), int(event.y))
                if pos:
                        data =  self.store[pos] [0]
                        tip  = "<b>" +  str(data) + "</b>\n<i>" +mimetypes.guess_type(self.sozluk[data])[0] + "</i>\nFile Path: " + self.sozluk[data]
                        self.iconview.set_tooltip_markup(tip)
                else:
                        self.iconview.set_tooltip_markup("")
 	def ac(self,filename):
 		i=0
                while True:
                        i+=1
                        resim = self.oku(filename,i)
                        if not resim:
                                break
                        self.get_icon(resim)
        def far(self,data):
		dialog = gtk.FileChooserDialog("ImageListFile Path..",
                                       				 None,
                                       				 gtk.FileChooserAction.SAVE,
                                      				 (gtk.STOCK_CANCEL, gtk.ResponseType.CANCEL,
                                       				 gtk.STOCK_OK, gtk.ResponseType.OK))	
                dialog.set_default_response(gtk.ResponseType.OK)
	        response = dialog.run()   	
	        if response == gtk.ResponseType.OK:
		        bilgi = dialog.get_filename()
		        self.iconview.select_all()
		        item = self.iconview.get_selected_items()
		        os.system("> '"+bilgi + "'") 
		        for x in item:
		                path = self.store[x][0]
		                os.system("echo '"+ self.sozluk[path] + "'|tee -a '"+ bilgi + "'") 
			self.iconview.unselect_all()         		        
			dialog.destroy()                                                 
	        else:
		        dialog.destroy()                            
        def open(self,data):
		dialog = gtk.FileChooserDialog("ImageListFile Path..",
                                       				 None,
                                       				 gtk.FileChooserAction.OPEN,
                                      				 (gtk.STOCK_CANCEL, gtk.ResponseType.CANCEL,
                                       				 gtk.STOCK_OK, gtk.ResponseType.OK))	
                dialog.set_default_response(gtk.ResponseType.OK)
	        response = dialog.run()   	
	        if response == gtk.ResponseType.OK:
	        	self.iconview.select_all()
	        	self.remove(1)
		        bilgi = dialog.get_filename()
 			self.ac(bilgi)	 
                        name = os.path.basename(bilgi)
 			self.label.set_text(name)
                        dialog.destroy()    
                        self.hatt()                  
	        else:
		        dialog.destroy() ; self.label.set_text("")        
 
        def save_(self,data) :
                self.iconview.select_all()
                item = self.iconview.get_selected_items()
                os.system("> "+ home+"/.cache/masgor") 
                for x in item:
                        path = self.store[x][0]
                        os.system("echo '"+ self.sozluk[path] + "'|tee -a "+home+"/.cache/masgor") 
                self.iconview.unselect_all()    
                self.label.set_text("")                 

        def oku(self,dosya,no):
	        dosya = open(dosya,"r")
                for i in range(no):
                        name = dosya.readline().strip('\n')
                dosya.close()	 
                if name == "":
                        return False
                else:
                        return name 
        def get_icon(self, filename):
                try:
                        pix = gdkpixbuf.Pixbuf.new_from_file_at_size( filename,148,148)	
                except Exception:
                        self.hata.append(filename)
                else:        
                        name = os.path.basename(filename)
                        self.sozluk[str(name)] = str(filename)
                        self.store.append([str(name), pix, False])             
        def on_item_activated(self, widget,item):
                model = widget.get_model()
                path = model[item][0]
                os.system("xdg-open '" + self.sozluk[path] +"'  & " )  
        def remove(self,data):  
                model = self.iconview.get_model()
                item = self.iconview.get_selected_items()
                for x in item:
                        iter = model.get_iter(x)
                        model.remove(iter)
        def ekle(self,  data):
                dialog = gtk.FileChooserDialog("Select image files..",
                                       				 None,
                                       				 gtk.FileChooserAction.OPEN,
                                      				 (gtk.STOCK_CANCEL, gtk.ResponseType.CANCEL,
                                       				 gtk.STOCK_OK, gtk.ResponseType.OK))	
                dialog.set_default_response(gtk.ResponseType.OK)
	        filter = gtk.FileFilter()
	        filter.set_name("Pictures")
	        resim = ["*jpg","*jpeg","*png","*svg"]
                for x in resim:
	                filter.add_pattern(x)
	        dialog.set_select_multiple(True)
	        dialog.add_filter(filter)
	        response = dialog.run()   	
	        if response == gtk.ResponseType.OK:
		        bilgi = dialog.get_filenames()
		        for x in bilgi:
		                self.get_icon(x)	 
                        dialog.destroy()           
                        self.hatt()
	        else:
		        dialog.destroy()     
                self.label.set_text("") 
        def hatt(self):
                try:
                        if bool(self.hata[0]) == True:
                                i = str(self.hata) ; lis = {",":"\n","[":"","]":""}
                                for x in lis:i = i.replace(x,lis[x])
                                self.mesaj("\nglib.GError: Unknown image file..\n file/files cannot open..\n\n" + i   )     
                                self.hata = []
                except IndexError:
                        pass                                       
	def mesaj(self,msj):
                dialog = gtk.Window()
                dialog.set_modal(True)
                dialog.set_title("Error!!")  
		dialog.set_type_hint(gdk.WindowType.TOPLEVEL)         
                view = gtk.TextView()
                view.get_buffer().set_text(msj)
                view.set_editable(False)
                sw = gtk.ScrolledWindow()
                sw.add(view)
                sw.set_policy(gtk.PolicyType.AUTOMATIC, gtk.PolicyType.AUTOMATIC)
                dialog.add(sw)
                pixbuf =  gdkpixbuf.Pixbuf.new_from_file_at_size("./gtk-cancel.png",88,88)
                buffer = view.get_buffer()
                iter = buffer.get_iter_at_offset(0)
                buffer.insert_pixbuf(iter, pixbuf)
                tag = buffer.create_tag( foreground="white",
                                                     paragraph_background="#7F3731",
                                                     size_points=11.0,
                                                     wrap_mode=gtk.WrapMode.CHAR )
                s, e = buffer.get_bounds()
                buffer.apply_tag(tag, s,e )
                dialog.set_size_request(400,200)
                dialog.set_resizable(False)
                dialog.show_all()
	                              
        def menu(self,item):         
                menu = gtk.Menu()
                for x in item:
                    menu_items = gtk.MenuItem(x)   
	            menu.append(menu_items)
	            menu_items.connect("activate", self.menuitem_response, x)
                    menu_items.show()
         	return menu
        def button_press(self, widget, event):
		if event.button == 3:
			widget.popup(None, None, None , None ,event.button, event.time)  
			return True
		else:
			return False
                	
        def menuitem_response(self, widget, string):
	        lang= "%s" % string
                if lang == "Delete":
		        self.remove(1)
	        elif lang == "Selecet All":
                        self.iconview.select_all()
                elif lang == "Open":
                        for x in self.iconview.get_selected_items():
                                self.on_item_activated(self.iconview,x)
