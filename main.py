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

from datetime import date
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
		self.msg = gtk.Label() # TextView das mensagens
		self.field = gtk.Entry() # input do nome
		self.submit_bt = gtk.Button("Enviar") # botão de enviar
		self.reset_bt = gtk.Button("Limpar") # botão de limpar os campos
		self.view_bt = gtk.Button("Ver Cadastrados") # botão que vizualisa todos os clientes cadastrados
		
		# cria os boxes horizontais
		self.boxTop = gtk.HBox() # box superior que contém o titulo
		self.boxMid = gtk.HBox() # box do meio que contém o campo a ser preenchido
		self.boxBottom = gtk.HBox() # box inferior que contém o botão de enviar
		self.boxMsg = gtk.HBox() # box de mensagens
		
		# adiciona os conteudos as boxes horizontais
		self.boxTop.pack_start(self.rotulo)
		self.boxMid.pack_start(self.label)
		self.boxMid.pack_start(self.field)
		self.boxBottom.pack_start(self.submit_bt)
		self.boxBottom.pack_start(self.reset_bt)
		self.boxBottom.pack_start(self.view_bt)
		self.boxMsg.pack_start(self.msg)
		
		# cria box vertical
		self.body = gtk.VBox()
		
		# adiciona o conteudo a box vertical
		self.body.pack_start(self.boxTop)
		self.body.pack_start(self.boxMid)
		self.body.pack_start(self.boxBottom)
		self.body.pack_start(self.boxMsg)
		
		# adiciona triggers
		self.submit_bt.connect('clicked', self.submitForm) # linka o click no botão submit a função de enviar o form
		self.reset_bt.connect('clicked', self.clearForm) # linka o click no botão de reset a função que limpa o form
		self.view_bt.connect('clicked', self.viewAll) # linka o click no botão de viewAll a função que vizualiza todos os cadastrados
		
		# adiciona body na janela
		self.janela.add(self.body)
		self.janela.show_all()
		
	def viewAll(self, arg2):
		"""
			Função que vizualiza todos os cadastrados no arquivo
			listaClientes.txt
			
			@param:
				self = Objeto GTK.Window
				arg2 = UNDEFINED!!! #TODO : descobrir o que é o segundo argumento
		"""
		data = open("listaClientes.txt", "r")
		self.setMsg(data.read())
	
	def clearForm(self, arg2):
		"""
			Função que limpa os campos do form
			
			@param:
				self = Objeto SELF
				arg2 = UNDEFINED!!! #TODO : descobrir o que é o segundo argumento
			
			#TODO : fazer de modo que eu não precise definir o nome de cada campo
		"""
		self.field.set_text("")
		self.msg.set_text("")
	
	def submitForm(self, arg2):
		"""
			Função que envia o formulário preenchido na main panel
			
			@param:
				self = Objeto GTK.Window
				arg2 = UNDEFINED!!! #TODO : descobrir o que é o segundo argumento
		"""
		hoje = date.today()
		data = self.field.get_text()
		
		if data != "":
			texto = "Cliente %s adicionado no dia %s \n" % (data, hoje)
			self.setMsg(texto)
			
			with open("listaClientes.txt" , "a") as arq:
				arq.write(texto)
				arq.close
			
		else:
			self.setMsg("Por favor, digite o nome do cliente")
			
	def setMsg(self, msg):
		"""
			Função que exibe as mensagens do programa numa box
			
			@param:
				self = Objeto GTK.Window
				msg = Mensagem a ser exibida
		"""
		self.msg.set_text(msg)


panel = mainPanel() # chama a class
gtk.main() # inicia o GTK
