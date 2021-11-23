
def dvostruke_godine():

# list comprehension

    godine = [22,33,23,11]
    nove_godine=[]
    for god in godine:
        g = god*2
        nove_godine.append(g)

    print(nove_godine)

def trostruke_godine():
    #list comprehension
    godine = [22,33,23,11]
    god =  [i*3 for i in godine]
    print(god)

#%%
def povrsina(a,b,ime_lika):
    p = a * b
    # povrsina <ime_lika> je <p>
    print(f"povrsina {ime_lika}a je {p}")
#%%
def dohvati_podatke():
    a = "mirko"
    b= "preklopotovic"
    return a,b

ime, prezime = dohvati_podatke()
print(ime,prezime) 
# %%
