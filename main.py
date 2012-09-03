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
import pprint

class mainPanel():
	"""
		Cria a janela principal da aplicação.
	"""
	version = '0.1'
	
	def __init__(self):
		"""
			Função construct que cria a janela principal e seus widgets
		"""
		self.gladefile = "crmpy.glade"  # importa o arquivo
		self.glade = gtk.Builder() # chama o builder
		self.glade.add_from_file(self.gladefile) # seta o builder para construir a partir do arquivo importado anteriormente
		
		scrolledwindow = self.glade.get_object("scrolled") # pega a box com barra de rolagem
		scrolledwindow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC) # define que o scroll dela vai ser automático
		
		# Dicionário das triggers
		dic = { 
			"submit_bt_clicked" : self.submitForm, 
			"reset_bt_clicked" : self.clearForm, 
			"view_bt_clicked" : self.viewAll 
		}
		
		self.glade.connect_signals(dic) # adiciona os triggers
		self.updateLayout() # exibe todo conteúdo
		
		
	def viewAll(self, arg2):
		"""
			Função que vizualiza todos os cadastrados no banco
			
			@param:
				self = Objeto GTK.Window
				arg2 = UNDEFINED!!! #TODO : descobrir o que é o segundo argumento
		"""
		conexao.db.execute('SELECT * FROM cliente') # chama a query
		clientes = conexao.db.fetchall() # transforma os resultados em um dicionário
		tbl = gtk.VBox() # cria a vBox da tabela fake
		self.removeLabel() # remove o label Filho da Viewport
		dad = self.glade.get_object("viewport1") # pega a viewport
		
		for cliente in clientes:
			ln = gtk.HBox() # seta uma linha na tabela fake
			
			for campo in cliente:
				field = gtk.Label() # chama um label
				field.set_text(str(campo)) # atribui um texto a ele
				ln.pack_start(field) # adiciona a coluna a linha
				
			tbl.pack_start(ln) # adiciona a linha a tabela fake
			
		dad.add(tbl) # adiciona a tabela fake ao viewport
		self.updateLayout() # atualiza todo conteudo
	
	def updateLayout(self):
		"""
			Atualiza o layout do aplicativo
		"""
		self.glade.get_object("MainWindow").show_all()
	
	def removeLabel(self):
		"""
			Procura dentro da viewport se ele tem algum filho e o destrói
		"""
		if self.glade.get_object("viewport1").get_child():
			self.glade.get_object("viewport1").get_child().destroy()
	
	def addLabel(self):
		"""
			Adiciona o field de mensagens ao viewport
		"""
		self.removeLabel()
		self.glade.get_object("viewport1").add(gtk.Label('msg'))
	
	def clearForm(self, arg2):
		"""
			Função que limpa os campos do form
			
			@param:
				self = Objeto SELF
				arg2 = UNDEFINED!!! #TODO : descobrir o que é o segundo argumento
		"""
		self.addLabel()
		self.glade.get_object('nome').set_text("")
		
	def submitForm(self, arg2):
		"""
			Função que envia o formulário preenchido na main panel
			
			@param:
				self = Objeto GTK.Window
				arg2 = UNDEFINED!!! #TODO : descobrir o que é o segundo argumento
		"""
		data = date.today() # pega data de hoje no formato americano
		nome = self.glade.get_object("nome").get_text() # pega o valor do campo
		
		if nome:
			texto = "Cliente %s adicionado no dia %s \n" % (nome, data) # define texto de saida
			self.setMsg(texto)
			
			try:
				# TODO : criar um novo método para inserção
				conexao.db.execute("INSERT INTO cliente (nome) VALUES ('%s')" % nome) # tenta inserir no banco os dados inseridos
				conexao.con.commit()
			except:
				conexao.con.rollback() # caso não funcione, executa um rollback na query e preserva os dados
				self.setMsg('Erro no SQL, por favor, verifique as configurações') # exibe a mensagem de erro
			
		else:
			self.setMsg("Por favor, digite o nome do cliente")
			
	def setMsg(self, msg):
		"""
			Função que exibe as mensagens do programa numa box
			
			@param:
				self = Objeto GTK.Window
				msg = Mensagem a ser exibida
		"""
		self.addLabel() # cria o field de mensagens
		self.glade.get_object("viewport1").get_child().set_text(msg)
		self.updateLayout()


if __name__ == "__main__":
	panel = mainPanel() # chama a class
	gtk.main() # inicia o GTK
