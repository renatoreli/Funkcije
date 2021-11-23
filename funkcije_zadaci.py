#%%
#1
def kalkulator(a,b):
    umnozak = a*b
    zbroj = a+b
    razlika = a-b
    kolicnik = a/b
    return(umnozak,zbroj,razlika,kolicnik)

print (kalkulator(2,3))
# %%
#2
def ucenici_in_class(ucenik):
    ucenici = [ "Marko","Ivan","Renato"]
    print(ucenik in ucenici)

ucenici_in_class("Renato")
# %%
def najveci_broj(num1,num2,num3):
    list = [num1,num2,num3]
    even = [i for i in list if i%2==0 ]
    odd = [i for i in list if i%2!=0 ]
    print(even)
    print(odd)
print(najveci_broj(1,2,3))

# %%
#4

def faktorijel(broj):
    if broj ==1:
        return broj
    else:
        return broj*faktorijel(broj-1)
broj = 6
fakt=faktorijel(broj)
print(fakt)
# %%
#5
def velika_slova(string_lower:str):
    return string_lower.upper()
print(velika_slova("renato"))
# %%
#6
import math
from typing_extensions import Unpack
def kalkulus(radius):
    p=(radius*2) * math.pi
    v = 2*radius* math.pi
    o = 4*math.pi*(radius**2)
    print("Povrsina",p)
    print("Volumen", v)
    print("Oplosje", o)

kalkulus(5)
# %%
#7
def suma(brojevi:list):
    total = 0
    for broj in brojevi:
        total += broj

    return total

print(suma([3,4,5]))
# %%
#8

def palindrom(string: str):
    unazad= string[::-1]
    if string == unazad:
        return True
    else:
        return unazad

print(palindrom("Renato"))
print(palindrom("kapak"))

# %%
#9
def umnozak(a,b):
    umnozak = a * b
    print(f"umnozak  je {umnozak}")
print(umnozak(2,3))
# %%
#10
def brojac(string: str):
    velika_slova = []
    mala_slova = []
    brojevi = []

    for slovo in string:
        if slovo.isupper():
            velika_slova.append(slovo)
        elif slovo.islower():
            mala_slova.append(slovo)
        elif slovo.isdigit():
            brojevi.append(brojevi)
    print("Velika slova su", len(velika_slova))
    print("Mala slova su",len(mala_slova))
    print("brojevi su", len(brojevi))

brojac("REna53To")
# %%
#11
def lista(list1: list):
    lista = []
    for broj in list1:
        if list1.count(broj)==0:
            list1.append(broj)
    return list1
print(lista(["Idemo", 43,43, "idemo", 32 ,32]))
    
# %%
#13
def prost_broj(a):
    return (a % 2!=0)
a=int(input("Unesi broj"))

if prost_broj(a):
    print(a,"je prost broj")
else:
    print(a,"nije prost broj")
# %%
#14
def nadi_broj(brojevi:int):
    brojevi=[]
    for i in range(2000,3200):
         djeljiv = i %7 ==0
         nije_djeljiv = i%5 !=0
    if djeljiv and nije_djeljiv:
        brojevi.append(i)
    
    print(",".join(brojevi))

nadi_broj()

# %%
#15
def kvadrat(brojevi:int):
    return[i**2 for i in brojevi]

print(kvadrat([2,4,6,8]))
     
# %%
#16
def redoslijed(string: str):
    zarez= string.split(",")
    sortirano = sorted(zarez)
    return ",".join(sortirano)
print(redoslijed("marko,ivan,luka"))
#%%
#17
def veliko_slovo(string:str):
    return string.title()

print(veliko_slovo("hello world"))
# %%
#20 #21
def brojac(string):
  
    upper = 0
    lower = 0
  
    for i in range(len(string)):
          
        # For lower letters
        if (ord(string[i]) >= 97 and
            ord(string[i]) <= 122):
            lower += 1
  
        # For upper letters
        elif (ord(string[i]) >= 65 and
              ord(string[i]) <= 90):
            upper += 1
  
    print('Lower case characters = %s' %lower,
          'Upper case characters = %s' %upper)

brojac("REna53To")

# %%
#22
def kvadrat():
    brojevi = [22,33,23,11]
    novi_brojevi=[]
    for broj in brojevi:
        g = broj**2
        novi_brojevi.append(g)

    print(novi_brojevi)
kvadrat()
# %%
#24
def  print_YES(string:str):
    if string.lower() =="yes":
        print("Yes")
print_YES("YES")
print_YES("yes")
print_YES("Yes")
print_YES("YeS")

# %%
#26
def djeljivo(brojevi:list):
    for broj in brojevi:
        djeljiv_sa_sedam= broj %7==0
        djeljiv_sa_pet= broj%5==0

        if djeljiv_sa_pet and djeljiv_sa_sedam:
            print(broj)
print(djeljivo([5,10,15,25,35,70,140]))
# %%
#27
def makni(number: int, numbers:list):
    return[i for i in numbers if i!=number]

print(makni(3,[2,3,7,24,13,3]))
# %%
#28
def ne_znam(string:str, index:int):
    final_string=""
    for i in range(len(string)):
        char = string[i]
        if i % index==0:
            final_string += char
    print(final_string)
ne_znam("dananas",1)
ne_znam("dananas",2)
ne_znam("dananas",3)


# %%
