"""Proseguire l’esercizio sul login iniziato in classe, il server si occupa di gestire il DB. Il
server può ricevere tre comandi:
• signup: vengono inviati un nome utente e una password e viene salvato nel DB
• login: vengono inviati nome utente e password, il server risponde se il login ha
avuto successo
Se il login ha avuto successo il server permette al client di effettuare la ricerca dei nomi
utente che contengono una stringa. Il server, una volta completata una richiesta deve
rimanere in ascolta per un’altra
Parte dell’esercizio è documentarsi su come realizzare le parti che non abbiamo visto in
classe (e.g. leggere il risultato di una query)
Di seguito alcuni alcuni esempi di scambi di messaggi tra client e server (i messaggi sono
solo di esempio, modificare il formato con cui inviare e ricevere dati come si preferisce)."""

import sqlite3 as sql 

def signup():
    #invio nome utente e password e salvo nel db
    print("signup")

def login():
    #invio nome utente e password, il db risponde se è avvenuto con successo
    #se successo
    # PERMETTO AL CLIENT DI EFFETTUARE UNA RICHIESTA DEVE RIMANERE IN ASCOLTO PER UN'ALTRA
    print("login")
    


def inserisciUtente():
    conn = sql.connect("./utenti.db")   #passo come stringa il nome dei mio database per poterlo connettere 

    nome_utente= input("Inserisci username>> ")
    psw_utente = input("Inserisci password>> ")

    curs = conn.cursor()
    curs.execute("INSERT into UTENTI(nome, password) VALUES (?,?)", (nome_utente, psw_utente))
    conn.commit()    #eseguo la query
    conn.close()  #chiudo il database


if __name__ == "__main__":
    inserisciUtente()