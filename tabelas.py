
# Importando o módulo sqlite3 para criarmos nosso banco e manipulá-lo.
from datetime import date
from cores import Cores
from sqlite3 import Error

#*****INSERCAO DE DADOS
#*********INSERCAO DE DADOS
#***********INSERCAO DE DADOS
#**************INSERCAO DE DADOS

def inserir(tabela, conn):
    try:
        c = conn.cursor()
        if tabela == 'aluno': #Cadastrar aluno
            nome = input("Nome do aluno: ").title()
            cpf = input("CPF: ")
            dataNasc = input("Data de nascimento: ")
            curso = input("Curso matriculado: ").upper()
            alunoNovo = (nome, cpf, dataNasc, curso)
            c.execute("INSERT INTO aluno (nome, cpf, dataNasc, curso) VALUES (?, ?, ?, ?);", alunoNovo)
            conn.commit()  # Gravar o novo aluno no BD
      
        elif tabela == 'tipo':  #cadastrar tipo de prova
            descricao = input("Tipo de avaliação: ").upper()
            x = (descricao,)
            c.execute("INSERT INTO tipo (descricao) VALUES (?);", x)
            conn.commit()  # Gravar o novo tipo de prova no BD
        
        elif tabela == 'professor':  #Cadastrar professor no BD
            nome = input(" Nome do professor: ").title()
            materia = input("Matéria: ").upper()
            profNovo = (nome, materia)
            c.execute("INSERT INTO professor (nome, materia) VALUES (?, ?);", profNovo)
            conn.commit()  # Gravar o novo professor no BD
    
        elif tabela == 'avaliacao':  #Cadastrar avaliações no BD
            materia = input("Matéria: ").upper()
            descricao = input("Descrição de como será realizada a prova: ").upper()
            notaMin = input("Nota mínima: ") 
            notaMax = input("Nota máxima: ")
            notaAprov = input("Nota de aprovação: ")
            dataPrevista = input("Data de realização: ")
            idTipo = input("Insira o id do tipo de prova: ")
            avaliacaoNovo =(materia, descricao, notaMin, notaMax, notaAprov, dataPrevista, idTipo)
            c.execute("INSERT INTO avaliacao (materia, descricao, notaMin, notaMax, notaAprov, dataPrevista, idTipo) VALUES (?,?,?,?,?,?,?);", avaliacaoNovo)
            conn.commit()  # Gravar novas avaliações no BD
            print(
             f"{Cores.BOLD}{Cores.OKGREEN}Inserção com sucesso em {tabela}.{Cores.ENDC}"
              ) 
            
        elif tabela == 'dataProva':  #Cadastrar dataProva (relação M:N aluno/Avaliação) no BD
            notaObt = input("Nota obtida: ")
            dataProva = input("Data em que foi realizada: ")
            materia = input("Insira a matéria da prova: ").upper()
            matricula = input("Insira a matrícula do aluno: ")
            idProf = input("Insira o id do professor: ")
            idAvaliacao = input("Insira o id da prova: ")
            situacao = input("Insira a situação do aluno:").title()

            dataProvaNovo =(notaObt, dataProva, materia, matricula, idProf, idAvaliacao, situacao)
            c.execute("INSERT INTO dataProva (notaObt, dataProva, materia, matricula, idProf, idAvaliacao, situacao) VALUES (?, ?, ?, ?, ?, ?, ?);", dataProvaNovo)
            conn.commit()  # Gravar novas avaliações no BD
      
    except Error as e:
        print(e)
    else:
        print(f"{Cores.BOLD}{Cores.OKGREEN}Inserção com sucesso em {tabela}.{Cores.ENDC}")  
        input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

#alterar cadastro de aluno   
def atualizar(tabela, conn):
    try:
        c = conn.cursor()
        if tabela == 'avaliacao': # Atualizar a tabela avaliação
            pesquisar(tabela, conn)
            x = input("Informe o ID da avaliação : ")
            materia = input('\nMatéria da prova: ').upper()
            descricao = input('\nForma como será realizada a prova: ').upper()
            notaMin = input('\nNota Minima : ')
            notaMax = input('\nNota maxima : ')
            notaAprov = input('\nNota de aprovação : ')
            dataPrevista = input('\nData Prevista : ')
            idTipo = input('\nInsira o id do tipo de prova : ')

            avaliacao = (materia, descricao, notaMin, notaMax, notaAprov, dataPrevista, idTipo,x)

            c.execute("UPDATE avaliacao SET materia =?, descricao =?, periodo =? ,notaMin =?, notaMax =?, notaAprov =?, dataPrevista =?, idTipo=? WHERE idAvaliacao=?;", avaliacao)
            conn.commit()

        elif tabela == 'dataProva': # Atualizar a tabela dataProva
            id = input("Informe o ID da avaliação realizada : ")
            notaObt = input("Nota obtida pelo aluno: ")
            dataProva = input("Data em que foi realizada: ")

            avaliacaoData = (notaObt, dataProva, id)

            c.execute("UPDATE avaliacao SET notaObt=?, dataProva=? WHERE idDataProva=?;", avaliacaoData)
            conn.commit()
    
        elif tabela == 'professor': # Atualizar a tabela professor
            pesquisar(tabela, conn)
            id = input("Informe o Id do professor: ").title()
            nome = input("Informe o Nome do professor: ").title()
            materia = input('Informe a sigla da materia: ').upper()
            professor = (nome, materia,id)
            c.execute("UPDATE professor SET nome=?, materia=? WHERE idProf=?;", professor)
            conn.commit()
        
        elif tabela == 'aluno': # Atualizar a tabela aluno
            pesquisar(tabela, conn)
            id = input("Informe a matricula do aluno: ").title()
            nome = input("Informe o Nome do aluno: ").title()
            cpf = input("Informe o CPF do aluno: ")     
            DataNasc = input("Informe a data de nascimento do aluno: ")
            curso = input("Informe a sigla do curso do aluno: ").upper()
      
            aluno = (nome, cpf,DataNasc, curso,id)

            c.execute("UPDATE aluno SET nome =?, cpf =?, DataNasc =?, curso =? WHERE matricula=?;", aluno)
            conn.commit()
          
        elif tabela == 'dataProva': # Atualizar a tabela dataProva
            pesquisar(tabela, conn)
            id = input("Informe o Id da realização da prova: ")
            notaObt = input("Informe a nota obtida pelo aluno: ")
            dataProva = ('Informe a data em que a prova foi realizada: ')

            realProva = (notaObt,dataProva,id)
            c.execute("UPDATE dataProva SET notaObt=?, dataProva=? WHERE idDataProva=?;", realProva)
            conn.commit()

    except Error as e:
        print(e)
    else:
        print(f"{Cores.BOLD}{Cores.OKGREEN}Atualização com sucesso em {tabela}.{Cores.ENDC}")
        input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

def pesquisar(tabela, conn):
  try:
      c = conn.cursor()    
      if tabela == 'avaliacao': # Realizar pesquisa na tabela avaliação
          c.execute("SELECT * FROM avaliacao;")
          resultado = c.fetchall()
          if resultado:
              print(f"{Cores.BOLD}{Cores.OKGREEN}")
              print("{:<4} {:<5} {:<10} {:<10} {:<10}  {:<12} {:<14} {:<10}".format("ID", "Mat","EAD/PRES",'Nota Min','Nota Max','Nota Aprov','Data', 'idTipo'))
              print(f"{Cores.ENDC}")
              for item in range(len(resultado)):
                  print("{:<4} {:<7} {:<11} {:<10} {:<10} {:<10} {:<17} {:<10}".format(resultado[item][0], resultado[item][1], resultado[item][2],resultado[item][3], resultado[item][4],resultado[item][5],resultado[item][6],resultado[item][7]))
            
      elif tabela == 'professor': # Realizar pesquisa na tabela professor
          c.execute("SELECT * FROM professor;")
          resultado = c.fetchall()
          if resultado:
              print(f"{Cores.BOLD}{Cores.OKGREEN}")
              print("{:<4} {:<10} {:<8} ".format("ID","Nome", "Matéria"))
              print(f"{Cores.ENDC}")
              for item in range(len(resultado)):
                  print("{:<4} {:<10} {:<8} ".format(resultado[item][0], resultado[item][1], resultado[item][2]))
    
      elif tabela == 'aluno': # Realizar pesquisa na tabela aluno
          c.execute("SELECT * FROM aluno;")
          resultado = c.fetchall()
          if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<4} {:<8} {:<13} {:<12} {:<10}".format("Matricula", "Nome","CPF",'Data Nasc','Curso'))
            print(f"{Cores.ENDC}")
            for item in range(len(resultado)):
               print("{:<9} {:<8} {:<13} {:<12} {:<7}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4]))

      elif tabela == 'dataProva': # Realizar pesquisa na tabela aluno
          c.execute("SELECT * FROM dataProva;")
          resultado = c.fetchall()
          if resultado:
                print(f"{Cores.BOLD}{Cores.OKGREEN}")
                print("{:<4} {:<10} {:<10} {:<10} {:<6} {:<7} {:<7} {:<7}".format("ID","nota Obtida", "Data Realizada", "Matéria", "Matrícula", "idProf", "idAvaliacao", "Situacao"))
                print(f"{Cores.ENDC}")
                for item in range(len(resultado)):
                    print("{:<8} {:<8} {:<14} {:<10} {:<11} {:<9} {:<5} {:<10}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4], resultado[item][5], resultado[item][6], resultado[item][7]))

      elif tabela == 'tipo': # Realizar pesquisa na tabela professor
          c.execute("SELECT * FROM tipo;")
          resultado = c.fetchall()
          if resultado:
              print(f"{Cores.BOLD}{Cores.OKGREEN}")
              print("{:<4} {:<7} ".format("ID", "Tipo de Prova"))
              print(f"{Cores.ENDC}")
              for item in range(len(resultado)):
                  print("{:<4} {:<10}".format(resultado[item][0], resultado[item][1]))

  except Error as e:
      print(e)
  else:
      print(f"{Cores.BOLD}{Cores.OKGREEN}Atualização com sucesso em {tabela}.{Cores.ENDC}")
      input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

def excluir(tabela, conn):
  try:
      c = conn.cursor()
      if tabela == 'avaliacao': # Excluir dados da tabela avaliação
          pesquisar(tabela, conn)
          x = input("Informe o id da Avaliação a excluir: ")
          avaliacao = (x)
          c.execute("DELETE FROM avaliacao WHERE idavaliacao=?;", avaliacao)	
          conn.commit()
      elif tabela == 'professor': # Excluir dados da tabela professor
          pesquisar(tabela, conn)
          x = input("Informe o id do Professor para excluir: ")
          professor = (x)
          c.execute("DELETE FROM professor WHERE idProf=?;", professor)	
          conn.commit()
      elif tabela == 'aluno': # Excluir dados da tabela aluno
          pesquisar(tabela, conn)
          x = input("Informe o id do Aluno a excluir: ")
          aluno = (x)
          c.execute("DELETE FROM aluno WHERE matricula=?;", aluno)	
          conn.commit()
      elif tabela == 'dataProva': # Excluir dados da tabela dataProva
          pesquisar(tabela, conn)
          x = input("Informe o id da prova realizada a excluir: ")
          realProva = (x)
          c.execute("DELETE FROM dataProva WHERE idDataProva=?;", realProva)	
          conn.commit()
      elif tabela == 'dataProva': # Excluir dados da tabela tipo
          pesquisar(tabela, conn)
          x = input("Informe o id do tipo a ser excluido: ")
          tipo = (x)
          c.execute("DELETE FROM tipo WHERE idTipo=?;", tipo)	
          conn.commit()
  except Error as e: 
        print(e)
  else:
        print(f"{Cores.BOLD}{Cores.OKGREEN}Atualização com sucesso em {tabela}.{Cores.ENDC}")
        input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

def pesquisarAluno(tabela, conn): #Pesquisa Aluno Unico
  try:
    c = conn.cursor()
    if tabela == 'aluno':
      matricula = input("Matrícula: ")
      c.execute(
      "SELECT * FROM aluno WHERE matricula like (?);", matricula)
      resultado = c.fetchall()
      if resultado:
        print(f"{Cores.BOLD}{Cores.OKGREEN}")
        print("{:<4} {:<10} {:<10} {:<10} {:<6}".format("Matrícula", "Nome", "CPF", 'Data Nasc','Curso'))
        print(f"{Cores.ENDC}")
      for item in range(len(resultado)):
          print("{:<8} {:<8} {:<13} {:<10} {:<7}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4]))
      else:
        print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")

  except Error as e:
    print(e)
  else:
    print(f"{Cores.BOLD}{Cores.OKGREEN}Pesquisa realizada com sucesso em {tabela}.{Cores.ENDC}")
    input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")    
      
def pesquisaEsp(tabela, conn, faixaPesq):
  try:
      c = conn.cursor()  
      if faixaPesq == 'periodo':
          periodoIn = input('Informe a data inicial da pesquisa: ')
          periodoFin = input('Informe a data final da pesquisa: ')
          opcao = (periodoIn, periodoFin)
          c.execute("Select * from dataProva where dataProva >= ? and dataProva <= ?", opcao)
          resultado = c.fetchall()
          if resultado:
                print(f"{Cores.BOLD}{Cores.OKGREEN}")
                print("{:<4} {:<10} {:<10} {:<10} {:<6} {:<7} {:<7} {:<7}".format("ID","nota Obtida", "Data Realizada", "Matéria", "Matrícula", "idProf", "idAvaliacao", "Situacao"))
                print(f"{Cores.ENDC}")
                for item in range(len(resultado)):
                    print("{:<8} {:<8} {:<13} {:<10} {:<7} {:<7} {:<7} {:<7}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4], resultado[item][5], resultado[item][6], resultado[item][7]))

      elif faixaPesq == 'prof':
          tabela = 'professor'
          pesquisar(tabela,conn)
          prof = input('Informe o id do professor a ser pesquisado: ')
          opcao = prof
          c.execute("Select * from dataProva where idProf = ?", opcao)
          resultado = c.fetchall()
          if resultado:
                print(f"{Cores.BOLD}{Cores.OKGREEN}")
                print("{:<4} {:<10} {:<10} {:<10} {:<6} {:<7} {:<7} {:<7}".format("ID","nota Obtida", "Data Realizada", "Matéria", "Matrícula", "idProf", "idAvaliacao", "Situacao"))
                print(f"{Cores.ENDC}")
                for item in range(len(resultado)):
                  print("{:<8} {:<9} {:<15} {:<111} {:<7} {:<7} {:<7} {:<7}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4], resultado[item][5], resultado[item][6], resultado[item][7]))

      elif faixaPesq == 'tipo':
          tabela = 'tipo'
          pesquisar(tabela,conn)
          tipo = input('Informe o id do tipo de prova a ser pesquisado: ') 
          opcao = tipo
          c.execute("Select * from avaliacao where idTipo = ?", opcao)
          resultado = c.fetchall()
          if resultado:
              print(f"{Cores.BOLD}{Cores.OKGREEN}")
              print("{:<4} {:<5} {:<10} {:<8} {:<10}  {:<12} {:<10} {:<10}".format("ID", "Mat","EAD/PRES",'Nota Min','Nota Max','Nota Aprov','Data', 'idTipo'))
              print(f"{Cores.ENDC}")
              for item in range(len(resultado)):
                  print("{:<4} {:<7} {:<8} {:<10} {:<10} {:<10} {:<11} {:<9}".format(resultado[item][0], resultado[item][1], resultado[item][2],resultado[item][3], resultado[item][4],resultado[item][5],resultado[item][6],resultado[item][7]))
          
      else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
  except Error as e:
        print(e)
  else:
        print(f"{Cores.BOLD}{Cores.OKGREEN}Pesquisa com sucesso em {tabela}.{Cores.ENDC}")
        input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

def listarSemAvaliacao(tabela, conn):
  try:
      c = conn.cursor()  
      if tabela == 'aluno':
        c.execute("Select a.matricula, a.nome from aluno a where a.matricula NOT IN(Select matricula from dataProva)")

#Select * from Tabela1 where Tabela1.ID NOT IN (Select ID * from Tabela2) inner join, infos diferentes nas tableas

        resultado = c.fetchall()
        if resultado:
          print(f"{Cores.BOLD}{Cores.OKGREEN}")
          print("{:<8} {:<8}".format("Matricula","Nome do aluno"))
          print(f"{Cores.ENDC}")
          for item in range(len(resultado)):
            print("{:<8} {:<8}".format(resultado[item][0], resultado[item][1]))
      else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
  except Error as e:
        print(e)
  else:
        print(f"{Cores.BOLD}{Cores.OKGREEN}Pesquisa com sucesso em {tabela}.{Cores.ENDC}")
        input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

def listarNotas(tabela, conn):
  try:

      c = conn.cursor()  
      if tabela == 'aluno':
        notaMinima = input('Informe a nota inicial da pesquisa: ')
        notaMaxima = input('Informe a nota final da pesquisa: ')
        opcao = (notaMinima, notaMaxima)
        c.execute("Select a.nome, dp.notaObt from aluno a LEFT JOIN dataProva dp ON a.matricula = dp.matricula where notaObt >= ? and notaObt < ? ", opcao)
        resultado = c.fetchall()
        if resultado:
          print(f"{Cores.BOLD}{Cores.OKGREEN}")
          print("{:<8} {:<8}".format("Nome do aluno", "Nota Obtida"))
          print(f"{Cores.ENDC}")
          for item in range(len(resultado)):
            print("{:<14} {:<14}".format(resultado[item][0], resultado[item][1]))

      else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
  except Error as e:
        print(e)
  else:
        print(f"{Cores.BOLD}{Cores.OKGREEN}Pesquisa com sucesso em {tabela}.{Cores.ENDC}")
        input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

def listarSituacao(tabela, conn):
  try:

      c = conn.cursor()  
      if tabela == 'aluno':
        verSit = input('Especifique a situação escolhida(Reprovado/IFA/Aprovado): ')
        c.execute("Select a.nome, dp.notaObt, dp.situacao from aluno a LEFT JOIN dataProva dp ON a.matricula = dp.matricula where situacao like ? ", ('%'+verSit+'%',))
        resultado = c.fetchall()
        if resultado:
          print(f"{Cores.BOLD}{Cores.OKGREEN}")
          print("{:<4} {:<8} {:<14}".format("Nome do aluno", "Nota Obtida", "Situação"))
          print(f"{Cores.ENDC}")
          for item in range(len(resultado)):
            print("{:<16} {:<8} {:<4}".format(resultado[item][0], resultado[item][1], resultado[item][2]))

      else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
  except Error as e:
        print(e)
  else:
        print(f"{Cores.BOLD}{Cores.OKGREEN}Pesquisa com sucesso em {tabela}.{Cores.ENDC}")
        input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")
