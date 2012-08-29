#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sem título.py
#  
#  Copyright 2012 VIctor <victor@vfreitas>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade

class HellowWorldGTK:
	
	def __init__(self):
		self.gladefile = "crmpy.glade" 
		self.glade = gtk.Builder()
		self.glade.add_from_file(self.gladefile)
		self.glade.connect_signals(self)
		self.glade.get_object("MainWindow").show_all()

	def on_MainWindow_delete_event(self, widget, event):
		gtk.main_quit()

if __name__ == "__main__":
	a = HellowWorldGTK()
	gtk.main()
