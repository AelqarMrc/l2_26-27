file_name = "Discussion.txt"
encodage="utf-8"

print("===================================================")
file_object = open(file_name)
for ligne in file_object:
    liste=list(ligne)
    print(liste)
file_object.close()

# print("===================================================")
# for ligne in open(file_name):
#     print(ligne)

# print("===================================================")
# for ligne in open(file_name,encoding=encodage):
#     print(ligne)

# print("===================================================")
# for ligne in open(file_name,encoding=encodage):
#     print(ligne,end="")
# print()

# print("===================================================")
# with open(file_name, encoding=encodage) as file_object:
#     print(file_object.readlines())

# print("===================================================")
# with open("test", 'w') as file_object:
#     file_object.write("Coucou")
#     print("ça va ?",file=file_object)
    
# with open("test") as file_object:
#     print(file_object.read())

# print("===================================================")
# with open("test2", 'a') as file_object:
#     file_object.write("Coucou\n")
#     print("ça va ?",file=file_object)
    
# with open("test2") as file_object:
#     print(file_object.read())

