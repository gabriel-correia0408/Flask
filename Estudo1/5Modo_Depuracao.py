          ######### Modo de Depuração #########

# As aplicações Flask podem,opcionalmente, ser executadas em modo de depuração
#(debug mode).Neste modo,dois módulos muito convenientes do servidor de desen-
#-volvimento,chamados de reloader e debugger,são ativados por padrão.

# Quando o reloader é ativaddo,o Flask observa todos os arquivos de código-fonte
# de seu projeto e reinicia automaticamente o servidor se algum deles for modificado.
# Ter um servidor exexcutando com o roloader ativado,é extramamente conveniente duran-
#-te o desenvolvimento,pois,sempre que voçê modificar e salvar um arquivo,o servidor
#será automaticamente reiniciado levando em conta as aterações.

# O depurador (debugger) é uma ferramenta de web que aparece em seu navegador quando
#a aplicação lança uma exceção não tratada. A janela do navegador web se transfoma em
# um stack trace interativo que permite inspecionar o código-fonte e avaliar expressões
#em qualquer lugar da pilha de chamadas (call stack).


# Para ativar use app,run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Primeiro teste e com Sucesso!</h1>'

FLASK_APP=hello
app.run()
