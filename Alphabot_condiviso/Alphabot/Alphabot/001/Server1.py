#!/usr/bin/python
# _*_ coding: utf-8 -*-
#server tpc

import socket as sck
import threading as thr
import time
#from Alphabot1 import AlphaBot
from Packet import Packet
#import RPi.GPIO as GPIO

#import sqlite3 #libreria data base
BUFFER_SIZE = 4096
TEMPO_PER_CURVARE_DI_90_GRADI = 0.5

#classe thread
#funzione che si avvia alla creazione della classe
def __init__(self, connessione, indirizzo ,alphabot):
    thr.Thread.__init__(self)   #costruttore super (java)
    self.connessione = connessione
    self.indirizzo=indirizzo
    self.alphabot=alphabot          #per usare la classe del robot all'interno del thread
    self.running = True

#funzione che si avvia con il comando start()
def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM) 
    s.bind(('0.0.0.0', 5000))       #bind del server tcp
    s.listen()
    #Ab = AlphaBot()      #inizzializzo alphabot

    running = True
    
    connessione, indirizzo = s.accept()   #connessioni dei client
     
    #client = Classe_Thread(connessione, indirizzo, Ab)
    #mettere codice run
    while running:     #ciclo infinito del programma
        
        messaggio_ricevuto = s.recvfrom(BUFFER_SIZE)#(connessione.recv(4096)).decode("utf-8")
        pkt_movimento = Packet.from_bytes(messaggio_ricevuto[0])
        print(pkt_movimento)
        pkt_durata = Packet.from_bytes(messaggio_ricevuto[1])
        print(pkt_durata)
        
        #pkt_durata = (connessione.recv(4096)).decode("utf-8") #ricevo il comando

        if pkt_movimento == 'exit':             #per chiudere il programma e scollegare i client
            running = False

            lista_client.remove()
            
        else:
            print(f"comando: {pkt_movimento} con pkt_durata: {pkt_durata} secondi")
                    
            if pkt_movimento.upper().startswith("W"): #avanti
                #Ab.forward()
                time.sleep(int(pkt_durata))        #pkt_durata del pkt_movimento
                #Ab.stop()
            if pkt_movimento.upper().startswith("D"): #destra
                #Ab.right()
                time.sleep(int(pkt_durata))   
                #Ab.stop()
            if pkt_movimento.upper().startswith("S"): #indietro
                #Ab.backward()
                time.sleep(int(pkt_durata))   
                #Ab.stop()
            if pkt_movimento.upper().startswith("A"): #sinistra
                #Ab.left()
                time.sleep(int(pkt_durata))   
                #Ab.stop()
            if pkt_movimento.upper().startswith("ESCI"): #fermo
                #Ab.stop()
                print("stop")
    s.close()

if __name__ == "__main__":
    lista_client = []   
    main()