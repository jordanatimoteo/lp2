v = int(input("Informe um número para calcular seu fatorial: "))
número = v
controle = v
fatorial = v
while controle >1:
 v = v - 1
 fatorial = fatorial * v
 controle = controle - 1
print ('O fatorial do número ',número,'é:', fatorial)