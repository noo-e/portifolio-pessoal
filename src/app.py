from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre-mim.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/contato')
def contatos():
    return render_template('contato.html')

@app.route('/teste')
def teste():
    return render_template('teste.html')

@app.route('/base')
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug = True)