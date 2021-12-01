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
    c.execute("""CREATE TABLE IF NOT EXISTS aluno (
        matricula INTEGER primary key,
        nome TEXT,
        cpf TEXT,
        dataNasc DATE,
        curso TEXT)""")

    conn.commit()
    
    # Insere dados na tabela Aluno
    #---------------------------------------------#
    c.execute("INSERT INTO aluno VALUES ('123','Pedro','524534543','2000-11-11','ads'),('456','joao','524556745','1998-11-11','ADS'),('789','Felipe','524533343','2094-01-02','ENG'),('112','Paulo','524533459','2097-08-09','ADS');")
    conn.commit()
   

    # Executando a instrução de criação da tabela tipo
    c.execute("""CREATE TABLE IF NOT EXISTS tipo (
        idTipo INTEGER primary key,
        descricao TEXT NOT NULL)
    """)
    conn.commit()

     # Insere dados na tabela Tipo
     #-------------------------------------------#
    c.execute("INSERT INTO tipo VALUES ('1','P1'),('2','P2'),('3','IFA');")
    conn.commit()
    
    # Executando a instrução de criação da tabela professor
    c.execute("""
    CREATE TABLE IF NOT EXISTS professor (
        idProf INTEGER primary key,
        nome TEXT NOT NULL,
        materia TEXT NOT NULL)
    """)
    conn.commit()	

     # Insere dados na tabela professor
     #-------------------------------------------#
    c.execute("INSERT INTO professor VALUES ('1','Matarazo','ESW'),('2','Ana Banana','LP2'),('3','Felipe','SPO');")
    conn.commit()


    # Executando a instrução de criação da tabela avaliação
    c.execute("""
    CREATE TABLE IF NOT EXISTS avaliacao (
        idAvaliacao INTEGER primary key,
        materia TEXT NOT NULL,
        descricao TEXT NOT NULL,
        notaMin DOUBLE NOT NULL,
        notaMax DOUBLE NOT NULL,
        notaAprov DOUBLE NOT NULL,
        dataPrevista DATE NOT NULL,
        idTipo INTEGER NOT NULL,
        FOREIGN KEY (idTipo) REFERENCES tipo(idTipo))
    """) 
    conn.commit()

     # Insere dados na tabela avaliação
     #-------------------------------------------#
    c.execute("INSERT INTO avaliacao VALUES ('1','ESW','Pres','4','10','6','2021-11-11','1'),('2','SPO','Pres','4','10','6','2021-10-10','2'),('3','ESW','Ead','4','10','6','2021-11-16','1');")
    conn.commit()

    # Executando a instrução de criação da tabela dataProva
    c.execute("""
    CREATE TABLE IF NOT EXISTS dataProva (
        idDataProva INTEGER primary key,
        notaObt DOUBLE NOT NULL,
        dataProva DATE NOT NULL,
        materia TEXT NOT NULL, 
        matricula INTEGER NOT NULL,
        idProf INTEGER NOT NULL,
        idAvaliacao INTEGER NOT NULL,
        situacao TEXT NOT NULL,
        FOREIGN KEY (matricula) REFERENCES aluno(matricula),
        FOREIGN KEY (idProf) REFERENCES professor(idProf),
        FOREIGN KEY (idAvaliacao) REFERENCES avaliacao(idAvaliacao))
    """)
    conn.commit()

    # Insere dados na tabela dataProva
    #-------------------------------------------#
    c.execute("INSERT INTO dataProva VALUES ('1','8','2021-12-01','ESW','123','1','1','Aprovado'),('2','3','2021-11-16','SPO','456','3','2','Reprovado'),('3','8','2021-12-01','ESW','123','1','3','Aprovado'), ('4','5','2021-12-05','SPO','123','3','2','IFA');")
    conn.commit()

    print(f"{Cores.BOLD}{Cores.OKGREEN}Tabelas criadas com sucesso!{Cores.ENDC}")
  except Error as e:
    print(e)
