# import sys
# from sys import exit
# from sys import exit as sortie_avec_code

value = input("Taper un entier svp : ")

print(f"Le type de la variable value est {type(value)}")

# value = int(input("Taper un entier svp : "))

# print(f"Le type de la variable value est {type(value)}")

# try:
#     value = int(input("Taper un entier svp : "))
# except ValueError:
#     print("Vous n'avez pas tapé une value entière, shame on you !!!")
#     sys.exit(666)
#     exit(666)
#     sortie_avec_code(666)
# else:
#     print("Ouf tout va bien")
#     print(f'value + 1 faut {value+1}')

# print()

# try:
#     5/0
# except ZeroDivisionError:
#     print("Je fais n'importe quoi")

# print("Je vais faire encore une bêtise mais tant pis ...")

# try:
#     # npkoi=5/0
#     operation_de_la_mort_qui_tue()
#     tous_les_etudiants_deviennent_defaillants()
# except ZeroDivisionError:
#     pass
# else:
#     print("Cela s'est vraiment passé ?")