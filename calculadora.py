numero = []
ordem = ['primeiro', 'segundo']
caracteristica = []
for i in range(2):
    a = float(input('Digite o '+ordem[i]+' número: '))
    numero.append(a)
b = str(input('Qual operação você deseja realizar: Soma(+),Subtração(-),Multiplicação(*) ou Divisão(/)? '))
b = b.lower()
soma = ['+','soma','somar']
subtraçao = ['-', 'subtração','subtrair']
multiplicaçao = ['*','multiplicação','multiplicar']
divisao = ['/','divisão','dividir']
if b in soma:
    resultado = numero[0]+numero[1]
    if resultado % 2 == 0:
        caracteristica.append('par')
    else:
        caracteristica.append('ímpar')
    if resultado > 0:
        caracteristica.append('positivo')
    elif resultado < 0:
        caracteristica.append('negativo')
    if resultado == round(resultado):
        caracteristica.append('inteiro')
    else:
        caracteristica.append('decimal')
    print('O resultado da soma de',numero[0],'e',numero[1],'é:',str(resultado)+
          '.\nEsse número é:',caracteristica[0]+',',caracteristica[1],'e',caracteristica[2])
if b in subtraçao:
    resultado = numero[0]-numero[1]
    if resultado % 2 == 0:
        caracteristica.append('par')
    else:
        caracteristica.append('ímpar')
    if resultado >= 0:
        caracteristica.append('positivo')
    elif resultado < 0:
        caracteristica.append('negativo')
    if resultado == round(resultado):
        caracteristica.append('inteiro')
    else:
        caracteristica.append('decimal')
    print('O resultado da subtração de',numero[0],'e',numero[1],'é:',str(resultado)+
          '.\nEsse número é:',caracteristica[0]+',',caracteristica[1],'e',caracteristica[2])
if b in multiplicaçao:
    resultado = numero[0]*numero[1]
    if resultado % 2 == 0:
        caracteristica.append('par')
    else:
        caracteristica.append('ímpar')
    if resultado > 0:
        caracteristica.append('positivo')
    elif resultado < 0:
        caracteristica.append('negativo')
    if resultado == round(resultado):
        caracteristica.append('inteiro')
    else:
        caracteristica.append('decimal')
    print('O resultado da multiplicação de',numero[0],'e',numero[1],'é:',str(resultado)+
          '.\nEsse número é:',caracteristica[0]+',',caracteristica[1],'e',caracteristica[2])
if b in divisao:
    resultado = numero[0]/numero[1]
    if resultado % 2 == 0:
        caracteristica.append('par')
    else:
        caracteristica.append('ímpar')
    if resultado > 0:
        caracteristica.append('positivo')
    elif resultado < 0:
        caracteristica.append('negativo')
    if resultado == round(resultado):
        caracteristica.append('inteiro')
    else:
        caracteristica.append('decimal')
    print('O resultado da divisão de',numero[0],'e',numero[1],'é:',str(resultado)+
          '.\nEsse número é:',caracteristica[0]+',',caracteristica[1],'e',caracteristica[2]