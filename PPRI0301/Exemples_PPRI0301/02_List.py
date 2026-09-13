# myList = list()
# myList = []
myList=list(range(10))
# myList[4]='toto'
# print("myList est une variable de type", type(myList))
# print("Elle contient", myList)

if len(myList) == 0:
    print("Elle est vide")
else:
    print("Elle contient", len(myList), "éléments :", myList)

# for i in range(len(myList)):
#     print(myList[i])
    
# for valeur in myList:
#     print(valeur)

for indice,valeur in enumerate(myList):
    print("myList[",indice,"] = ",valeur,sep="")
    # ("myList["+indice+"] ="+valeur)