# mySet = set()

# WARNING: PAS UN SET MAIS UN DICT AVEC {}
# mySet = {}

mySet=set(range(10))

# mySet={1,1,1,1,1,1}

print("mySet est une variable de type", type(mySet))
print("Il contient", mySet)

# mySet[4]='toto'
# print(mySet[4])

# if len(mySet) == 0:
#     print("Il est vide")
# else:
#     print("Il contient", len(mySet), "éléments :", mySet)

# for i in range(len(mySet)):
#     print(mySet[i])
    
# for valeur in mySet:
#     print(valeur)

# for indice,valeur in enumerate(mySet):
#    print("mySet[",indice,"] =",valeur)

# COMPARISON
# mySet2 = set(range(0,20,2))

# print("1 =",mySet)
# print("2 =",mySet2)

# print()

# _1m2 = mySet-mySet2
# print("1 - 2 ==>",_1m2)
# _1o2 = mySet|mySet2
# print("1 | 2 ==>",_1o2)
# _1a2 = mySet&mySet2
# print("1 & 2 ==>",_1a2)
# _1oe2 = mySet^mySet2
# print("1 ^ 2 ==>",_1oe2)