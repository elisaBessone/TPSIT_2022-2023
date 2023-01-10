import threading
#creo una variabile globale in modo che tutti i threads possano utilizzarla
variable = 0

def thread():
    #incremento numero 10000 volte
    global variable
    print(f"Partenza del {threading.current_thread().name}")
    for _ in range(0,10000):    
        variable = variable + 1
    print(f"Finito lavoro thread{threading.current_thread().name}")

def main():
    #richiamo il thread 1000 volte
    #creo una lista in modo tale da controllare che tutti i thread abbiano finito
    t = []
    for i in range(0,1000):
        t.append(threading.Thread(target=thread, name = f" {i}"))   #non devo mettere le tonde - sbagliato!
        
    for i in range(0,1000):
        t[i].start() 

    for i in range(0,1000):
        t[i].join()    #blocco il programma fino a quando tutti i thread vengono eseguiti completamente
    #devo aspettare che tutti i threads abbiano finito di essere eseguiti
    
    #visualizzo la variabile incrementata
    print(f"VARIABILE>> {variable}")
    
if __name__ == "__main__":
    main()

#FUNZIONE DEPRECATA -- 

