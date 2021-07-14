def somaNum(a,b):
  if a + b > 1000:
   raise OverflowError
  return a + b
try:
  x = int(input('Informe o primeiro número: '))
  y = int(input('Informe o segundo número: '))
  print ( 'o resultado da soma é: ',somaNum(x,y))
except OverflowError:
  print('A soma entre',x,'e',y,' resulta em um valor maior que 1000.')
except ValueError:
  print('Entrada de dados inesperada.')