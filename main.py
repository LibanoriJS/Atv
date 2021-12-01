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
  print(f"{Cores.FAIL}9. Cadastrar tipo de prova{Cores.ENDC}")
  print(f"{Cores.FAIL}10. Alterar tipo de prova{Cores.ENDC}")
  print(f"{Cores.FAIL}11. Ver tipo de prova{Cores.ENDC}")
  print(f"{Cores.FAIL}12. Excluir tipo de prova{Cores.ENDC}")    
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
	print(f"{Cores.FAIL}0. Sair{Cores.ENDC}")
	opcaoa = int(input("X. Escolha uma opçao : "))
	return opcaoa

#Opções visualizadas pelo Professor
def professor():
  print(33 * '*')
  print(f"{Cores.BOLD}{Cores.OKBLUE}***-- Perfil Professor --***{Cores.ENDC}")
  print(33 * '*')
  print(f"{Cores.BOLD}{Cores. OKGREEN}Tabela de escolha :{Cores.ENDC}")
  print(f"{Cores.FAIL}1. Inserir avaliações{Cores.ENDC}")
  print(f"{Cores.FAIL}2. Alterar avaliações{Cores.ENDC}")
  print(f"{Cores.FAIL}3. Ver avaliações{Cores.ENDC}")
  print(f"{Cores.FAIL}4. Excluir avaliações{Cores.ENDC}")
  print(33 * '*')
  print(f"{Cores.FAIL}5. Inserir Dados boletim{Cores.ENDC}")
  print(f"{Cores.FAIL}6. Alterar dados boletim{Cores.ENDC}")
  print(f"{Cores.FAIL}7. Ver dados boletim{Cores.ENDC}")
  print(f"{Cores.FAIL}8. Excluir dados boletim{Cores.ENDC}")  
  print(33 * '*')
  print(f"{Cores.FAIL}0. Sair{Cores.ENDC}")
  opcaop = int(input("X. Escolha uma opçao : "))
  return opcaop

# Exibição do menu principal
def perfil():
  print(33 * '*')
  print(f"{Cores.BOLD}{Cores.OKBLUE}***-- Controle de Avaliação --**  {Cores.ENDC}")
  print(33 * '*')
  print(f"{Cores.FAIL}1. Perfil Professor{Cores.ENDC}")
  print(f"{Cores.FAIL}2. Perfil Administrador{Cores.ENDC}")
  print(f"{Cores.FAIL}3. Perfil Aluno{Cores.ENDC}")
  print(f"{Cores.FAIL}4. Pesquisas Misc{Cores.ENDC}")
  print(f"{Cores.FAIL}{Cores.FAIL}5. Sair{Cores.ENDC}")
  print(19 * '*')
  perfil = int(input('X. Selecione uma opção: '))
  return perfil

def exercicio():
  print(33 * '*')
  print(f"{Cores.BOLD}{Cores.OKBLUE}***-- Exercícios  --**  {Cores.ENDC}")
  print(33 * '*')
  print(f"{Cores.FAIL}1. Listar todas as tabelas{Cores.ENDC}")
  print(f"{Cores.FAIL}2. Listar avaliações por periodo{Cores.ENDC}")
  print(f"{Cores.FAIL}3. Listar avaliações por professor{Cores.ENDC}")
  print(f"{Cores.FAIL}4. Listar avaliações por tipo{Cores.ENDC}")
  print(f"{Cores.FAIL}5. Listar alunos sem avaliações{Cores.ENDC}")
  print(f"{Cores.FAIL}6. Listar alunos por situação{Cores.ENDC}")
  print(f"{Cores.FAIL}7. Listar alunos por notas{Cores.ENDC}")
  print(33 * '*')
  print(f"{Cores.FAIL}{Cores.FAIL}0. Sair{Cores.ENDC}")
  print(19 * '*')
  ex = int(input('X. Selecione uma opção: '))
  return ex
    
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

  while opcaoperfil != 5:
    if opcaoperfil == 1:
      limpar()
      opcaoP = professor()	
      while opcaoP != 0:
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

        tabela = 'dataProva' #Dataprova
        if opcaoP == 5:
          print(f'Inserir {tabela}')
          tabelas.inserir(tabela, conn)
        elif opcaoP == 6:
          print(f'Atualizar {tabela}')
          tabelas.atualizar(tabela, conn)
        elif opcaoP == 7:
          print(f'Pesquisar {tabela}')
          tabelas.pesquisar(tabela, conn)
        elif opcaoP == 8:
          print(f'Excluir {tabela}')
          tabelas.excluir(tabela, conn)
        else:
          print('Opção inválida!')
          sleep(1)
        limpar()
        opcaoP = professor()
      else:
        print("Obrigado professor!")
        sleep(1)
      limpar()
      opcaoperfil = perfil()	

 		#alterar informações do professor
    elif opcaoperfil == 2:
      limpar()
      opcaoadm = administrador()

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

        #Opções dentro da tabela aluno

        tabela = 'aluno' 
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

#Opções dentro da tabela tipo, usado para provas

        tabela = 'tipo'
        if opcaoadm == 9:
          tabela = 'tipo'
          print(f'Inserir {tabela}')
          tabelas.inserir(tabela, conn)
        elif opcaoadm == 10:
          tabela = 'tipo'
          print(f'Atualizar {tabela}')
          tabelas.atualizar(tabela, conn)
        elif opcaoadm == 11:
          tabela = 'tipo'
          print(f'Pesquisar {tabela}')
          tabelas.pesquisar(tabela, conn)
        elif opcaoadm == 12:
          tabela = 'tipo'
          print(f'Excluir {tabela}')
          tabelas.excluir(tabela, conn)
        else: 
          print("Opção inválida!")
          sleep(1)
        limpar()
        opcaoadm = administrador()
      else:
        print("Obrigada administrador!")
        sleep(1)
      limpar()
      opcaoperfil = perfil()
			
		#Sistema a ser acessado pelo aluno
    elif opcaoperfil == 3:
      limpar()
      opcaoA = aluno()
      while opcaoA != 0:
        if opcaoA == 1:
          tabela = 'avaliacao'
          print(f'Pesquisa Avaçada, Matricula :  {tabela}')
          tabelas.pesquisarAluno(tabela, conn)
        else:
          print("Opção inválida!")
          sleep(1)
        limpar()
        opcaoA = aluno()
      else:
        print("Obrigado pelo acesso!")
        sleep(1)
      limpar()
      opcaoperfil = perfil()			

  # Exercicios pedidos do trabalho
    elif opcaoperfil == 4:
      limpar()
      opcaoEx = exercicio()
      while opcaoEx != 0:
        if opcaoEx == 1:
          print(f'Mostrar todas as Tabelas')

          print(f"{Cores.BOLD}{Cores.OKBLUE}Tabela Aluno{Cores.ENDC}")
          tabela = 'aluno'
          tabelas.pesquisar(tabela, conn)
          print('\n')

          print(f"{Cores.BOLD}{Cores.OKBLUE}Tabela Professor{Cores.ENDC}")
          tabela = 'professor'
          tabelas.pesquisar(tabela, conn)
          print('\n')

          print(f"{Cores.BOLD}{Cores.OKBLUE}Tabela Avaliação{Cores.ENDC}")
          tabela = 'avaliacao'
          tabelas.pesquisar(tabela, conn)
          print('\n')

          print(f"{Cores.BOLD}{Cores.OKBLUE}Tabela DataProva{Cores.ENDC}")
          tabela = 'dataProva'
          tabelas.pesquisar(tabela, conn)
          print('\n')

          print(f"{Cores.BOLD}{Cores.OKBLUE}Tabela Tipo{Cores.ENDC}")
          tabela = 'tipo'
          tabelas.pesquisar(tabela, conn)


        elif opcaoEx == 2:
          tabela = 'dataProva'
          faixaPesq='periodo'
          tabelas.pesquisaEsp(tabela, conn, faixaPesq)
          print('\n')
          
        elif opcaoEx == 3:
          tabela = 'dataProva'
          faixaPesq='prof'
          tabelas.pesquisaEsp(tabela, conn, faixaPesq)
          print('\n')

        elif opcaoEx == 4:
            tabela = 'avaliacao'
            faixaPesq='tipo'
            tabelas.pesquisaEsp(tabela, conn, faixaPesq)
            print('\n')

        elif opcaoEx == 5:
            tabela = 'aluno'
            tabelas.listarSemAvaliacao(tabela, conn)
            print('\n')
        
        elif opcaoEx == 6:
            tabela = 'aluno'
            tabelas.listarSituacao(tabela, conn)
            print('\n')

        elif opcaoEx == 7:
            tabela = 'aluno'
            tabelas.listarNotas(tabela, conn)
            print('\n')
        else:
            print("Opção inválida!")
            sleep(1)
        limpar()
        opcaoEx = exercicio()
      else:
        print("Nenhum exercicio encontrado! Use numeros de 1 a 7!")
        sleep(1)
      limpar()
      opcaoperfil = perfil()
      
  else:
    print('Volte sempre!')