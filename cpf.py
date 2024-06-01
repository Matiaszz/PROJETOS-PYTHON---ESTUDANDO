# Gerador de cpf

import random

ata = input('Quantos cpfs quer gerar?: ' )
for _ in range(int(ata)):
    nove_digitos = ''# aqui pega os 9 primeiros indices do cpf
    regressiva1 = 10 #contagem regressiva
    resultado1 = 0 #aqui vai o resultado do FOR digito

    for i in range(9):
        nove_digitos += str(random.randint(0,9))

    
    for digito1 in nove_digitos: #para cada caractere em nove_digitos
        resultado1 += int(digito1) * regressiva1 #adiciona o valor do digito x a contagem regressiva no resultado
        regressiva1 -= 1 # o contador vai regredindo, no caso: 10, 9 , 8...

    digito1 = (resultado1 * 10) % 11 
    digito1 = digito1 if digito1 <= 9 else 0 #digito 1 se o digito 1 for menor ou igual a 9, senão é 0




    #a partir daqui pra baixo é praticamente a mesma coisa, porém adiciona o primeiro digito na conta
    nove2 = nove_digitos + str(digito1)
    regressiva2 = 11
    resultado2 = 0


    for digito2 in nove2:
        resultado2 += int(digito2) * regressiva2
        regressiva2 -= 1

    digito2 = (resultado2 * 10) % 11
    digito2 = digito2 if digito2  <= 9 else 0


    print(f' {nove_digitos + str(digito1) + str(digito2)}')
