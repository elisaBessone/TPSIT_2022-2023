import threading
import time

luc = threading.Lock()

def funzione():
    print(f"Partenza del {threading.current_thread().name}")
    #print(f"Partenza del thread{num}")
    print(f"Elaboro....{threading.current_thread().name}")
    time.sleep(1)
    print(f"Finito lavoro thread{threading.current_thread().name}")


def main():
    #t = threading.Thread(target=funzione)  #devo dire quale metodo
            #deve far partire il mio threas, gli passo come parametro:funzione
    
    t = threading.Thread(target=funzione, name = "Primo")  #args per dire che parametro passo al thread
    t.start()   #capisce che deve far partire il metodo run

    q = threading.Thread(target=funzione, name = "Secondo")   # , args=(2,))
    q.start() 

    funzione()
    print("fine chiamata main")

if __name__ == "__main__":
    main()