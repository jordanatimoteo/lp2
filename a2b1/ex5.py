n = int (input("Digite um número para apresentar todos os primos entre 1 e N: "))
i=1
while i < n:
  contar = 0
  j=1
  while j < i:
   if i % j == 0:
    contar += 1
   j += 1
  if contar == 1:
   print(i)
  i +=1