import sqlite3

def connect():
    return sqlite3.connect('cockmon.db')

def create_table():

    connection = connect();
    cursor = connection.cursor();

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS cockmon(
                   nome TEXT NOT NULL,
                   tipo TEXT NOT NULL,
                   vida INTEGER NOT NULL,
                   exp INTEGER NOT NULL,
                   lvl INTEGER NOT NULL)
        ''')
    connection.commit()
    connection.close()

def create_cockmon():
    cockName = str(input("|-> Cual o nome de seu CockMon?: "))
    cockType = str(input("|-> Cual o tipo do seu CockMon?: "))
    cockLife = int(input("|-> Cuanto de vida tem o seu CockMon?: "))
    cockExp = 0
    cockLvl = int(input("|-> Qual é o nível inicial de seu CoclMon?: "))



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
    print("--- COCKMON CRIADO COM SUCESSO!! ---")

def  view_cockmon():
    connection = connect();
    cursor = connection.cursor();
    
    


create_table();
create_cockmon();