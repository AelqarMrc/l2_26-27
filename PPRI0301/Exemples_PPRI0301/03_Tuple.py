# myTuple = tuple()
# myTuple = ()
# myTuple=tuple(range(10))
myTuple=(0,1,2,3,4,5)

# myTuple[4]='toto'

print("myTuple est une variable de type", type(myTuple))
print("Il contient", myTuple)

# if len(myTuple) == 0:
#     print("Il est vide")
# else:
#     print("Il contient", len(myTuple), "éléments :", myTuple)

# for i in range(len(myTuple)):
#     print(myTuple[i])
    
# for valeur in myTuple:
#     print(valeur)

# for indice,valeur in enumerate(myTuple):
#     print("myTuple[",indice,"] =",valeur)

# PACKING
# valeurs = 'A', 'B', 'C'
# print("valeurs est une variable de type", type(valeurs))
# print("Elle contient", valeurs)
# a,b,c=valeurs
# print("a =",a,", b =",b,"et c =",c)

# BONUS: switching values
x=1
y=x+1
print(x,y)
# x,y = y,x
# print(x,y)