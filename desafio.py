def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2

while True:
    print('''
        CALCULADORA:
        DIGITE UMA DAS OPÇÕES ABAIXO PARA CALCULAR
        [1] - SOMA
        [2] - SUBTRAÇÃO
        [3] - MULTIPLICAÇÃO
        [4] - DIVISÃO
        [9] - SAIR
    ''')
    menu = input(': ')
    if menu == '1':
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        print(soma(num1, num2))
    elif menu == '2':
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        print(subtracao(num1, num2))
    elif menu == '3':
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        print(multiplicacao(num1, num2))
    elif menu == '4':
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        if num1 == 0 or num2 == 0:
            print('ERRO')
        else:
            print(divisao(num1, num2))
    elif menu == '9':
        print('Programa finalizado')
        break
