# CRM Py
## simple pyGTK CRM

##### Mudança Importante:
Layout feito com Glade 3, alterações de XML feitas na mão, e.g.: gtkBox => gtkHBox

##### Requisitos:
* Python 2.6 +
* pyGTK
* GTK+
* Glade 3 +
* python-mysqldb


##### Banco de dados:
* Tabelas:
 - cliente [id, nome, data]
 - telefone [id, clienteid, tel] 
 - email [id, clienteid, email]

##### TODO:
* Layout :
 + Adicionar os campos :
  - Telefone
  - Email
 + Adicionar botão para ativar lightbox (evita o clique fora da aplicação)
 + Adicionar botão para ativar o fullscreen
* Melhorias :
 + Criar função para remover cliente
 + Criar função para editar cliente
 + Criar função para buscar cliente
 + Função clearForm(), fazer de forma que não precise ser descrito o nome de cada field a ser limpo
 + Descobrir o que são os "segundos parametros" passados nas funções
 + Melhorar a explicação nas Docstrings
* Futuro :
 + Refatorar o código fazendoo funcionar como um MVC
 + Gerar um pacote .deb
 + Utilizar o py2exe para criar um executável do Windows.
 + Deixar o programa com uma cara mais "User Friendly"
 + Adicionar botão para gerar backup do banco de dados.
 + Adicionar "teclas de atalho" :
  - Enter, enviar o form
  - ESC, limpar o form
  - CTRL + A, visualizar todos
