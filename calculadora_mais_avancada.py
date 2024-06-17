import math

def adc(x,y):
    if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
        return 'Nenhum dos valores é um numero'
    
    try:
        return x + y
    except TypeError:
        
        if not isinstance(x, (int,float)):
            return f'{x} não é numero'
        
        if not isinstance(y, (int, float)):
            return f'{y} não é um numero'
        

def sub(x,y):
    try:
        return x - y
    except TypeError:
        if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
            return 'Nenhum dos valores é um numero'
        if not isinstance(x, (int,float)):
            return f'{x} não é numero'
        if not isinstance(y, (int, float)):
            return f'{y} não é um numero'

def mult(x, y):
    if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
        return 'Nenhum dos valores é um numero'

    if not isinstance(x, (int,float)):
        return f'{x} não é numero'
        
    if not isinstance(y, (int, float)):
        return f'{y} não é um numero'
        
    try:

        return x * y
    
    except Exception:
        return 'Erro desconhecido'


def div(n, d):
    try:
        return n / d
    
    except ZeroDivisionError:

        return 'Não pode dividir por zero'
    
    except TypeError:
        if not isinstance(n, (int, float)) and not isinstance(d, (int, float)):
            return 'Nenhum dos valores é um numero'
            
        if not isinstance(n, (int, float)):
            return f'{n} não é número'
        
        elif not isinstance(d, (int, float)):
            return f'{d} não é número'
        

def raiz(x):
    
    if not isinstance(x, (int, float)):
        return f'{x} não é numero'
    
    if x < 0:
        return 'Não pode dividir por numero negativo'

    return math.sqrt(x)

# acima tem as funções matematicas


def value_1():
    while True:
        try:
            user_value = input('Digite um número inteiro ou flutuante: ')
            number = float(user_value)  
            if number.is_integer(): #se o numero for inteiro, retorne o numero de forma inteira
                return int(number)            
            return number  #se não, continue sendo flutuante
        except ValueError:
            print('Entrada inválida. Por favor, digite um número inteiro ou flutuante.')


print()

def value_2():
    while True:
        try:
            user_value = input("Digite um número inteiro ou decimal: ")
            number = float(user_value)  
            if number.is_integer():  
                return int(number)  #se o numero for inteiro, retorne o numero de forma inteira
            return number  #se não, continue sendo flutuante
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro ou decimal.")
    
def operation_loop():
    while True:
        user_value = input('Digite uma operação: ')
        if user_value not in ['+', '-', '*', '/', 'r']:
            print('Operação desconhecida')
            continue
        
        if user_value == '+':
            print(f' {n1} + {n2} = {adc(n1, n2)}')

        elif user_value == '-':
            print(f' {n1} - {n2} = {sub(n1, n2)}')

        elif user_value == '*':
            print(f' {n1} * {n2} = {mult(n1, n2)}')

        elif user_value == '/':
            print(f' {n1} / {n2} = {div(n1, n2)}')
            
        elif user_value == 'r':
            print('Valores separados:')

            print(f' Raiz de {n1} = {raiz(n1)}')
            print(f' Raiz de {n2} = {raiz(n2)}')

#funcoes para atribuição de valores



n1 = value_1()
n2 = value_2()
print('Operações: [+] [-] [*] [/] [r]')
print('r = raiz quadrada')
operation = operation_loop()




#Testes (peguei do chatgpt, pq ninguem merece testar um por um  as 2 da manhã kkkkkkk)

# Teste para adição
# print("Teste para adição:")
# print(adc(2, 3))        # Deve retornar 5
# print(adc(2, '2'))      # Deve retornar '2 não é número'
# print(adc('a', 3))      # Deve retornar 'a não é número'
# print(adc('a', 'b'))    # Deve retornar 'Nenhum dos valores é um número'
# print()

# # Teste para subtração
# print("Teste para subtração:")
# print(sub(5, 3))        # Deve retornar 2
# print(sub(2, '2'))      # Deve retornar '2 não é número'
# print(sub('a', 3))      # Deve retornar 'a não é número'
# print(sub('a', 'b'))    # Deve retornar 'Nenhum dos valores é um número'
# print()

# # Teste para multiplicação
# print("Teste para multiplicação:")
# print(mult(2, 3))       # Deve retornar 6
# print(mult(2, '2'))     # Deve retornar '2 não é número'
# print(mult('a', 3))     # Deve retornar 'a não é número'
# print(mult('a', 'b'))   # Deve retornar 'Nenhum dos valores é um número'
# print()

# # Teste para divisão
# print("Teste para divisão:")
# print(div(6, 3))        # Deve retornar 2.0
# print(div(6, 0))        # Deve retornar 'Não pode dividir por zero'
# print(div('a', 3))      # Deve retornar 'a não é número'
# print(div(6, 'b'))      # Deve retornar 'b não é número'
# print(div('a', 'b'))    # Deve retornar 'Nenhum dos valores é um número'
# print()

# # Teste para raiz quadrada
# print("Teste para raiz quadrada:")
# print(raiz(4))          # Deve retornar 2.0
# print(raiz(-1))         # Deve retornar 'Não posso calcular raiz de número negativo'
# print(raiz('a'))        # Deve retornar 'Não é número'
