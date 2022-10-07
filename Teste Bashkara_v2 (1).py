# BIBLIOTECAS
import math
import cmath


# FUNÇÕES AUXILIARES
def function_parameters():
    print('Entre com a equação quadrática:\nDado:\ta.x² + b.x + c')
    a = float(input('Valor de "a":\t'))
    b = float(input('Valor de "b":\t'))
    c = float(input('Valor de "c":\t'))
    print()
    return a, b, c

def zero_function(a, b, delta, raiz_delta):
    raiz1 = (-b + raiz_delta) / (2 * a)  # calculo das raizes e armazenado cada uma em uma variável
    raiz2 = (-b - raiz_delta) / (2 * a)
    print(f'Valor de Delta:\t{delta}\t\t')
    print(f'Os valores das raízes são:\t\tx1 = {raiz1}\t x2 = {raiz2}\n')


# FUNÇÃO PRINCIPAL
print("*******************************  Calculadora 2.0  *******************************\n")

option = 0                                                              # variável auxiliar para entrar no loop
while option != "N":
    a, b, c = function_parameters()                                     # entre com os parametros da equação quadrática
    delta = (b**2) - (4*a*c)

    if delta >=0:
        raiz_delta = math.sqrt(delta)                                   # calculo da raiz quadrada do delta e armazenado em uma variável - biblioteca MATH
        print(('Raizes no campo dos números REAIS!!\n'))
        zero_function(a, b, delta, raiz_delta)

    else:
        raiz_delta = cmath.sqrt(delta)                                  # uso da biblioteca CMATH
        print(('Raizes no campo dos números COMPLEXOS!!\n'))
        zero_function(a, b, delta, raiz_delta)

    option = input('Precione qualquer tecla para continuar ou "N" para sair\t')     # mensagem final no loop perguntando se deseja continuar
    print()

print('Até logo!!!\n')                                                  # mensagem final de despedida


# ------------------------------------------------------------------------ RESOLUÇÃO ------------------------------------------------------------------------
# passo1 : monte uma equação que calcule o delta e as raizes
# passo1.2: efetue testes no caminho efetuando o print() das variaveis utilizadas na tela para ver se o codigo está rodando
# passo2: monta o loop e coloca dentro as operações
# -*- coding: utf-8 -*-
# EQUAÇÃO: ax**2 + bx + c
# DELTA:   b**2 - 4 * a * c
# X:       x = [- b +/- sqr(DELTA)]/ (2*a)

# passo3: uso de funcoes auxiliares para deixar o codigo mais rápido para execução