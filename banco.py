import sqlite3
import time

def connect():
    return sqlite3.connect('cockmon.db')

def create_table():

    connection = connect();
    cursor = connection.cursor();

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS cockmon(
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   tipo TEXT NOT NULL,
                   vida INTEGER NOT NULL,
                   exp INTEGER NOT NULL,
                   lvl INTEGER NOT NULL)
        ''')
    connection.commit()
    connection.close()

def create_cockmon():
    time.sleep(1)
    cockName = str(input("|-> Qual o nome de seu CockMon?: "))
    cockType = str(input("|-> Qual o tipo do seu CockMon?: "))
    cockLife = int(input("|-> Quanto de vida tem o seu CockMon?: "))
    cockExp = 0
    cockLvl = int(input("|-> Qual é o nível inicial de seu CockMon?: "))



    connection = connect();
    cursor = connection.cursor()

    # cursor.execute("""
    #             SELECT nome, tipo, vida, lvl from cockmon

    #         """)

    cursor.execute("""
                INSERT INTO cockmon (nome, tipo, vida, exp, lvl) VALUES (?,?,?,?,?)

            """, (cockName, cockType, cockLife, cockExp, cockLvl))

    connection.commit();
    connection.close();
    time.sleep(0.5)
    print("--- COCKMON CRIADO COM SUCESSO!! ---")


# Função destinada à listar todos os cockmon registrados
def  view_cockmon():
    connection = connect();
    cursor = connection.cursor();

    cursor.execute("""
                Select * from cockmon

            """)

    cock_info = cursor.fetchall();

    # Verificação para caso não haja retorno de dados
    if cock_info:

        # laço for para cada cockmon
        for cocks in cock_info:
            time.sleep(0.5)
            print(f"| ID : {cocks[0]}")
            print(f"| Nome : {cocks[1]}")
            print(f"| Tipo : {cocks[2]}")
            print(f"| Vida : {cocks[3]}")
            print(f"| Exp : {cocks[4]}")
            print(f"| Nível : {cocks[5]}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    else:
        print("Nenhum CockMon encontrado :( ")

    connection.close();

def delete_Cockmon():
    connection = connect();
    cursor = connection.cursor();

    print("|-> Digite o Cockmon que queres que sejá apagado.")
    print("| -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    dlt_answer = input("|-> ")

    cursor.execute('''
                    DELETE from cockmon WHERE ID = ?
            ''', (dlt_answer,))
    cursor.execute('''
                    DELETE FROM sqlite_sequence WHERE name = 'cockmon';
            ''')

    if cursor.rowcount > 0:
        print(f" -- COCKMON APAGADO COM SUCESSO!!! (ID = {dlt_answer}) --")
    else:
        print("Nenhum CockMon encontrado :( ")

    connection.commit();
    connection.close();


    
    
# Função para criar um "Sistema" no terminal
def show_system():
    running = True

    while running:
        time.sleep(1)
        print("x-------------------------------------x")
        print("| - BEM VINDO AO TERMINAL COCKMON! -")
        print("|")
        print("| Informe oque deseja fazer...")
        print("| [1] - Listar CockMon existentes;")
        print("| [2] - Criar/Registrar CockMon;")
        print("| [3] - Apagar CockMon;")
        print("| [4] - Alterar registro CockMon (em Desenvolvimento);")
        print("| [0] - Sair...")
        print("| -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        answer = str(input("| -> "));

        if answer == "1":
            view_cockmon();
        elif answer == "2":
            create_cockmon();
        elif answer == "3":
            delete_Cockmon();
            time.sleep(2)
        elif answer == "4":
            print(">> Função de alterar CockMon em desenvolvimento (eliminar DEV) <<")
            time.sleep(2)

        elif answer == "0":
            print("Encerrando Programa...")
            time.sleep(1)
            running = False
        else:
            print("Valor inválido... Informe um valor dentro da lista de funções.")
            time.sleep(2)

create_table();
show_system();