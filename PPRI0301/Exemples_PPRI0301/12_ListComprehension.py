from ListComprehensionToolBox import power_list, fibo1, fibo2, fibo3, fibo4, show_list
from ListComprehensionToolBox import valeurs_paires_avec_fibo2 as vpaf2
from ListComprehensionToolBox import valeurs_paires_avec_fibo3 as vpaf3
from ListComprehensionToolBox import valeurs_paires_avec_fibo4 as vpaf4
from ListComprehensionToolBox import valeurs_paires_avec_fibo4_2nd_version as vpaf4v2

if __name__ == "__main__":
    
    maListe = list(range(10))

    print(maListe)
    show_list(maListe)
    # power_list(maListe)
    # print(maListe)
    # show_list(maListe)
    
    # print()
    
    # autreListe=[x*x for x in list(range(10))]
    # show_list(autreListe)
    
    # generateur=(x*x for x in list(range(10)))
    # generateur=(y for y in (x*x for x in list(range(10))) if y%2==0)
    # print(generateur)
    # for valeur in generateur:
    #     print(valeur)
    
    # print("générateur fini")
    
    # for valeur in generateur:
    #     print(valeur)
    
    # print()
    
    # print(f'fibo1(10) = {fibo1(10)}')
    # print(f'fibo2(10) = {fibo2(10)}')
   
    # print()
   
    # print('Valeurs impaires de fibo2(10) :',[x for x in fibo2(10) if x%2==1]) 
   
    # print() 
   
    # print('valeurs paires parmi les 10 premiers termes avec fibo2',vpaf2(10))
    
    # ATTENTION BOUCLE INFINIE
    # for valeur in fibo3():
    #     print(valeur)
    
    # print('valeurs paires parmi les 50 premiers termes avec fibo3',vpaf3(50))    
    # print('Les 10 premières valeurs paires parmi les termes de Fibonnacci avec fibo4   ',vpaf4(10))
    # print('Les 10 premières valeurs paires parmi les termes de Fibonnacci avec fibo4 V2',vpaf4v2(10))
