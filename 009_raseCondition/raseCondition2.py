import threading 
#creo una variabile globale in modo che tutti i threads possano utilizzarla

#classe incrementa 
class Incrementa(threading.Thread):
    def __init__(self, x):
        threading.Thread.__init__(self)
        self.x = x

    def incrementa(self):
        for _ in range(0,10000):
            self.x = self.x + 1

class ThreadIncrementa(threading.Thread):
    def __init__(self, x):
        threading.Thread.__init__(self)
        self.x = x
    def run(self):
        self.x.incrementa()

def main():
    x = Incrementa(0)
    #richiamo il thread 1000 volte
    #creo una lista in modo tale da controllare che tutti i thread abbiano finito
    lista_thread = []
    for i in range(0,1000):
        lista_thread.append(ThreadIncrementa(x))   #oggetto di tipo incrementa. non è più un intero
        
    for t in lista_thread:
        t.start() 

    for t in lista_thread:
        t.join()    #blocco il programma fino a quando tutti i thread vengono eseguiti completamente

    print(f"VARIABILE>> {x.x}")   #per non stampare l'oggetto x.x
    
if __name__ == "__main__":
    main()

#FUNZIONE DEPRECATA -- 