         #############  Rotas e funções de view  #############

# O flask,precisa asber qual código deve ser executado,para cada URL requoisitada,portanto ele
# mantém um mapeamento de URLs, para as funções python, a associação de uma URL para a função
#python é feita (route)



@app.route('/')
def index():
    return '<h>Hollo Word!</h1>'

#Incluir código HTML em strings d erespostas nos arquivos fonte de epython
# resulta em um código de dificil manutenção, esse conceito só foi usado
#para termos um entendimentomelhor sobre respostas.

# se prestarmos atenção algumas URLs de serviço que usamos no dia a dia
#exemplo uma de facebook https://www.facebook.com/<seu-nome>, que tem o nome
#do usuario,fazendo assim que seja diferente para cada usuário.O Flask aceita
#esse tipo de URL usando uma sintaxe do decorador
@app.route('/user/<nome>')
def usuario(nome):
    return '<h1>Hello, {}!</h1>'.format(nome)

# A parte do URL na rota entre os sinais de menor e ,maior é parte dinâmica.Qualquer
#URL que corresponde ás partes estáticas será mapeado para esta rota,
# e quando a função de view for chamada o componente dinâmico será passado como
# argumento.

#Os componentes dinâmicos nas rotas,por padrão,são strings,mas podem também ser
# de outros tipos.Por exemplo,a rota /user/<int:id> corresponderá somente aos URLs
# que tenham um inteiro no segmento dinâmico id.Por exemplo,/user/1123. O Flask aceita
#os tipos string,int,float e path para rotas.O tipo path é um tipo string.

