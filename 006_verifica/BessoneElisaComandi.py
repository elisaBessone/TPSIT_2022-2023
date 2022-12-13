class Comandi:
    #imposto dei comandi predefiniti per facilitare la scrittura del codice
    LEGGI = "leggi"
    SALVA = "salva"
    ESCI = "esci"

    #non usata, controllo del comando scritto su file
    def controllo_comandi(comando):
        if comando == Comandi.LEGGI or comando == Comandi.SALVA:
            comando = True
        else:
            comando = False
        return comando