# CRM Py
## simple pyGTK CRM

##### Mudança Importante:
Layout feito com Glade 3, alterações de XML feitas na mão, e.g.: gtkBox => gtkHBox

##### Requisitos:
* Python 2.6 +
* pyGTK
* GTK+
* GDK
* pPrint ( para dump de variáveis )
* Glade 3 +  ( desenvolvimento visual do aplicativo )
* python-mysqldb

##### Teclas de atalho:
* ESC : fechar o programa
* F1 : vizualiza todos os cadastros
* F2 : limpa o formulário
* F3 : busca de clientes (TODO)
* ENTER : submita o formulário

##### Banco de dados:
* Tabela:
 - cliente [id, nome, email, telefone, data]

##### TODO:
* Melhorias :
 + Adicionar validação de campos no submit
 + Criar função para remover cliente
 + Criar função para editar cliente
 + Criar função para buscar cliente
 + Definir largura fixa para as labels na fake table
 + Liberar para que as labels da fake table tenham seus textos selecionados
* Futuro :
 + Refatorar o código fazendoo funcionar como um MVC
 + Gerar um pacote .deb
 + Utilizar o py2exe para criar um executável do Windows.
 + Deixar o programa com uma cara mais "User Friendly"
 + Adicionar botão para gerar backup do banco de dados.

