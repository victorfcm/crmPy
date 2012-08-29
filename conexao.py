#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  conexao.py
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


import MySQLdb

try:
	con = MySQLdb.connect('localhost', 'root', 'victor1103') # efetua o login no banco
	con.select_db('crmpy') # seleciona o DB
	db = con.cursor() # define o cursor dentro da variável DB
except:
	print('Erro de conexão com o banco.')
