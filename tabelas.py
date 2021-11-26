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
            dataNasc = input("Data de nascimento: ").title()          
            siglaCurso = input("Curso matriculado: ").upper()
            situacao = input("Situação do aluno:").title()
            criado_em = date.today()
            alunoNovo = (nome, cpf, dataNasc, siglaCurso, situacao, criado_em)
            c.execute("INSERT INTO aluno (nome, cpf, dataNasc, siglaCurso, situacao, criado_em) VALUES (?, ?, ?, ?, ?, ?);", alunoNovo)
            conn.commit()  # Gravar o novo aluno no BD
            print(f"{Cores.BOLD}{Cores.OKGREEN}Inserção com sucesso em {tabela}.{Cores.ENDC}")
      
        elif tabela == 'tipo':  #cadastrar tipo de prova
            materia = input("Matéria: ").upper()
            descricao = input("Descrição (P1, P2, IFA): ").title()
            criado_em = date.today()
            tipoNovo =(materia, descricao, criado_em)
            c.execute("INSERT INTO tipo (materia, descricao, criado_em) VALUES (?, ?, ?);", tipoNovo)
            conn.commit()  # Gravar o novo tipo de prova no BD
            print(f"{Cores.BOLD}{Cores.OKGREEN}Inserção com sucesso em {tabela}.{Cores.ENDC}") 
        
        elif tabela == 'professor':  #Cadastrar professor no BD
            nome = input(" Nome do professor: ").title()
            materia = input("Matéria: ").upper()
            criado_em = date.today()
            profNovo = (nome, materia, criado_em)
            c.execute("INSERT INTO professor (nome, materia, criado_em) VALUES (?, ?, ?);", profNovo)
            conn.commit()  # Gravar o novo professor no BD
            print(f"{Cores.BOLD}{Cores.OKGREEN}Inserção com sucesso em {tabela}.{Cores.ENDC}") 
    
        elif tabela == 'avaliacao':  #Cadastrar avaliações no BD
            siglaMat = input("Matéria: ").upper()
            descricao = input("Descrição de como será realizada a prova: ").title()
            notaMin = input("Nota mínima: ").title()  
            notaMax = input("Nota máxima: ").title()
            notaAprov = input("Nota de aprovação: ").title()        
            dataPrevista = input("Data de realização: ").title()
            criado_em = date.today()
            avaliacaoNovo =(siglaMat, descricao, notaMin, notaMax, notaAprov, dataPrevista, criado_em)
            c.execute("INSERT INTO avaliacao (siglaMat, descricao, notaMin, notaMax, notaAprov, dataPrevista, criado_em) VALUES (?,?,?,?,?,?,?);", avaliacaoNovo)
            conn.commit()  # Gravar novas avaliações no BD
            print(f"{Cores.BOLD}{Cores.OKGREEN}Inserção com sucesso em {tabela}.{Cores.ENDC}") 
        
        elif tabela == 'dataProva':  #Cadastrar dataProva (relação M:N aluno/Avaliação) no BD
            siglaMat = input("Matéria: ").upper()
            notaObt = input("Nota obtida: ").title()   
            dataProva = input("Data em que foi realizada: ").title()
            criado_em = date.today()
            dataProvaNovo =(siglaMat, notaObt, dataProva, criado_em)
            c.execute("INSERT INTO dataProva (siglaMat, notaObt, dataProva, criado_em) VALUES (?, ?, ?, ?);", dataProvaNovo)
            conn.commit()  # Gravar novas avaliações no BD
            print(f"{Cores.BOLD}{Cores.OKGREEN}Inserção com sucesso em {tabela}.{Cores.ENDC}")    
        
    except Error as e:
        print(e)
    else:
        input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

#alterar cadastro de aluno   
def atualizar(tabela, conn):
    try:
        c = conn.cursor()
        if tabela == 'avaliacao':
            pesquisar(tabela, conn)
            x = input("Informe o ID da avaliação : ")

            siglaMat = input('\nMatéria da prova: ').upper()

            descricao = input('\nForma como será realizada a prova: ').upper()

            notaMin = input('\nNota Minima : ').title()

            notaMax = input('\nNota maxima : ').title()

            notaAprov = input('\nNota de aprovação : ').title()

            dataPrevista = input('\nData Prevista : ').title()

            avaliacao = (siglaMat, descricao, notaMin, notaMax, notaAprov, dataPrevista ,x)

            c.execute("UPDATE avaliacao SET siglaMat =?, descricao =?, notaMin =?, notaMax =?, notaAprov =?, dataPrevista =? WHERE idAvaliacao=?;", avaliacao)
            conn.commit()

        elif tabela == 'dataProva':
            id = input("Informe o ID da avaliação realizada : ")
            notaObt = input("Nota obtida pelo aluno: ").title()   

            dataProva = input("Data em que foi realizada: ").title()

            avaliacaoData = (notaObt, dataProva, id)

            c.execute("UPDATE avaliacao SET notaObt=?, dataProva=? WHERE idDataProva=?;", avaliacaoData)
            conn.commit()
    
        elif tabela == 'professor':
            pesquisar(tabela, conn)
            id = input("Informe o Id do professor: ").title()
            nome = input("Informe o Nome do professor: ").title()
            materia = input('Informe a sigla da materia: ').title()
            professor = (nome, materia,id)
            c.execute("UPDATE professor SET nome=?, materia=? WHERE idProf=?;", professor)
            conn.commit()
        
        elif tabela == 'aluno':
            pesquisar(tabela, conn)
            id = input("Informe a matricula do aluno: ").title()
            nome = input("Informe o Nome do aluno: ").title()
            cpf = input("Informe o CPF do aluno: ").title()     
            DataNasc = input("Informe a data de nascimento do aluno: ").title()
            siglaCurso = input("Informe a sigla do curso do aluno: ").upper()
            situacao = input("Informe a situação do aluno: ").title()
      
            aluno = (nome, cpf,DataNasc, siglaCurso,situacao,id)

            c.execute("UPDATE aluno SET nome =?, cpf =?, DataNasc =?, siglaCurso =?, situacao =? WHERE matricula=?;", aluno)
            conn.commit()

        elif tabela == 'dataProva':
            pesquisar(tabela, conn)
            id = input("Informe o Id da realização da prova: ").title()
            dataProva = ('Informe a data em que a prova foi realizada: ').title()
            notaObt = input("\nInforme a nota obtida pelo aluno: ").title()
            realProva = (dataProva, notaObt,id)
            c.execute("UPDATE professor SET dataProva=?, notaObt=? WHERE idDataProva=?;", realProva)
            conn.commit()
    except Error as e:
        print(e)
    else:
        print(f"{Cores.BOLD}{Cores.OKGREEN}Atualização com sucesso em {tabela}.{Cores.ENDC}")
        input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

def pesquisar(tabela, conn):
    try:
        c = conn.cursor()
      
        if tabela == 'avaliacao':
            c.execute("SELECT * FROM avaliacao;")
            resultado = c.fetchall()
      
        if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<4} {:<7} {:<8} {:<10} {:<10} {:<12} {:<10}".format("ID", "Mat", "A maneira", 'Nota Min','Nota Max','Nota Aprov','Data'))
            print(f"{Cores.ENDC}")
            for item in range(len(resultado)):
                print("{:<4} {:<10} {:<8} {:<10} {:<10} {:<8} {:<7}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4],resultado[item][5],resultado[item][6]))
            
        if tabela == 'professor':
            c.execute("SELECT * FROM professor;")
            resultado = c.fetchall()
        if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<4} {:<7} {:<8} ".format("ID", "Nome", "Matéria"))
            print(f"{Cores.ENDC}")
            for item in range(len(resultado)):
                print("{:<4} {:<10} {:<8} ".format(resultado[item][0], resultado[item][1], resultado[item][2]))

        if tabela == 'aluno':
            c.execute("SELECT * FROM aluno;")
            resultado = c.fetchall()
        if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<4} {:<10} {:<10} {:<10} {:<6} {:<5}".format("Matrícula", "Nome", "CPF", 'Data Nasc','Curso','Situação'))
            print(f"{Cores.ENDC}")
            for item in range(len(resultado)):
                print("{:<8} {:<8} {:<13} {:<10} {:<7} {:<3}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4],resultado[item][5]))
    except Error as e:
        print(e)
    else:
        print(f"{Cores.BOLD}{Cores.OKGREEN}Atualização com sucesso em {tabela}.{Cores.ENDC}")
        input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

def excluir(tabela, conn):
    try:
        c = conn.cursor()
        if tabela == 'avaliacao':
            pesquisar(tabela, conn)
            x = input("Informe o id da Avaliação a excluir: ")
            avaliacao = (x)
            c.execute("DELETE FROM avaliacao WHERE idavaliacao=?;", avaliacao)	
            conn.commit()
        elif tabela == 'professor':
            pesquisar(tabela, conn)
            x = input("Informe o id do Professor para excluir: ")
            professor = (x)
            c.execute("DELETE FROM professor WHERE idProf=?;", professor)	
            conn.commit()
        elif tabela == 'aluno':
            pesquisar(tabela, conn)
            x = input("Informe o id do Aluno a excluir: ")
            aluno = (x)
            c.execute("DELETE FROM aluno WHERE matricula=?;", aluno)	
            conn.commit()
    except Error as e: 
        print(e)
    else:
        print(f"{Cores.BOLD}{Cores.OKGREEN}Atualização com sucesso em {tabela}.{Cores.ENDC}")
        input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")
      
      
def mostrarTudo(tabela, conn):
    try:
        c = conn.cursor()  
        if tabela == 'aluno':
            c.execute('SELECT matricula, aluno.nome, professor.nome,notaObt.dataProv FROM aluno INNER JOIN professor ON professor.materia = aluno.materia INNER JOIN notaObt ON dataPrev.materia = aluno.materia')
            resultado = c.fetchall()
        if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<4} {:<7} {:<8} {:<10} {:<10}".format("Aluno", "Mat", "Professor", 'Data Prova', 'Nota Obt'))
            print(f"{Cores.ENDC}")
            for item in range(len(resultado)):
                print("{:<4} {:<10} {:<8} {:<10} {:<10}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4]))
        else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
    except Error as e:
        print(e)
    else:
        input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")