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
import gtk.gdk
import conexao
import re # regexp libary
import pprint # fazer um 'var_dump' de uma variável, utilize pprint.pprint(variavel)
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
		self.glade.get_object("rotulo").modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#AAAAAA')) # altera cor do rodapé
		
		# Dicionário das triggers
		dic = { 
			"window_keypress" : self.keyListener,
			"submit_bt_clicked" : self.submitForm, 
			"reset_bt_clicked" : self.clearForm, 
			"view_bt_clicked" : self.viewAll 
		}
		
		self.glade.connect_signals(dic) # adiciona os triggers
		self.updateLayout() # exibe todo conteúdo
	
	def keyListener(self, widget, event):
		"""
			Função listener de keypress para execução das teclas de atalho
		"""
		if event.keyval == 65307: # ESC
			gtk.main_quit()
		if event.keyval == 65470: # F1
			self.viewAll(arg1)
		if event.keyval == 65471: # F2
			self.clearForm(arg1)
		if event.keyval == 64572: # F3
			pass # Pesquisar usuario
		if event.keyval == 65293: # ENTER
			self.submitForm(widget)
	
	def viewAll(self, widget):
		"""
			Função que vizualiza todos os cadastrados no banco
			
			@param:
				self = Objeto GTK.Window
				widget = widget pai
		"""
		conexao.db.execute('SELECT * FROM cliente') # chama a query
		clientes = conexao.db.fetchall() # transforma os resultados em um dicionário
		tbl = gtk.VBox() # cria a vBox da tabela fake
		self.removeLabel() # remove o label Filho da Viewport
		dad = self.glade.get_object("viewport1") # pega a viewport
		c = 1 # zera contador
		
		campos = ['ID' , 'Nome', 'Data de criação' ,'Email', 'Telefone'] # define labels do header
		tln = gtk.HBox() # cria lane header da fake table
		for campo in campos:
			f = gtk.Label() # cria o label
			f.set_markup("<b>"+campo+"</b>") # define o texto
			tln.pack_start(f)
		
		tbl.pack_start(tln) # adiciona o header na fake table
		
		for cliente in clientes:
			ln = gtk.HBox() # seta uma linha na tabela fake
			
			for campo in cliente:
				field = gtk.Label() # chama um label
				texto = "<b>"+str(campo)+"</b>" if c % 2 == 0 else str(campo) # cria o efeito "zebra"
				field.set_markup(texto) # atribui um texto a ele
				ln.pack_start(field) # adiciona a coluna a linha
			c += 1
			
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
	
	def clearForm(self, widget):
		"""
			Função que limpa os campos do form
			
			@param:
				self = Objeto da class
				widget = Objeto com o Widget que chamou a função
		"""
		self.addLabel()
		self.glade.get_object('nome').set_text("")
		self.glade.get_object('email').set_text("")
		self.glade.get_object('telefone').set_text("")
		
	def submitForm(self, widget):
		"""
			Função que envia o formulário preenchido na main panel
			
			@param:
				self = Objeto da class
				widget = Objeto com o Widget que chamou a função
		"""
		data = date.today() # pega data de hoje no formato americano
		nome = self.glade.get_object("nome").get_text() # pega o valor do campo nome
		email = self.glade.get_object("email").get_text() # pega o valor do campo email
		telefone = self.glade.get_object("telefone").get_text() # pega o valor do campo telefone
		
		if nome and telefone and email:
			if self.validate({ data : 'data', email : 'email', telefone : 'tel', nome : 'str'} ):
				texto = "Cliente %s adicionado no dia %s \n Telefone: %s \n Email: %s" % (nome, data, telefone, email) # define texto de saida
				self.setMsg(texto)
				
				try:
					# TODO : criar um novo método para inserção
					conexao.db.execute("INSERT INTO cliente (nome, email, telefone) VALUES ('%s', '%s', '%s')" % (nome, email, telefone)) # tenta inserir no banco os dados inseridos
					conexao.con.commit()
				except:
					conexao.con.rollback() # caso não funcione, executa um rollback na query e preserva os dados
					self.setMsg('Erro no SQL, por favor, verifique as configurações') # exibe a mensagem de erro
		else:
			self.setMsg("Por favor, preencha todos os campos")
			
	def validate(self, data):
		for valor in data.keys():
			if data[valor] == "tel":
				rgx = "^\([0-9][0-9]\)[0-9]{4}\-[0-9]{4}$"
				msg = "Ocorreu um problema na validação do telefone"
				
				if not re.compile(rgx).match(valor):
					self.setMsg(msg)
					return False
			
			if data[valor] == "email":
				rgx = "^\w+\@\w+\.\w+$"
				msg = "Ocorreu um erro na validação do Email"
				
				if not re.compile(rgx).match(valor):
					self.setMsg(msg)
					return False
			
			if data[valor] == "str":
				rgx = "^\w+$"
				msg = "Ocorreu um erro na validação de String"
				
				if not re.compile(rgx).match(valor):
					self.setMsg(msg)
					return False
					
		return True
	
	def setMsg(self, msg):
		"""
			Função que exibe as mensagens do programa numa box
			
			@param:
				self = Objeto da class
				msg = Mensagem a ser exibida
		"""
		self.addLabel() # cria o field de mensagens
		self.glade.get_object("viewport1").get_child().set_text(msg)
		self.updateLayout()


if __name__ == "__main__":
	panel = mainPanel() # chama a class
	gtk.main() # inicia o GTK
