
#CONDIÇOES SIMPLES: COMPARAÇOES: >, <, >=, <=, ==, TRUE OU FALSE

A=0; B=3
print(A>B)
x=3.7
print(x<=10.0)
a=9 ; b=16
print(a-b>=0)
a=2; b=4; n=10
print(a*b<n)
a=3; b=9; c=5
print(10*a>=b*c)
a=3; b=6; c=5
print(10*a>=b*c)
n=7
print(n%2==0)
n=8
print(n%2==0)
t="Morango"
print(t=="Banana")
t="Morango"
print(t>"Banana")

# CONDIÇOES COMPOSTAS: AND, OR,  != ,= TRUE OU FALSE
a=10; b=15; c=4
print(a<b and a<c)
a=10; b=15; c=4
print(a<b or a<c)
a=1; b=9; c=0
print(a>=0 and b==c)
a=1; b=9; c=9
print(a>=0 and b==c)
a=1; b=9; c=0
print(a>=0 or b==c)
a=1; b=9; c=9
print(a>=0 or b==c)
a=0; b=0; c=0
print(b!=0 and a!=c)
a=0; b=0; c=25
print(b!=0 and a!=c)
a=0; b=0; c=0
print(b!=0 or a!=c)
a=0; b=0; c=25
print(b!=0 or a!=c)

#CONDIÇOES MISTAS: NOT, AND, OR, >, <, >=, <=, ==, != , TRUE OU FALSE
a=10; b=15; c=4
print(a<b and a<c or c!=0)
a=10; b=15; c=4
print(a<b and (a<c or c!=0))
a=1; b=9; c=0
print(not(a>=0 and b==c))
a=1; b=9; c=9
print(not(a>=0) and not (b==c))
a=1; b=9; c=0
print((a>=0 or b==c)and c==0)
a=0; b=1; c=0
print(a==0 and b!=0 and c==0)
a=-2; b=0; c=2
print(not(a<=b) or c>b)
a=-2; b=0; c=2
print(not(a<0 or c>b))
a=5; b=0; c=0
print(a==0 and b!=0 and c==0)
a=5; b=0; c=0
print(a==0 or b!=0 or c==0)



# Calcular a hipotenusa de um triângulo retângulo
a=6 
b=8 
c=(a**2 + b**2)**0.5
print (c)

a=50
b=80
c=(a**2 + b**2)   
d= c**0.5

print(d)*

#***************************************************
#28_08_25
n =0;
while n < 100 or n > 500:
    try:
        s = (input("digite um valor no intervalo de [100, 500]:"))
        n = int (s);
    except:
        print("{} não é um número.".format(s));
        n=0;
    else:
        if n <100 or n >500:
            print("o valor lido {} esta forra do intervalo" .format(n));
        else:
            print("o valor lido {} esta ok" .format(n));
    finally:
        print("\n\n");#repetição do código


#*************
x = "abcd";
print( x[-1]);
print( x[-2]);
print( x[-3]);

print( x[0]);
print( x[1]);
print( x[2]);

print( x[1]);
print( x[2]);
print( x[3]);

s ='cadeia de texto definido com apostofro';
d = "cadeia de texto definido com aspas";
print (s);
print(d);
print(type(d));
print(type(s));
print(len(s));#quantidade total de string, fila
print(s[0]);
print(s[1]);
print(s[37]);
print(s[40]); #deu erro pq o numero de letras é menor

##
v= 'nono';
print(id(v));
v='outro';
print(id(v));
v[0] = 'p';
print(v[0]);
####
s="Festa"
T="na vila"
U= s+ T
print(U)
U= 'hoje tem '+ U
print(U)
K="repete."
W = K * 3
print(W)
s= "festa "+ 100 # da erro pq string não concatena COM NUMERO 
#### Fatiamento 
s= 'abcdefghijklmno'
print(s)
len(s)
print(s[3:10])
print(s[0:5]) #o mesmo valor abcde pq tanto faz colocar o zero
p = s[3:10]
print (p)
print(len(p))
i = 0
f=0
print(s[i:f])
print(s[:5])#o mesmo valor abcde pq tanto faz colocar o zero
print(s[5:])

t='9pula8pula7pula6pula5'
print(len(t))
print(t[0:21:5])# de cinco em cinco
print(t[::5])# de cinco em cinco

#Exercicos lista satoshi----------------------------------------------
#Exercicio 1 ----
lado=(input("Digite o lado de um quadrado"))
area=(lado+lado)
print("A area é igual a ",  area)

#Exercicio 2 ----
salario= int(input("digite o salario "))
novoSalario=((salario)*1.15)
print("Novo salário igual", novoSalario)

#Exercicio 3 ----
base= int(input("Digite a base do triângulo "))
altura=(int(input("Digite a altura de um triângulo")))
area=((base*altura)/2)
print("Area é: ", area)

#Exercicio 4 ----
temperatura= float(input("Digite a temperatura "))
F=(((9*temperatura)+160)/5)
print("A conversão da tempura em graus para Fahrenheit é: ", F)

#Exercicio 5 --------------------------------------
a= float(input("Digite o valor de A "))
b= float(input("Digite o valor de b "))
c= float(input("Digite o valor de c "))
E=(((a**2)+160)/5)

#Exercicio 6 --------------------------------------
#Exercicio 7 ----
l= int(input("Digite A Largura "))
a= int(input("Digite  a Altura "))
c= int(input("Digite o Comprimento "))
volume=(c*l)*a
print("O volume do paralelepípedo é: ", volume)
print(f"O volume do paralelepípedo é: {volume}")#maneiras

#Exercicio 8 ----
"""Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que recebe 1,3% a.m."""
poupanca=int(input("Digite o para depósito :"))
valorapos=(poupanca)*1.13
print("O informe de rendimento apos 1 mês é: %.2f " %valorapos)

#Exercicio 9 ----
"""Receba os 2 númeors inteiros. Calcule e mostre a soma dos quadrados"""
a= int(input("Digite o valor de A "))
b= int(input("Digite o valor de b "))
res=(a*a)+(b*b)
print(f"A soma dos quadrados é {res}")

#Exercicio 10 ----
"""Receba os 2 númeors inteiros. Mostre a diferença"""
a= int(input("Digite o valor de A "))
b= int(input("Digite o valor de b "))
res=(a-b)
print(f"A diferença é {res}")

#Exercicio 11  ----
"""Receba o raio e calcule o comprimento de um circuferência"""
import math
r= int(input("Informe o raio "))
(C=(2*math.pi)*r)
print(f"A diferença é {}")

#Exercicio  ----
#Exercicio  ----
#Exercicio  ----
#Exercicio  ----
#Exercicio  ----
#Exercicio  ----
#Exercicio  ----
#Exercicio  ----
#Exercicio  ----


