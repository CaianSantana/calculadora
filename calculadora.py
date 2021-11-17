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
if b in subtraçao:
    resultado = numero[0]-numero[1]
if b in multiplicaçao:
    resultado = numero[0]*numero[1]
if b in divisao:
    resultado = numero[0]/numero[1]
print('O resultado da divisão de',numero[0],'e',numero[1],'é:',str(resultado))
