# -*- coding: utf-8 -*-
# EQUAÇÃO: ax**2 + bx + c
# DELTA:   b**2 - 4 * a * c
# X:       x = [- b +/- sqr(DELTA)]/ (2*a)


# BIBLIOTECAS
import math
import cmath

# FUNÇÕES AUXILIARES

# FUNÇÃO PRINCIPAL  - CABEÇALHO
print("*******************************  Calculadora 1.0  *******************************\n")

option = 0                                                              # variável auxiliar para entrar no loop
while option != "N":
    print('Entre com a equação quadrática:\nDado:\ta.x² + b.x + c')    # entre com os parametros da equação quadrática
    a = float(input('Valor de "a":\t'))
    b = float(input('Valor de "b":\t'))
    c = float(input('Valor de "c":\t'))
    print()

    delta = (b**2) - (4*a*c)
    #print(delta)                                                         # Exemplo de verificação se está correto o valor de DELTA

    if delta >=0:
        raiz_delta = math.sqrt(delta)                                   # calculo da raiz quadrada do delta e armazenado em uma variável - biblioteca MATH
        raiz1 = (-b + raiz_delta) / (2*a)                               # calculo das raizes e armazenado cada uma em uma variável
        raiz2 = (-b - raiz_delta) / (2*a)

        print(f'Valor de Delta:\t{delta}\t\t~\t\tRaiz no campo dos números reais')
        print(f'Os valores das raízes são:\t\tx1 = {raiz1}\t x2 = {raiz2}\n')

    else:
        raiz_delta = cmath.sqrt(delta)                                  # uso da biblioteca CMATH
        raiz1 = (-b + raiz_delta) / (2*a)                               # calculo das raizes e armazenado cada uma em uma variável
        raiz2 = (-b - raiz_delta) / (2*a)

        print(f'Valor de Delta:\t{delta}\nRaiz no campo dos números complexos!')
        print(f'Os valores das raízes são:\t\tx1 = {raiz1}\t x2 = {raiz2}\n')


    option = input('Precione qualquer tecla para continuar ou "N" para sair\t')     # mensagem final no loop perguntando se deseja continuar
    print()

print('Até logo!!!\n')                                                  # mensagem final de despedida


# ------------------------------------------------------------------------ RESOLUÇÃO ------------------------------------------------------------------------
# passo1 : monte uma equação que calcule o delta e as raizes
# passo1.2: efetue testes no caminho efetuando o print() das variaveis utilizadas na tela para ver se o codigo está rodando
# passo2: monta o loop e coloca dentro as operações