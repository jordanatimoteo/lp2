try:
  x=int(input("Entre com um número: ") )
  y=int(input("Entre com outro número: ") )
  print( x,'/', y,'=', x/y )
except ValueError:
  print("Algum dos números não é um número inteiro.")
except ZeroDivisionError:
  print("O segundo número é 0, e divisão por zero não existe.")