class File:
    def __init__(self):
        pass       

    #la funzione prende come parametro il nome del file, lo legge e splitta in base al nome del file dato 
    #che ho un numero e un tipo di parametri differenti in base al file che leggo
    def leggiFile(nome_file):
        f = open(nome_file)
        file = str(f.read())
        print(file)
        file_split = file.split(';')
        print(file_split)   

        #in base al file che leggo ritorno valori diversi
        if (nome_file == "confServer.txt"):
            host = file_split[0]
            port = int(file_split[1])
            contenuto_file = host, port
        elif(nome_file == "confClient.txt"):
            host = file_split[0]
            port = int(file_split[1])
            comando = file_split[2]
            contenuto_file = host, port, comando
        return contenuto_file

    #richiede in input nome utente e contenuto da inviare al server 
    def valori_input():
        nome_utente = input("Inserisci il tuo nome utente>> ")
        contenuto = input("Inserisci il contenuto da inviare>> ")
        return nome_utente, contenuto

