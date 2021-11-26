# Importando o módulo do sqlite3 para manipularmos o banco de dados SQLITE3
import sqlite3
# Importando o módulo do sqlite3 e a classe Error para exibir mensagens de erro
from sqlite3 import Error
# Importando o módulo time para utilizar o método sleep que aguarda o 
# tempo em segundos informando dentro do parênteses
from time import sleep
# Importando o arquivo schema.py para criar as tabelas do banco de dados
import schema
# Importando o arquivo tabelas para manipular as informações nelas (CRUD)
# Criar, atualizar, excluir, e pesquisar.
import tabelas
# Importando o o arquivo cores.py, a classe Cores para colocar cores nos textos
from cores import Cores
#Opções visualizadas pelo Admin do sistema
def administrador():
  print(33 * '*')
  print(f"{Cores.BOLD}{Cores.OKBLUE}***-- Perfil Administrador --***{Cores.ENDC}")
  print(33 * '*')
  print(f"{Cores.BOLD}{Cores. OKGREEN}Tabela de escolha :{Cores.ENDC}")
  print(f"{Cores.FAIL}1. Cadastrar Professor{Cores.ENDC}")
  print(f"{Cores.FAIL}2. Alterar Professor{Cores.ENDC}")
  print(f"{Cores.FAIL}3. Ver professores Cadastrados{Cores.ENDC}")
  print(f"{Cores.FAIL}4. Excluir Cadastrados{Cores.ENDC}")  
  print(33 * '*')
  print(f"{Cores.FAIL}5. Cadastrar Alunos{Cores.ENDC}")
  print(f"{Cores.FAIL}6. Alterar Alunos{Cores.ENDC}")
  print(f"{Cores.FAIL}7. Ver Alunos Cadastrados{Cores.ENDC}")
  print(f"{Cores.FAIL}8. Excluir Alunos{Cores.ENDC}")  
  print(33 * '*')
  print(f"{Cores.FAIL}9. Inserir Dados boletim{Cores.ENDC}")
  print(f"{Cores.FAIL}10. Alterar dados boletim{Cores.ENDC}")
  print(f"{Cores.FAIL}11. Ver dados boletim{Cores.ENDC}")
  print(f"{Cores.FAIL}12. Excluir dados boletim{Cores.ENDC}")
  print(33 * '*')
  print(f"{Cores.FAIL}0. Sair{Cores.ENDC}")
  opcaoadm = int(input("X. Escolha uma opçao : "))
  return opcaoadm

#Opções visualizadas pelo aluno
def aluno():
	print(33 * '*')
	print(f"{Cores.BOLD}{Cores.OKBLUE}***-- Perfil Aluno --***{Cores.ENDC}")
	print(33 * '*')
	print(f"{Cores.BOLD}{Cores. OKGREEN}Tabela de escolha :{Cores.ENDC}")
	print(f"{Cores.FAIL}1. Visualizar notas{Cores.ENDC}")
	print(f"{Cores.FAIL}2. Sair{Cores.ENDC}")
	opcaoa = int(input("X. Escolha uma opçao : "))
	return opcaoa
  #Opções visualizadas pelo Professor
def professor():
  print(33 * '*')
  print(f"{Cores.BOLD}{Cores.OKBLUE}***-- Perfil Professor --***{Cores.ENDC}")
  print(33 * '*')
  print(f"{Cores.BOLD}{Cores. OKGREEN}Tabela de escolha :{Cores.ENDC}")
  print(f"{Cores.FAIL}1. Inserir notas{Cores.ENDC}")
  print(f"{Cores.FAIL}2. Alterar notas{Cores.ENDC}")
  print(f"{Cores.FAIL}3. Ver notas{Cores.ENDC}")
  print(f"{Cores.FAIL}4. Excluir notas{Cores.ENDC}")
  print(33 * '*')
  print(f"{Cores.FAIL}5. Inserir Dados boletim{Cores.ENDC}")
  print(f"{Cores.FAIL}6. Alterar dados boletim{Cores.ENDC}")
  print(f"{Cores.FAIL}7. Ver dados boletim{Cores.ENDC}")
  print(f"{Cores.FAIL}8. Excluir dados boletim{Cores.ENDC}")  
  print(33 * '*')
  print(f"{Cores.FAIL}0. Sair{Cores.ENDC}")
  opcaop = int(input("X. Escolha uma opçao : "))
  return opcaop

def perfil():
  print(33 * '*')
  print(f"{Cores.BOLD}{Cores.OKBLUE}***-- Controle de Avaliação --**  {Cores.ENDC}")
  print(33 * '*')
  print(f"{Cores.FAIL}1. Perfil Professor{Cores.ENDC}")
  print(f"{Cores.FAIL}2. Perfil Administrador{Cores.ENDC}")
  print(f"{Cores.FAIL}3. Perfil Aluno{Cores.ENDC}")
  print(f"{Cores.FAIL}{Cores.FAIL}4. Sair{Cores.ENDC}")
  print(19 * '*')
  perfil = int(input('X. Selecione uma opção: '))
  return perfil
    
def criar_conexao(banco):
	"""Criando a conexão com o banco de dados Sqlite3."""
	# Variável conn inicializada para estabelecer a conexão com o banco
	conn = None
	# Tentará fazer a conexão com o banco de dados
	try: 
		# Criando a conexão com o banco e salvando o objeto Connection na variável conn.
		conn = sqlite3.connect(banco)
		# Exibe a versão do Sqlite
		print(sqlite3.sqlite_version)
		# Sucesso na conexão. É retornado a conexão a quem chamou.
		return conn
		# Caso negativo, não conseguiu estabelecer conexão, retorna o erro que ocorreu.	
	except Error as e: 
		print(e)

# Função para limpar a tela antes de exibir a próxima instrução
def limpar():
    # Importando o módulo do sistema operacional (os) para usar instruções dele
    import os
    # Importando o módulo time para utilizar o método sleep que aguarda o 
    # tempo em segundos informando dentro do parênteses
    
    from time import sleep
    
    # Função para limpar a tela
    def screen_clear():
    # Para os sistemas operacionais: mac and linux(here, os.name is 'posix')
        if os.name == 'posix':
            _ = os.system('clear')
        else:
        # Para o sistema operacional windows
            _ = os.system('cls')
    # Aguarda 1 segundo para executar a próxima instrução
  
    # Chama a função de limpeza
    screen_clear()

if __name__ == '__main__':
  limpar()
  print(34 * '*')
  print(f"{Cores.BOLD}{Cores.OKBLUE}***-- Controle de Avaliações --***  {Cores.ENDC}")
  print(34 * '*')
  print(f"\n{Cores.HEADER}{Cores.HEADER}Criando o banco de dados se não existir ... {Cores.ENDC}")

  banco = input(f"{Cores.FAIL}{Cores.FAIL}Informe o Nome do Banco : {Cores.ENDC}")
  print(f"{Cores.BOLD}{Cores.OKBLUE}Criando conexão ... {Cores.ENDC}")
  conn = criar_conexao(banco)
  print(f"{Cores.BOLD}{Cores.OKBLUE}\nCriando tabelas do banco de dados se não existirem ... {Cores.ENDC}")
  schema.criar_tabelas(banco)

  input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para prosseguir...{Cores.ENDC}")
  limpar()

  #Seleciona o Perfil do usuario
  
  opcaoperfil = perfil()
  limpar()
  while opcaoperfil != 4:
    if opcaoperfil == 1:
      opcaoP = professor()
      limpar()
      #Escolhe as opçoes do usuario 1
      
      while opcaoP != 5: #alterar informações da avalição
        tabela = 'avaliacao'
        if opcaoP == 1:
          print(f'Inserir {tabela}')
          tabelas.inserir(tabela, conn)
        elif opcaoP == 2:
          print(f'Atualizar {tabela}')
          tabelas.atualizar(tabela, conn)
        elif opcaoP == 3:
          print(f'Pesquisar {tabela}')
          tabelas.pesquisar(tabela, conn)
        elif opcaoP == 4:
          print(f'Excluir {tabela}')
          tabelas.excluir(tabela, conn)
        else:
          print('Opção inválida!')
        limpar()
        opcaoP = professor()
        limpar()

   #alterar informações do professor
    if opcaoperfil == 2:
      opcaoadm = administrador()
      limpar()

      while opcaoadm != 0:

        tabela = 'professor'
        if opcaoadm == 1:
          print(f'Inserir {tabela}')
          tabelas.inserir(tabela, conn)
        elif opcaoadm == 2:
          print(f'Atualizar {tabela}')
          tabelas.atualizar(tabela, conn)
        elif opcaoadm == 3:
          print(f'Pesquisar {tabela}')
          tabelas.pesquisar(tabela, conn)
        elif opcaoadm == 4:
          print(f'Excluir {tabela}')
          tabelas.excluir(tabela, conn)
        tabela = 'dataProva' #Dataprova
        if opcaoadm == 5:
          print(f'Inserir {tabela}')
          tabelas.inserir(tabela, conn)
        elif opcaoadm == 6:
          print(f'Atualizar {tabela}')
          tabelas.atualizar(tabela, conn)
        elif opcaoadm == 7:
          print(f'Pesquisar {tabela}')
          tabelas.pesquisar(tabela, conn)
        elif opcaoadm == 8:
          print(f'Excluir {tabela}')
          tabelas.excluir(tabela, conn)

        tabela = 'aluno' #
        if opcaoadm == 5:
          print(f'Inserir {tabela}')
          tabelas.inserir(tabela, conn)
        elif opcaoadm == 6:
          print(f'Atualizar {tabela}')
          tabelas.atualizar(tabela, conn)
        elif opcaoadm == 7:
          print(f'Pesquisar {tabela}')
          tabelas.pesquisar(tabela, conn)
        elif opcaoadm == 8:
          print(f'Excluir {tabela}')
          tabelas.excluir(tabela, conn)
          
        tabela = 'dataProva' #Dataprova
        if opcaoadm == 9:
          print(f'Inserir {tabela}')
          tabelas.inserir(tabela, conn)
        elif opcaoadm == 10:
          print(f'Atualizar {tabela}')
          tabelas.atualizar(tabela, conn)
        elif opcaoadm == 11:
          print(f'Pesquisar {tabela}')
          tabelas.pesquisar(tabela, conn)
        elif opcaoadm == 12:
          print(f'Excluir {tabela}')
          tabelas.excluir(tabela, conn)
        else:
          print('Opção inválida!')
          limpar()
        opcaoadm = administrador()
        limpar()
   
  #alterar informações do aluno
    if opcaoperfil == 3:
      opcaoA = aluno()
      limpar()
      
      while opcaoA != 2: 
        tabela = 'avaliacao'
        if opcaoA == 1:
          print(f'Pesquisar {tabela}')
          tabelas.pesquisar(tabela, conn)
        else:
          print('Opção inválida!')
        limpar()
      opcaoperfil = perfil()
      limpar()
    else:
      limpar()
      print("Obrigado. Volte sempre!")  
      if opcaoA == 2:
          tabela= 'aluno'
          print(f'Pesquisar {tabela}')
          tabelas.mostrarTudo(tabela, conn)