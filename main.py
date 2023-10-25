from flask import Flask, render_template, request, redirect


class Dados():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


listaDeDados = []

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lista')
def lista():
    return render_template('dadosCadastrados.html', titulo= "Dados Cadastrados", dados= listaDeDados)


@app.route('/criar', methods =['POST',])
def criar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    dado = Dados(nome,sobrenome)
    listaDeDados.append(dado)
    return redirect("/lista")



app.run(debug=True)