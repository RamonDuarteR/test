from random import randint
#cpf=input('Coloque seu cpf : ')
c=0
co=0
mult=10
multi=11
soma=0
soma_1=0
novo_cpf=''
#novo =randint(100000000,999999999)
#cpf=str(novo)

#ESCOLHER ENTRE VERIFICADOR OU CRIADOR DE CPF

#OU PARA NOVO CPF USAR
#novo_cpf = cpf[:-2]
while c<=8:
    num=int(cpf[c])
    novo_cpf +=cpf[c]
    prod = num*mult
    soma = soma + prod
    c += 1
    mult -=1
resultado_1= 11-(soma%11)
digito_1= 0 if (resultado_1>9) else resultado_1
while co<=8:
    num=int(cpf[co])
    prod = num*multi
    soma_1 = soma_1 + prod
    co += 1
    multi -=1
prod=0
prod = digito_1*multi
soma_1= soma_1 + prod
digito_2=11-(soma_1%11)
novo_cpf = novo_cpf + str(digito_1) + str(digito_2)
validador = 'Seu CPF é válido' if (str(cpf) == novo_cpf) else 'Seu CPF é inválido'
print('='*60,f'\n{validador}\n','='*60)
print(f'\n{novo_cpf}')



#todo:testar o todo
