try:
  vetor = list(range(5))
  vetor = ['a','b','c','d','e']
  v = int(input('Informe a posição do vetor de 0 a 4 para o conteúdo exibido: '))
  print (vetor[v])
except IndexError:
  v = int (input('Esta posição não existe, informe um número de 0 a 4: '))
  print (vetor[v])