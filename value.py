n = int(input('Digite um número: '))
print('''Escolha uma das opcões das base para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] coverter para OCTAL
[ 3 ] converter para HAXADECIMAL ''')
opção = int(input('Qual sua opção de conversão: '))
if opção == 1:
    print('Binário: {}'.format((bin(n))))
elif opção == 2:
    print('OCTAL: {}'.format(oct(n)))
elif opção == 3:
    print('HAXADECIMAL: {}'.format(hex(n)))
else:
    print('Digite um valor valido. {} não é um valor valido'.format(opção))
