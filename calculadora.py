from math import sqrt

#Calculadora proposta no capitulo 4 do curso Fundamentos de Linguagem Python para Análise de Dados e Data Science

print("------------ Calculadora ------------")

print('1: Soma')
print('2: Subtração')
print('3: Multiplicação')
print('4: Divisão')
print('5: Potência')
print('6: Raiz Quadrada')
print('7: Porcentagem')

print('Escolha a operação: ')


#Operação de soma em Lambda
soma =  lambda num1, num2: num1 + num2
#Operação de subtração em Lambda
subtracao = lambda num1, num2: num1 - num2
#Operação multiplicação em lambda
multiplica = lambda num1, num2: num1 * num2
#Operação de Divisão em Lambda
divisao = lambda num1, num2: num1 // num2
#Operação de Potencia em lambda
potencia = lambda num1, num2: num1 ** num2
#Operação de raiz quadrada em Lambda
raiz_quadrada = lambda num1: sqrt(num1)
#Operação de porcentagem em Lambda
porcentagem = lambda num1, num2: (num1 * num2) / 100

valor_opcao = int(input('Qual operação você deseja realizar? '))

if valor_opcao in [1 , 2 , 3, 4, 5, 7]:
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))

if valor_opcao == 1:
    print('Operação de Soma')
    print(soma(num1, num2))
elif valor_opcao == 2:
    print('Operação de Subtração')
    print(subtracao(num1, num2))
elif valor_opcao == 3:
    print('Operação de Multiplicação')
    print(multiplica(num1, num2))
elif valor_opcao == 4:
    print('Operação de Divisão')
    print(divisao(num1, num2))
elif valor_opcao == 5:
    print('Operação de Potência')
    print(potencia(num1, num2))
elif valor_opcao == 6:
    print('Operação Raiz Quadrada')
    num1 = int(input('Digite o número: '))
    resultado = str(raiz_quadrada(num1))
    print('A raiz quadrada do valor é: ' + resultado)
elif valor_opcao == 7:
    print('Operação de Porcentagem')
    print(porcentagem(num1, num2))
else:
    'Operação inválida'
