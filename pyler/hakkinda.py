#!/usr/bin/python
# -*- coding: utf-8 -*- 
from gi.repository import GdkPixbuf as gdkpixbuf
from gi.repository import Gtk  as gtk
def hakkinda():
	hakkinda = gtk.AboutDialog()	
	hakkinda.set_title("Masgor ")
	hakkinda.set_program_name("masgor")
	hakkinda.set_version(versiyon) 
	hakkinda.set_copyright(kim)
	hakkinda.set_icon_from_file("./masgor.svg")
	hakkinda.set_license(lisans)
	hakkinda.set_website(site)
	hakkinda.set_authors(mail)
	logo = gdkpixbuf.Pixbuf.new_from_file_at_size("./masgor.svg", 148, 148)
	hakkinda.set_logo(logo)	
	
	hakkinda.show_all()
	if  hakkinda.run() == gtk.ResponseType.CANCEL:     
		hakkinda.destroy()
lisans="""
Masgor özgür bir yazılımdır, onu Özgür Yazılım
Vakfı'nın yayınladığı GNU Genel Kamu Lisansı'nın 2.
sürümü veya (tercihinize bağlı) daha sonraki sürümleri
altında dağıtabilir ve/veya değiştirebilirsiniz.


Masgor  faydalı olacağı umut edilerek dağıtılmaktadır,
fakat HİÇBİR GARANTİSİ YOKTUR; hatta ÜRÜN DEĞERİ
ya da BİR AMACA UYGUNLUK gibi garantiler de
vermez. Lütfen GNU Genel Kamu Lisansı'nı daha fazla
ayrıntı için inceleyin.


"""

mail=["Anıl Çörekcioğlu  <anilcorekci@gmail.com>"]


kim="copyright© hitokiri"

versiyon="1.0"

site="https://launchpad.net/masgor"
