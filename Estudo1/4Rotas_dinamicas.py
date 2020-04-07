          ########## Rotas Dinâmicas ##########

# A segunda versão da aplicação , que vamos ver,acrescenta uma segunda rota
# que é dinâmica.Ao acessar o URL dinâmico em seu navegador, agente verá uma
# saudação personalizada que inclui o nome fornecido no URL.

from flask import Flask

app = Flask(__name__)

nome = 'Gabriel'

@app.route('/usuario/<nome>')
def index(name):
    return '<h1>Hello, {}!</h1>'.format(nome)

app.run()

#quando rodar o programa,tem que colocar manualmente na barrade pesquisa,
#aparte de usuario e de nome, @app.route('/usuario/<nome>'),está parte
#que neste caso,na barra de pesquisa deve ficar
#http://127.0.0.1:5000/user/Gabriel