#def com return
'''
def funcao(arg):
    print(f'voce inseriu o argumento {arg}')
    return arg
funcao(56)
print(funcao('oi'))
'''



#def com uma função assumindo a outra
'''
def div(n1,n2):
    return(n1/n2)
resu = div(6,3)
print(resu)

def outra():
    return div
resul=outra()
print(resul(6,2))
'''


#Exercicios def

#1 -saudação
'''
def saudacao (saudacaao='Olá',nome='Persona'):
    print(saudacaao,nome)
saudacao()
'''
#2 - percentual
'''
def num (n1,n2):
    return n1+(n1*(n2/100))
perc = num(120,40)
print(perc)
'''
#3 - fizzbuzz
'''
def fiz(n):
    if n%2 == 0:
        return('Fizz')
    elif n%5 == 0 and n%3 == 0:
        return ('FizzBuzz')
    elif n%5 == 0:
        return('Buzz')
    else:return(n)
num=fiz(150)
print(num)
'''


#def : *args
# o asterisco empacota e desempacota valores
'''
def func(*args):
    
    #posso mudar a tupla para lista
    #args = list(args)
    
    print(args)
    print(*args,sep='-')
    print(args[0])
func(1,2,3,4,5,76)

#caso colocar uma lista como args, desempacota-la antes

'''


#def : **kwargs

'''
#cria um dicionario com argumentos citados

def func (*args,**kwargs):
    print(args)
    print(kwargs)
    nomes = kwargs.get('nome')
    print(nomes)

func(1,2,3,4,5,nome='ramon',idade='18')
'''


#global variavel
#nao e bom usar
'''
val='valor'
def func():
    print(val)
def func2():
    global val
    val='outro valor'
    print(val)
func()
func2()
print(val)
'''
#bom de usar
'''
def func():
    outra_val='ramon'
    return outra_val
def func2(arg):
    print(arg)
var=func()
func2(var)
'''



#exercicios def dominancia de uma função
'''
def func2():
    return 'conseguiu'
def mestre(funcao):
    return funcao()
exe=mestre(func2)
print(exe)
'''

#exercicios def 2
# RELAÇAO ENTRE FUNÇÕES
'''
def mestre(funcao,*args,**kwargs):
    return funcao(*args,**kwargs)
def func2():
    return 'conseguiu'

def bomdia(nome):
    return f'bom dia {nome}'
def saudacao(saud,nome):
    return f'{saud}, {nome}!!'

exe1=mestre(saudacao,'oiii','ramon')
print(exe1)
'''


#LAMBDA
#OCULTADOR DE FUNÇÃO
#NOME / VARIAVEIS / RETORNO
'''
a= lambda x,y : x*y
print(a(5,7))
'''

#LAMBDA COM ORGANIZAÇÃO DE LISTA
'''
lista = [['P1',13],['P2',6],['P3',7],['P4',50],['P5',8]]
lista.sort(key= lambda item: item[1])
print(lista)
'''


# ORDENAR LISTA DE ACORDO COM VALOR --> SORT
'''
lista = [['P1',13],['P2',6],['P3',7],['P4',50],['P5',8]]

def func(item):
    return item[1]
lista.sort(key=func)
print(lista)
'''

#TUPLA EM LISTA PARA MODIFICAÇÃO
'''
t1=(1,2,3,4,5)
t1=list(1)
t1[1]=3
'''

#DICIONARIO
#POSSIBILIDADES
#  d1, d1.keys or d1.values , d1.items
'''
d1=dict(chave='valor',chave2='valor2')
#ou
d2={'chave':'valor',
    'str':'oiii',
    123:'numeros',
    (1,2,3,4):'lista'}
#criar lista

d1['chave2']='novo'
#ou
d1.update('chave2':'novo')
#adc valor

print(d2.get('str'))
#ou
print(d1['chave'])
#ou se tiver mais valores no item
print(d1['chave'][1])
#printar valor

del d1['chave']
#ou
d1.pop('chave')
#apagar

print('chave' in d1)
print('valor' in d1.keys())
#localização

for k,v in d1.items():
    print(k,v)
#localizar itens 
    
v=d1.copy()
#cria uma copia identica

d1.update(d2)
#juntar dois dic

'''

#DICIONARIOS DENTRO DE DICIONARIOS
'''
clientes = {'cliente1': {'nome':'paulo','sobrenome':'claudiano'},
            'cliente2': {'nome':'ricardo','sobrenome':'claudiano'}}

for clientela , infos in clientes.items():
    print(clientela)
    for nomes,sobrenome in infos.items():
        print(nomes,sobrenome,sep='=')
'''

#LISTA EM DICIONARIO
'''
l=[['c',1],['b',2]]
d1=dict(l)
print(d1)
'''


#TESTE COM PERGUNTAS E RESPOSTAS COM DICIONARIOS
'''
sair=''
while sair != 'S':
    perg={
        'pergunta1':{
            'pergunta':'Qual meu nome',
            'respostas':{'A':'Eduardo','B':'Carlos','C':'Ramon'},
            'resp':'C'
        },
        'pergunta2':{
            'pergunta':'Qual minha idade',
            'respostas':{'A':'34','B':'18','C':'14'},
            'resp':'B'
            }
    }

    for pd,pv in perg.items():
        print(f'{pd}:{pv["pergunta"]}')
        for tv,td in pv["respostas"].items():
            print(f'{tv}:{td}')
        inp =input('\nQual a resposta ? = ')
        if inp == pv['resp']:
            print('ACERT POH !')
        else: print('ERRO BRO')
        print('se liga ai na proxima !')
    sair=input('DESEJA SAIR ? [S] OU [N]')
    '''

#SETS
'''
s1=set()
s1.add(3)

s2={3,4,5}
s2.update('a') #add e itera
s2.update('python') #vai iterar

l1=[1,1,1,2,2,3,4,5,5]
l1=set(l1)
l1=list(l1)
#REMOVEU ELEMENTOS REPETIDOS D LISTA

s1 | l1 #união
s1 & l1 #interseção
s1 ^ l1 #pega elementos que nao estão so em um e nao em ambos
'''



#EXERCICI0 REPETIÇÃO EM LISTAS (fazer com def depois)
'''
l=[
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],]

for td in l:
    t = []
    b = 5
    a = 0
    for num in td:
        if num in t:
            a=num
            b = 0
            print(f'{td} ===> O PRIMEIRO QUE REPETE É {a}')
            break
        t.append(num)
    if b != 0:
        print(f'{td} ===> -1')
'''


#LISTCOMPREE
#EXERCICIO.LISTCOMP
'''
st='012345678901234567890123456789012345678901234567890123456789'

n=10
l1=[(i,i+n) for i in range(0,len(st),n)]
l2=[st[h:j] for h,j in l1]
print(l2)
l3 ='.'.join(l2)
print(l3)
'''


#VERIFICADOR SE É ITERAVEL
'''
l1=[1,2,3,4,5,6]
print(hasattr(l1,'__iter__'))
'''
#VERIFICAR SE É ITERADOR E PEGAR PROXIMO VALOR
'''
l1=iter(l1)
print(next(l1))
print(hasattr(l1,'__next__'))
'''

#GERADOR COM TIME (yield com for)
'''
import sys
import time

def gera():
    for v in range(100):
        yield v
        time.sleep(0.1)
g=gera()
print(next(g))
for n in g:
    print(n)

'''

#GERADOR MANUAL (Armazenar variaveis com yield)
'''
def gera():
    v='valor1'
    yield v
    v = 'valor2'
    yield v
g=gera()
print(next(g)) #retorna valor1
print(next(g)) #retorna valor2
#OU
for n in g:
    print(n)
'''

#GERADOR METODO PARENTESES
#(ECONOMIZA TAMANHO NA MEMORIA)
'''
lista=[x for x in range(1000)]
print(lista)
gera=(x for x in range(1000)) #FORMA UM GERADOR
print(gera)
print(next(gera))
'''


#EXERCICIO CARRINHO COM LISTCOMP
'''
car=[]
car.append(('pt1',30))
car.append(('pt2',30))
car.append(('pt3',50))
total=sum([v for p,v in car ])
print(total)
'''

#ZIP E ZIP_LONGEST
'''
from itertools import *
cdd= ['sao paulo','fortaleza','salvador','monte belo']
est=['SP','CE','BA']
indice=count()
cdd_est2=zip_longest(cdd,est,fillvalue='estado')
cdd_est=zip(indice,cdd,est) #une listas formando um iterador
print(next(cdd_est))
#print(dict(cdd_est))
print(list(cdd_est2))
#zip_longest une ate a maior lista
'''


#EXERCICIO SOMA LISTA
'''
l1=[1,2,3,4,5]
l2=[2,3,4]
l3=zip(l1,l2)
l4=[x+y for x,y in l3]
print(l4)
#ou
l5=[x+y for x,y in zip(l1,l2)]
print(l5)
'''


#COUNT
'''
from itertools import *
conta=count(start=2,step=0.2567)
#print(next(conta))
for i in conta:
    print(round(i,2))
    if i >= 10:
        break
'''


#itertools
'''
from itertools import combinations,count,permutations, product
counta=count(start=1)
pessoas=['ramon','leticia','pedro','jv','luis']
for dupla in combinations(pessoas,2):#SEM REPETIÇÃO
    print(dupla)
    print(next(counta))
for triorep in permutations(pessoas,3): #COM REPETIÇAO EM ORDENS DIFERENTES
    print(triorep)
for quarteto in product(pessoas,repeat=4): # COM REPETIÇAO CONSECUTIVA
    print(quarteto)
'''


#groupby
'''
from itertools import groupby
aluno=[
    {'alunoss':'rodrigo','nota':'D'},
    {'alunoss':'raul','nota':'A'},
    {'alunoss':'renen','nota':'C'},
    {'alunoss':'ramon','nota':'B'}
]
ordena = lambda item:item['nota']
aluno.sort(key=ordena)
aluno_agrup=groupby(aluno,ordena)
for i,k in aluno_agrup:

    print(i)
    for nome in k :
        print(nome)
    print()

    # quant=len(list(k))
    # print(f'{quant} pessoas tiraram {i}')
'''

#MAP: SEMPRE ENTRA COM FUNÇÃO NO PRIMEIRO PARAMETROOOOO
'''
from dados import pessoas, produtos,lista
novalist=map(lambda x: x*2,lista)
novalist2=[x*2 for x in lista]
print(lista)
print(list(novalist))
print(novalist2)
'''
#MAP: retornar valores novos nos dados
'''
from dados import pessoas, produtos,lista

def novosdados(p):
    p['preco']=round(p['preco']*1.05,2)
    return p

novosprod=map(novosdados,produtos) #mapeia buscando valores na lista indicada
for novos in novosprod:
    print(novos)


def novosnomes(nomi):
    nomi['nome']=nomi['nome'].replace('a','@')
    return nomi

novosnomis=map(novosnomes,pessoas)# procura onde tem o argumento passado na funcao
for novosnome in novosnomis:
    print(novosnome)
'''

#FILTER
'''
from dados import pessoas, produtos,lista

#nova_list=[x for x in lista if x>5]
#ou
nova_list=filter(lambda x:x>5,lista)
print(list(nova_list))
'''

#REDUCE: ACUMULA VALORES (SOMA)
'''
from dados import produtos
from functools import reduce
acumula=reduce(lambda ac,i: i['preco']+ac,produtos,0)
print(round(acumula,2))
'''


#TRY E EXCEPT PARA ERROS
'''
try:
    a
    a=[]
    print(a[1])
except NameError as erro:
    print('erro de variavel',erro)
except Exception:
    print('ocorreu outro erro')
finally:pass #sempre e executada
print('continue')
'''


#raise : levanta um erro pedido
'''
def mult(n1,n2):
    if n2==1:
        raise ValueError('erro bro')
    return n1*n2
print(mult(2,1))
'''


#MODULOS
#PARA INSTALAR UM MODULO DIGITA NO TERMINAL ('pip install 'nomedomodulo')
'''
from sys import platform as SO #dar ctrl + space para ver opções
print((SO))
'''

#MEUS MODULOS
#fazer (if __name__ == '__main__': e colocar as ações do modulo de teste)
#pois o mudlo não pode executar nada quando for chamado

#criar modulos e cham-los no programa
#criar packages exclusivos com modulos

#ESCREVER E LER NORMAL
'''
file=open('abc.txt','w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0,0)
print(file.read())
print('#'*40)

file.seek(0,0)
print(file.readline(),end='')
print(file.readline(),end='')
print('#'*40)

file.seek(0,0)
for linha in file.readlines():
    print (linha)
file.close()
'''

#ESCREVER E LER PYTHON
#
# with open('abcd.txt','w+') as filee: #a+ faz adicionar ao arquivo mais texto
#     filee.write('texto1\n')
#     filee.write('texto2\n')
#     filee.write('texto3')
#     filee.seek(0)
#     print(filee.read())

# import os
# os.remove('abcd.txt') #para apagar


#JSON
'''
import json
d1={
    'pessoa1':{'nome':'raue','idade':'3'},
    'pessoa2':{'nome':'rauana','idade':'23'}
}
d1json= json.dumps(d1,indent=True)
print(d1json)

with open('abc.json','w+') as file:
    file.write(d1json)

with open('abc.json','r') as files:
    print(files.read())
    d1json=json.loads(d1json)

for k,b in d1json.items():
    print(k)
    for h,j in  b.items():
        print(h,j)
'''

#DECORADORES
'''
def master(funcao):
    def slave():
        print('decorada')
        funcao()
    return slave

@master
def fala():
    print('hi guys')

# fala=master(fala)

fala()
'''

#EXEMPLO DECORADOR
'''
from time import sleep, time

def velo(funcao):
    def inter(*args,**kwargs):
        comeco=time()
        resultado=funcao(*args,**kwargs) #sempre executar a função com algo mais
        final=time()
        tempo=(final-comeco)
        print(f'a função {funcao.__name__} durou {tempo:.2f} seg')
    return inter

@velo #diz que velo é decorador da funcao
def demora(*args,**kwargs):
    for i in range(5):
        print(i)
        sleep(1)

demora(4354454)
'''

#NAO USAR MUTAVEIS EM PARAMETROS DE FUNÇOES: LISTAS OU DICIONARIOS
#EX: def mudar(lista,lista=[]) xxxxxxxxxxxx


#EXERCICIO UNDO REDO
'''
lista=[]
listaapaga=[]
opcao=0
while opcao!='5':
    def ver (funcao):
        def slave(*args,**kwargs):
            print(f'Essa é sua lista atual :\n{lista}')
            funcao()
        return slave
    @ver
    def verr():
        pass
    @ver
    def adc():
        acao=input('Qual ação deseja adicionar ? : ')
        lista.append(acao)

    def desf():
        cont= len(lista)-1
        itemm=lista[cont]
        listaapaga.append(itemm)
        lista.pop(cont)
        print(f'Essa é sua lista atual :\n{lista}')

    def ref():
        cont = len(listaapaga) - 1
        itemm = listaapaga[cont]
        listaapaga.pop(cont)
        lista.append(itemm)
        print(f'Essa é sua lista atual :\n{lista}')



    print('BEM VINDO A LISTA DE AÇÕES O QUE DESEJA ? :\n\t1)VER LISTA\n\t2)ADICIONAR AFAZERES\n\t3)DESFAZER MUDANÇA\n\t4)REFAZER MUDANÇA\n\t5)SAIR')
    opcao=(input('\n : '))
    if opcao == '1':
        verr()
    elif opcao == '2':
        adc()
    elif opcao == '3':
        desf()
    elif opcao == '4':
        ref()
###############NAO DAR PARA FAZER COM ESSES N1 N2 N3 
'''