from typing import List, Callable, Generator

def show_list(mylist : List[int], width : int = 3):
    print('[',end="")
    for element in mylist[:-2]:
        print(f"{element:{width}d},",end="")
    print(f"{mylist[-1]:{width}d}]")

def power_list(uneliste: List[int]):
    for i in range(len(uneliste)):
        uneliste[i]=uneliste[i]**2

def fibo1(n:int) -> int :
    n1:int=1
    n2:int=1
    
    # n1=n2=1
    
    i=1
    while i<n:
        
        temp:int=n1
        n1=n2
        n2=temp+n1
        
        # n1,n2=n2,n1+n2
        
        i+=1
    return n1    

def fibo2(n : int) -> List[int] :
    if n==1:
        return [1]
    liste=[1,1]
    i=2
    while i<n:
        liste.append(liste[-2]+liste[-1])
        i+=1
    return liste

def fibo3() -> Generator:
    n1=n2=1
    while(True):
        yield(n1)
        n1, n2 = n2, n1+n2

# Beware to infinite loop with bad test_function
def fibo4(test_function : Callable) -> Generator:
    n1=n2=1
    while(True):
        if not test_function(n1):
            n1, n2 = n2, n1+n2
            continue
        yield(n1)
        n1, n2 = n2, n1+n2

def valeurs_paires_avec_fibo2(n:int) -> List[int]:
    liste = []
    for valeur in fibo2(n):
        if valeur % 2 == 0:
            liste.append(valeur)
    return liste

def valeurs_paires_avec_fibo3(n:int) -> List[int]:
    generateur = fibo3()
    liste=[]
    for i in range(n):
        valeur = next(generateur)
        if valeur %2 == 0:
            liste.append(valeur)
    return liste

def valeurs_paires_avec_fibo4(n:int) -> List[int]:
    generateur = fibo4(est_paire)
    liste:List[int]=[]
    for i in range(n):
        liste.append(next(generateur))
    return liste

def est_paire(n:int) -> bool:
    return n%2==0

def valeurs_paires_avec_fibo4_2nd_version(n:int) -> List[int]:
    generateur = fibo4(lambda x : x%2==0)
    liste=[]
    for i in range(n):
        liste.append(next(generateur))
    return liste

# maListe=list(range(10))
# power_list(maListe)
# print(maListe)

# if __name__ == '__main__':
#     maListe : List[int]=list(range(10))
#     power_list(maListe)
#     print(maListe)
