num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))

print('1- Adição')
print('2- Subtração')
print('3- Divisão')
print('4- Multiplicação')

operacao = int(input('Digite o número da operação que você deseja:'))

if operacao == 1:
    num3 = num1 + num2
    print(num3)

elif operacao == 2:
    num3 = num1 - num2 
    print(num3)

elif operacao == 3:
    if num2 == 0:
        print('Não é possível dividir qualquer número por 0')
    else:
        num3 = num1 / num2
        print(num3)

else:
    num3 = num1 * num2
    print(num3)
