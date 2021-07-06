valor = int(input('Informe o enésimo termo: '))
f1 = 0
f2 = 1
i = 0
while i < valor:
    x = f1 + f2
    f1 = f2
    f2 = x
    i = i + 1
print('O enésimo termo do valor informado é')
print(f1)