##### Começando meus estudo sobre Flask ###########
# A meta é criar um progreço que sai do basico e chegue ao avançado

# Uma vez instalado o flask no ambiente global, do python através dp pip3 install Flask

# Vamas importar a Biblioteca Flask e para podermos importar o flask

from flask import Flask

# Agora vamos instanciar o flask, por padrão usamos a variavél app
app = Flask(__name__)
# o único argumento preciso agora para o python é o __name__,esse é valor correto para essse
#argumento __name__,é usado para que o flask determine um lugar para a localização da aplica
#ção ,o que por sua vez permite que localize outros argumentos que façam parte da aplicação
#como ,imagens e templates.


