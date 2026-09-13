from sys import argv
from os import getcwd, listdir, chdir
from os.path import isfile, isdir, join, basename

arguments=argv[1:]

print(f'\nJe suis dans {getcwd()}\n')

print('======================================================================')

# all_files = listdir('.')
# print(f'Il y a {len(all_files)} fichiers dans le répertoire courant :')
# for file_name in all_files:
#     print('\t',file_name)

# print()    
# chdir("sous_repertoire")
# print(f'Je suis dans {getcwd()}')

# print()

# chdir("..")
# print(f'Je suis revenu dans {getcwd()}\n')

# print('======================================================================')

# for file_name in listdir('.'):
    
#     if not file_name[0]=='0':
#         # print(f'Je zappe {file_name}')
#         continue
    
#     if isdir(file_name):
#         # print(f'\t{file_name} est un répertoire')
#         print(f'\t{file_name:30s} est un répertoire')
    
#     if isfile(file_name):
#         # print(f'\t{file_name} est un fichier')
#         print(f'\t{file_name:30s} est un    fichier')

# print('======================================================================')
        
# for file_name in listdir('.'):
#     print(f'\t{file_name:30s} est un ',end='')
     
#     if isdir(file_name):
#         print('répertoire')
            
#     if isfile(file_name):
#         print('   fichier')
        
# print('======================================================================')

# for file_name in listdir('.'):
    
#     type = 'inconnu'
    
#     if isdir(file_name):
#         type='répertoire'
            
#     if isfile(file_name):
#         type='   fichier'

#     print(f'\t{file_name:30s} est un {type}')
          
# print('======================================================================')

# repertoire="."
# if len(arguments)==1:
#     repertoire=arguments[0]

# for file_name in listdir(repertoire):
#     chemin = join(repertoire,file_name)
#     print(chemin)
#     # chemin=file_name
#     if isdir(chemin):
#         print(f'Il y a {len(listdir(chemin))} éléments dans {chemin}')

# print('======================================================================')  