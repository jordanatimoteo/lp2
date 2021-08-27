from os import replace
with open('arquivo_dna.txt', 'r') as txt:
 recebetxt = txt.readlines()
print (recebetxt)
i=0
while i < len(recebetxt):
 x = recebetxt[i]
 A = x.replace("A","u")
 B = A.replace("T","a")
 C = B.replace("G","c")
 D = C.replace("C","g")
 print('\n')
 print(('string'),(i+1),('original '),(x))
 print(('impressão da string'),(i+1),(D.upper()))
 i=i+1