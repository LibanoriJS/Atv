# Importando o módulo sqlite3 para criarmos nosso banco e manipulá-lo.
import sqlite3
from sqlite3 import Error
from cores import Cores

def criar_tabelas(banco):
	# Definindo a conexão com o BD chamado 
	conn = sqlite3.connect(banco)
	# Definindo o cursor cuja função é permitir navegar e manipular os registros do BD.
	c = conn.cursor()
	
	try:
		# Executando a instrução de criação da tabela aluno no BD
		# a matrícula aponta para rowid (chave primaria da tabela)
		c.execute("""
		CREATE TABLE IF NOT EXISTS aluno (
		matricula INTEGER primary key,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL,
        dataNasc DATE NOT NULL,
		siglaCurso TEXT NOT NULL,
        situacao TEXT NOT NULL,
		criado_em DATE NOT NULL);
		""")
		
    # Executando a instrução de criação da tabela tipo
		c.execute("""
		CREATE TABLE IF NOT EXISTS tipo (
		idTipo INTEGER primary key,
        materia TEXT NOT NULL,
		descricao TEXT NOT NULL,
		criado_em DATE NOT NULL);
		""")

    # Executando a instrução de criação da tabela professor
		c.execute("""
		CREATE TABLE IF NOT EXISTS professor (
		idProf INTEGER primary key,
        nome TEXT NOT NULL,
        materia TEXT NOT NULL,
		criado_em DATE NOT NULL);
		""")		

    # Executando a instrução de criação da tabela avaliação
		c.execute("""
		CREATE TABLE IF NOT EXISTS avaliacao (
		idAvaliacao INTEGER primary key,
        siglaMat TEXT NOT NULL,
        descricao TEXT NOT NULL,
        notaMin DOUBLE NOT NULL,
		notaMax DOUBLE NOT NULL,
        notaAprov DOUBLE NOT NULL,
        dataPrevista DATE NOT NULL,
		criado_em DATE NOT NULL);
		""") 

    # Executando a instrução de criação da tabela dataProva
		c.execute("""
		CREATE TABLE IF NOT EXISTS dataProva (
		idDataProva INTEGER primary key,
        siglaMat TEXT NOT NULL,
        notaObt DOUBLE NOT NULL,
        dataProva DATE NOT NULL,
		criado_em DATE NOT NULL);
			""") 

   	# Exibindo na tela a mensagem de sucesso de criação da tabela tarefas.
		return print(f"{Cores.BOLD}{Cores.OKGREEN}Tabelas criadas com sucesso!{Cores.ENDC}")
	except Error as e:
		print(e)