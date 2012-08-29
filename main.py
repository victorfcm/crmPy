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
import gtk.glade
import conexao

class mainPanel():
	"""
		Cria a janela principal da aplicação.
	"""
	version = '0.1'
	
	def __init__(self):
		"""
			Função construct que cria a janela principal e seus widgets
		"""
		self.gladefile = "crmpy.glade" 
		self.glade = gtk.Builder()
		self.glade.add_from_file(self.gladefile)
		
		# Dicionário das triggers5
		dic = { 
			"submit_bt_clicked" : self.submitForm, 
			"reset_bt_clicked" : self.clearForm, 
			"view_bt_clicked" : self.viewAll 
		}
		
		self.glade.connect_signals(dic)
		self.glade.get_object("MainWindow").show_all()
		
		
	def viewAll(self, arg2):
		"""
			Função que vizualiza todos os cadastrados no banco
			
			@param:
				self = Objeto GTK.Window
				arg2 = UNDEFINED!!! #TODO : descobrir o que é o segundo argumento
		"""
		texto = "Clientes : \n"
		conexao.db.execute('SELECT * FROM cliente')
		clientes = conexao.db.fetchall()
		for cliente in clientes:
			texto += cliente[1]+"\n"
		
		self.setMsg(texto)
	
	def clearForm(self, arg2):
		"""
			Função que limpa os campos do form
			
			@param:
				self = Objeto SELF
				arg2 = UNDEFINED!!! #TODO : descobrir o que é o segundo argumento
			
			#TODO : fazer de modo que eu não precise definir o nome de cada campo
		"""
		self.glade.get_object('nome').set_text("")
		self.glade.get_object('msg').set_text("")
		
	def submitForm(self, arg2):
		"""
			Função que envia o formulário preenchido na main panel
			
			@param:
				self = Objeto GTK.Window
				arg2 = UNDEFINED!!! #TODO : descobrir o que é o segundo argumento
		"""
		data = date.today()
		nome = self.glade.get_object("nome").get_text()
		
		if nome:
			texto = "Cliente %s adicionado no dia %s \n" % (nome, data)
			self.setMsg(texto)
			
			try:
				conexao.db.execute("INSERT INTO cliente (nome) VALUES ('%s')" % nome)
				conexao.con.commit()
			except:
				conexao.con.rollback()
				self.setMsg('Erro no SQL, por favor, verifique as configurações');
			
		else:
			self.setMsg("Por favor, digite o nome do cliente")
			
	def setMsg(self, msg):
		"""
			Função que exibe as mensagens do programa numa box
			
			@param:
				self = Objeto GTK.Window
				msg = Mensagem a ser exibida
		"""
		self.glade.get_object('msg').set_text(msg)


if __name__ == "__main__":
	panel = mainPanel() # chama a class
	gtk.main() # inicia o GTK
