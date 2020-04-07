          ########## Uma Aplicação Completa ##########
# As linhas de código a baixo vão definir uma instância  de reaplicação,
#além de uma rota única e função  de view.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Primeiro teste e com Sucesso!</h1>'

if __name__ == '__main__':
    app.run()

