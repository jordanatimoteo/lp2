print('Infome os números para que seja calculada a média obs:a média será calculada quando o valor "0" for informado')
laco = int(input('Informe o número: '))
y = 0
somar = 0
while laco != 0:
    somar = somar + laco
    laco = int(input('Informe um número: '))
    y = y+1
print('A média vale: ', somar/y)