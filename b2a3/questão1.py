emissor=float(3) #Quantidade de quilômetros do emissor até a circunferência.
sensor=float(2) #Quantidade de quilômetros da circunferência até o sensor.
circunferência=float(8) #Quantidade de quilômetros da circunferência.
D =float(input("Insira um número entre 6 e 800008: ")) #Etapa onde o usuário colocará seu número.
Z= float(D - (emissor + sensor)) #Subtraindo o valor do número do usuário e o valor do emissor e do sensor, teremos Z, os quilômetros percorridos na circunferência.
X= (Z / circunferência) #Dividindo o valor de Z com o valor da circunferência, teremos o número de voltas que a partícula deu.
T= int(X) #O valor de X tem decimais, portanto criaremos uma "cópia" chamada T para retirá-los.
A= X - T #Agora, subtraimos X por T para termos A, apenas os decimais.
if A == 0.125: #Caso dê 0.125;
    print ("A partícula atingiu o sensor 1.") #A partícula atingirá o sensor 1.
if A == 0.25: #Agora, caso dê 0.25;
    print ("A partícula atingiu o sensor 2.") #A partícula atingirá o sensor 2.
if A == 0.375: #se o resultado for 0.375;
    print ("A partícula atingiu o sensor 3.") #A partícula atingirá o sensor 3.
if A > 0.375: #finalizando, se o resultado for maior que 70.375;
        print ("A partícula não atingiu nenhum sensor. tente outro número.") #A partícula não atingirá nenhum sensor.
if A < 0.125: #seguindo a lógica da de cima, se o resultado for menor que 0.125;
    print ("a partícula não atingiu nenhum sensor. tente outro número.") #A partícula não atingirá nenhum sensor, novamente.

    

    