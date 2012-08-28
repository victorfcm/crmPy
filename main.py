#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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

import pygtk
import gtk

class mainPanel():
	"""
		Cria a janela principal da aplicação.
	"""
	
	def __init__(self):
		"""
			Função construct que cria a janela principal e seus widgets
		"""
		
		# cria a janela
		self.janela = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.janela.set_title("CRM Py")
		self.janela.set_size_request(400, 200)
		
		# cria os widgets
		self.rotulo = gtk.Label("Bem vindo") # rotulo superior
		self.label = gtk.Label("Nome do cliente: ") # label do campo
		self.field = gtk.Entry() # input do nome
		self.submit_bt = gtk.Button("Enviar.")
		
		# cria os boxes horizontais
		self.boxTop = gtk.HBox()
		self.boxMid = gtk.HBox()
		self.boxBottom = gtk.HBox()
		
		# adiciona os conteudos as boxes horizontais
		self.boxTop.pack_start(self.rotulo)
		self.boxMid.pack_start(self.label)
		self.boxMid.pack_start(self.field)
		self.boxBottom.pack_start(self.submit_bt)
		
		# cria box vertical
		self.body = gtk.VBox()
		
		# adiciona o conteudo a box vertical
		self.body.pack_start(self.boxTop)
		self.body.pack_start(self.boxMid)
		self.body.pack_start(self.boxBottom)
		
		# adiciona triggers
		self.submit_bt.connect('clicked', self.submitForm)
		
		# adiciona body na janela
		self.janela.add(self.body)
		self.janela.show_all()
		
	def submitForm(arg1, arg2):
		data = arg1.field.get_text()
		print "Cliente %s adicionado" % data


panel = mainPanel()
gtk.main()
