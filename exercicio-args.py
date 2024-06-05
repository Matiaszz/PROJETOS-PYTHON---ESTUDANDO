# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicacao (*args):
    acumulador = 1
    for valor in args:
        acumulador *= valor
    return(acumulador)

numeros = 1,2,3,4,5,6
total = multiplicacao(*numeros)
print(total)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar

def par_ou_impar(numero):
        if numero % 2 == 0:
            return f'o numero {numero} é par'
        return f'o numero {numero} é impar'
    
var = par_ou_impar(6)
print(var)
