import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

# Exemplo de uso: gerar senha com comprimento 12
senha_gerada = gerar_senha(12)
print("Senha gerada:", senha_gerada)

# segundo código 

def sequ(n):
    aux1 = 2
    aux2 = 3.0
    soma = 0

    while aux1 <= num:
        print aux1, aux2
        soma = soma + aux1/aux2
        aux1 = aux1 + 1
        aux2 = aux2 + 2

    return soma

num = input('Digite um valor: ')
while num < 0:
    num = input('Digite um valor positivo: ')

res = sequ(num)
print res
