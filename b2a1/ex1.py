with open('arquivo_dna.txt', 'r') as var:
 recebevar = var.readlines()
print (recebevar)
print('\n')
j = 0
while j < len(recebevar):
 i = recebevar[j]
 print((i.count('A')),('Adeninas na'),('string'),(j+1
 ))
 print((i.count('T')),('Timinas na'),('string'),(j+1)
)
 print((i.count('C')),('Citosinas na'),('string'),(j+1))
 print((i.count('G')),('Guaninas na'),('string'),(j+1)
)
 print('\n\n')
 j=j+1