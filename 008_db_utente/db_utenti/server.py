from socket import socket, AF_INET, SOCK_STREAM
import sqlite3 as sql
BUFFER_SIZE = 1024

listaUsername = []

def leggo_lista_username(conn):
    listaUsername.clear()
    curs = conn.cursor()
    curs.execute("SELECT * FROM UTENTI")
    print("dati database - utenti.db")
    for i in curs.fetchall():
        listaUsername.append(i[0])
        print(i[0], i[1])
    print(listaUsername)
    print("---------------------------\n")
    return listaUsername

#effettuo il login con il db
def login(conn, nome_utente, psw_utente):
    curs = conn.cursor()
    login_status = curs.execute('''SELECT * FROM UTENTI WHERE nome=? and password=?''', (nome_utente,psw_utente))
    if len(login_status.fetchall()) == 1:
        return True
    else:
        return False


#iscrivo al db
def signup(conn, nome_utente, psw_utente):
    curs = conn.cursor()
    curs.execute("INSERT into UTENTI(nome, password) VALUES (?,?)", (nome_utente, psw_utente))
    conn.commit()    #eseguo la query

def cercaUtenti(conn, str):
    print("cerca utenti")
    utenti = ""
    curs = conn.cursor()
    searchUtenti = curs.execute('''SELECT nome FROM UTENTI WHERE (%s) LIKE ?''', %nome, (str,))

    #if len(searchUtenti.fetchall()) == 1:
    for i in searchUtenti.fetchall():
        utenti = utenti + ";" + i
        print(utenti)

    return utenti


def server():
    with socket(AF_INET, SOCK_STREAM) as s:

        s.bind(("0.0.0.0", 5000))

        s.listen()
        print("Server in ascolto...\n")
        while True:
            client, address = s.accept()
            #passo come stringa il nome dei mio database per poterlo connettere -- connessione al db.
            conn = sql.connect("utenti.db")   
            #svuoto la lista per non avere ripetizioni ogni volta che leggo il db
            listaUsername = leggo_lista_username(conn)
        
            msg = client.recv(BUFFER_SIZE)
            msg = msg.decode('utf-8')
            comando, nome_utente, psw_utente = msg.split(";")[0], msg.split(";")[1], msg.split(";")[2]
            print(f"MESSAGGIO RICEVUTO DALL'UTENTE >> {comando}, {nome_utente}, {psw_utente}")       


            if comando.upper() == "LOGIN":
                print("<<login>>")
                if login(conn, nome_utente, psw_utente):
                    client.sendall(f"Login avvenuto.".encode("utf-8"))

                    stringa = client.recv(BUFFER_SIZE).decode("utf-8")
                    print(stringa)

                    utenti = cercaUtenti(conn, stringa)
                    #ricerco nomi con stringa dentro
                    """for username in listaUsername:
                        if username.count(stringa) == 1:    #se la stringa è presente nello username la invio al client per visualizzarla 
                            utenti = utenti + ";" + username """


                    if utenti == "":
                        client.sendall(f"La stringa {stringa} non è contenuta in nessun username.".encode("utf-8"))
                    else:   
                        client.sendall(f"La stringa {stringa} è contenuta in >> {utenti}".encode("utf-8"))


                else:
                    client.sendall("Login fallito...".encode("utf-8"))
                    
            elif comando.upper() == "SIGNUP":
                print("<<signup>>")
                #se il nomeutente è già presente non lo inserisco e invio un messaggio di errore.
                if nome_utente in listaUsername:
                    client.sendall("Username già in uso...".encode("utf-8"))
                else:
                    #aggiorno la lista contenente tutti gli username.
                    listaUsername.append(nome_utente) 
                    print(listaUsername)
                    signup(conn, nome_utente, psw_utente)
                    client.sendall("Signup effettuato.".encode("utf-8"))


            conn.close()

            
if __name__ == "__main__":
    server()