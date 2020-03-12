import docstr

#CLASSE  = MOLDE ************
#METODO DE CLASSE = MODIFICA O MOLDE (METODO RELACIONADO A CLASSE E NAO A INSTANCIA) ***********
'''
from datetime import datetime

class Pessoa:
    ano= int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo= comendo
        self.falando= falando

    def comer(self,food):
        if self.comendo:
            print('Já Está Comendo')
            return
        if self.falando:
            print('nao pode comer falando')
            return
        print(f'{self.nome} está comendo {food}')
        self.comendo=True

    def PararComer(self):
        if not self.comendo:
            print('não ta comendo')
            return
        print('parou de comer')
        self.comendo=False

    def falar(self,assunt):
        if self.comendo:
            print('nao pode falar comendo')
            return
        print(f'{self.nome} está falando sobre {assunt}')
        if self.falando:
            print('já ta falando')
            return
        self.falando=True

    def PararFalar(self):
        if not self.falando:
            print('não ta falando')
            return
        print('parou de falar')
        self.falando=False

    def AnoNasc(self):
        idade=int(self.idade)
        print(f'{self.nome} Nasceu em {self.ano-idade}')

    @classmethod
    def CriarPessoa(cls,nome,AnoNasc):
        idade=2020-AnoNasc
        return cls(nome,idade)


#BRINCADEIRA
# f=False
# while True:
#     nome=input('Qual Nome  ? : ')
#     anoo=int(input(f'Que ano {nome} Nasceu ? :'))
#     if nome == 'leticia':
#         nome='Princesinha nenem P.C'
#     elif nome == 'ramon':
#         nome='Menino Mal e chato com Princesinha nenem P.C'
#     Leticia = Pessoa.CriarPessoa(nome,anoo)
#     print(f'\nO nome é {Leticia.nome}')
#     print(f' Tem {Leticia.idade} aninhos')
#     acao=input('O que quer fazer ?:')
#     if acao=='falar' and nome=='Princesinha nenem P.C':
#         pes = input('Com quem ? : ')
#         if pes=='menino mal'and not f:
#             print('NAO FALI COM O MENINO MAL POXA VIDA NAO FALI ELE É MAL')
#         if pes=='menino mal'and f:
#             print(f'{nome} podi voltar a falar com o menino hihihi')
#     if acao == 'falar' and nome=='Menino Mal e chato com Princesinha nenem P.C':
#         pes=input('Com quem ? : ')
#         if pes=='nenem'and not f:
#             print('NAO PODI TU FOI MAL COM O NENEM')
#         if pes=='nenem'and f:
#             ms=input('Que falar o que ? : ')
#             print(f'Princesinha nenem P.C o {nome} tá com muita saudade e muito amor po teu lado <3')
#     if acao == 'desculpar' and nome == 'Menino Mal e chato com Princesinha nenem P.C':
#         des=input('Quer se desculpar com quem : ')
#         if des == 'nenem':
#             print('tu foi mal dms com o nenem isso nao se faz\nmas nenem vai te desculpar pq ela e só nenem \ne ta so dodoi papai \n')
#             f=True

Leticia = Pessoa.CriarPessoa('Princesa',2000)
print(f'o Nome dela é {Leticia.nome} sua idade é {Leticia.idade}')
ramon = Pessoa('Ramon','18')
while True:
    acao=input('ação: ')
    if acao == 'c':
        alim=input('alimento: ')
        ramon.comer(alim)
    if acao == 'f':
        assunto = input('assunto: ')
        ramon.falar(assunto)
    if acao == 'pf':
        ramon.PararFalar()
    if acao == 'pc':
        ramon.PararComer()
    if acao == 'a':
        ramon.AnoNasc()

'''

# GETTER E SETTERS
#fAZER EXEMPLO DO CURSO
##################

#ATRIBUTOS DA CLASSE
'''
class A:
    c=123
    def __init__(self):
        self.c=234

a1=A()
a2=A()
print(a1.c) #234

a1.c = 321
print(a1.c) #321 : mudei para a instancia a1 mas não para classe
print(a2.c)#234
print(A.c)#123
#CASO QUEIRA MUDAR O DE TODOS MUDAR PELA CLASSE (A.C=123)
'''

#CONVENÇÃO
'''
_ = PROTECTED
__ = PRIVATE
'''


#COMPOSIÇÃO EM PYTHON ESCREVER E FAZER COM GETTER E SETTER DPS
'''
class Pessoa:

    def  __init__(self,nome,idade):
        self.nome=nome
        self.idade = idade

    def falar(self):
        print(f' essa Pessoa :{self.nome} esta falando')

    def comer(self):
        print(f' essa Pessoa :{self.nome} esta comendo')


class Aluno(Pessoa):    ######### ALUNO É PESSOA
    def __init__(self, nome, idade, sobrenom):
        Pessoa.__init__(self,nome,idade)             ### IMPORTANTE CHAMAR O INICIADOR
        self.sobre=sobrenom

    def falar(self):
        Pessoa.falar(self)
        print(f' esse aluno :{self.nome} esta falando')

    def comer(self):
        super().comer()      ### O MESMO QUE Pessoa.comer(self)
        print(f' essa Aluno :{self.nome} esta comendo')
    def estuda(self):
        print('estudando')

class AlunoVip(Aluno): ############# ALUNO VIP É ALUNO E PESSOA
    pass

al=Aluno('Ramon',35,"Rodrigues")
al.falar()
al.comer()
alvip=AlunoVip('noah',56,'kiel')
alvip.falar()
alvip.estuda()
'''


#### VER ARQUIVOS DE HERANÇA MULTIPLAS E ABSTRATAS

#### CLASSES ABSTRATAS FORÇAM QUE AS FILHAS TENHAM ALGUMA FUNÇÃO
#### CLASSES ABSTRATAS NAO PODEM SER INSTANCIONADAS ELAS SERVEM APENAS PARA SER CLASSES BASES

'''
########################################################################################################################
### Exemplo basico

from abc import  ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def metodoObrigatorio(self):
        print('todas subclasses de A tem que ter esse metodo')

class B(ABC):
    @abstractmethod
    def metodoObrigatorio2(self):
        print('todas subclasses de B tem que ter esse metodo')

class C(A,B):
    def metodoObrigatorio(self):
        pass
    def metodoObrigatorio2(self):
        pass

c=C() # SÓ É POSSIVEL EXECUTAR SE HOUVER OS METODOS OBRIGATORIOS EM C


########################################################################################################################
'''


### ver operadores em classes
### operadores magicos
### gerenciadores de conteudo


### HERANÇA e ABSTRAÇÃO
'''
from abc import ABC, abstractmethod

class P:
    def __init__(self,nome):
        self.nome=nome
    def falar(self):
        print('falando')

class D(P,ABC):
    def __init__(self,nome,idade):
        super().__init__(nome)
        self.idade=idade
    @abstractmethod  ###obriga as subclasses dele a ter esse metodo
    def obrigatorio(self):
        pass

class T(D):
    def andar(self):
        print('andando')
    def obrigatorio(self):
        print('metodo obrigatiorio')


a=T('ramon',45)
a.falar()
a.andar()
'''
#TODO: ESTUDAR GETTERS E SETTERS E METACLASSES

### METACLASSES
'''
class Meta(type):
        def __new__(mcs,name,bases,namespace):
            if name == 'A':
                return type.__new__(mcs,name,bases,namespace)
            if 'stringclasse' in namespace:
                del namespace['stringclasse']

            return type.__new__(mcs,name,bases,namespace)

class A(metaclass=Meta):
    stringclasse= 'Valor A'

class B(A):
    stringclasse = 'Valor B'

b=B()
print(b.stringclasse)    ### O VALOR NAO E SOBRESCRITO POIS A METACLASSE PROIBIU
'''

### METODO ESTÁTICO NA CLASSE NAO RECEBE 'SELF' ENTAO ELE NAO E INSTANCIADO
### SERVE COMO FERRRAMENTA DENTRO DA FUNÇAO COMO FAZER CALCULOS PAR ASER UTILIZADO EM
### OUTRA FUNÇÃO DENTRO DA CLASSE




###DocString
'''
help(docstr)
'''


