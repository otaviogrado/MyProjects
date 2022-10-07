# BIBLIOTECAS
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt


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
    return raiz1, raiz2

def y(a,b,c,x):
    return (a*(x**2)) + (b*x) + c

def graphic_plot(a,b,c, x1, x2):
    passo = 1                                                  # de quanto em quantos pontos o gráfico vai pulando de número

    if x1>=x2:                                                   # condicionais para poder usar plotagem gráfica
        raiz2 = x1
        raiz1 = x2
    else:
        raiz1 = x1
        raiz2 = x2

#    x = np.arange(-abs(raiz1*(1.25)),abs(raiz2*(1.25)), passo)   # gera quantidade de pontos no eixo x
    x = np.arange(-10,10, passo)

    Y = [0]*len(x)                                               # lista usada para armazenar valores de y(x) = a.x**2 + b.x + c
    for i in range(len(x)):
        Y[i] = y(a,b,c,x[i])

    plt.plot(x,Y, 'r', marker = 'o', label = f'f(x) = {a}.x² + {b}.x + {c}')                            # plota gráfico y(x)            / marcadores em bolinha e na cor vermelha ( "r" = red )
    plt.title('Calculadora V3.0')                               # titulo do gráfico
    plt.grid()                                                  # plota as linhas do gráfico
    plt.legend()                                                # legenda no gráfico
    plt.show()                                                  # comando para plotar o gráfico


# FUNÇÃO PRINCIPAL
print("*******************************  Calculadora 3.0  *******************************\n")
option = 0                                                              # variável auxiliar para entrar no loop
while option != "N":
    a, b, c = function_parameters()                                     # entre com os parametros da equação quadrática
    delta = (b**2) - (4*a*c)

    if delta >=0:
        raiz_delta = math.sqrt(delta)                                   # calculo da raiz quadrada do delta e armazenado em uma variável - biblioteca MATH
        print(('Raizes no campo dos números REAIS!!\n'))
        raiz1, raiz2 = zero_function(a, b, delta, raiz_delta)
        graphic_plot(a,b,c, raiz1, raiz2)
    else:
        raiz_delta = cmath.sqrt(delta)                                  # uso da biblioteca CMATH
        print(('Raizes no campo dos números COMPLEXOS!!\n'))
        raiz1, raiz2 = zero_function(a, b, delta, raiz_delta)


    value = input('Precione qualquer tecla para continuar ou "N" para sair:\t')     # mensagem final no loop perguntando se deseja continuar
    option = value.upper()                                                          # arruma variável para poder valer a letra tanto maiusculo como minusculo
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
# passo4: uso da biblioteca NUMPY e MATPLOTLIB - para gerar graficos

# OBS: não consegui gerar gráficos complexos, por esse codigo - desafio a fazer um assim e aprimorar esse código