"""Documentazione ufficiale Flask>> https://flask.palletsprojects.com/en/2.2.x/quickstart/"""
from flask import Flask, request

app = Flask(__name__)

#DECORETOR: prende in input la funzione somma, esegue codice prima e dopo essa. il valore di ritorno è un'altra funzione
#richiesta in GET
@app.route('/somma', methods=['GET'])
def sommaGet():
    try:
        a = int(request.args.get('txtA'))
        b = int(request.args.get('txtB'))
        c = a + b
        return str(c)
    except:
        return "Errore!!"
    """return "<h1>Faccio la somma</h1>"""

#richeista in POST
@app.route('/somma', methods=['POST'])
def sommaPost():
    try:
        a = int(request.form.get('txtA'))
        b = int(request.form.get('txtB'))
        c = a + b
        return str(c)
    except:
        return "Errore!!"
    """return "<h1>Faccio la somma</h1>"""


@app.route('/', methods=['GET'])
def homepage():
    return("""
        <html>
            <body>
                <form action="/somma" method="POST">
                    <label for="primoNumero">Primo numero> </label>
                    <input type="text" id = "primoNumero" name="txtA"><br>
                    
                    <label for="secondoNumero">Secondo numero> </label>
                    <input type="text" id = "secondoNumero" name="txtB"><br>

                    <input type="submit" value="somma">
                </form>
            </body>
        </html>
    """)

if __name__ == '__main__':
    app.run()



# RICHIESTA HTTP = http://localhost:5000/?a=2&b=7      --> 9            è andata a buon fine la richiesta
# RICHIESTA HTTP = http://localhost:5000/?a=2&b=fhbsd  --> Errore!!     non è andata a buon fine la richiesta
