
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
        
