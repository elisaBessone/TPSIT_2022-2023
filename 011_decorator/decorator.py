def inizioFine(func):
    #print , eseguo funzione , fine
    def wrapper():
        print("inizio")
        func()    
        print("fine")
    return wrapper   #ritorno una funzione 

@inizioFine   #DECORATOR>> funzione temporanea, stesso risultato di: ciao = inizioFine(ciao)
def ciao():
    print("Ciao!")
#ciao = inizioFine(ciao)  #assegno una funzione

@inizioFine
def hello():
    print("Hello!")
#hello = inizioFine(hello) 

if __name__ == "__main__":
    ciao()  #eseguo un parte prima e poi una parte dopo la funzione  (inizio , ciao , fine)
    print("-------------------")
    hello()