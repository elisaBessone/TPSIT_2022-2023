"""Documentazione ufficiale Flask>> https://flask.palletsprojects.com/en/2.2.x/quickstart/"""
from flask import Flask, request

app = Flask(__name__)

#DECORETOR: prende in input la funzione somma, esegue codice prima e dopo essa. il valore di ritorno è un'altra funzione
@app.route('/', methods=['GET'])
def somma():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        c = a + b
        return str(c)
    except:
        return "Errore!!"
    """return "<h1>Faccio la somma</h1>"""


if __name__ == '__main__':
    app.run()



# RICHIESTA HTTP = http://localhost:5000/?a=2&b=7      --> 9            è andata a buon fine la richiesta
# RICHIESTA HTTP = http://localhost:5000/?a=2&b=fhbsd  --> Errore!!     non è andata a buon fine la richiesta
