import random
import matplotlib.pyplot as plt

modalites = ("Voiture", "Transport en commun", "Vélo", "Moto", "Trotinette", "A pied")
poids = poids = [25, 40, 15, 15, 5, 10]

echantillon = random.choices(modalites, weights=poids, k=100)

N = len(echantillon)

effectifs = [echantillon.count(m) for m in modalites]
frequences = [eff / N for eff in effectifs]
frequencesP = [round(freq * 100,2) for freq in frequences]

tab_stat = {}

tab_stat['x'] = modalites
tab_stat['n'] = effectifs
tab_stat['f'] = frequences
tab_stat['fp'] = frequencesP

print()
# En-tête
print(f"{'Modalité (x)':<22} | {'Effectif (n)':>12} | {'Fréquence (f)':>14} | {'Fréquence % (fp)':>17}")
print("-" * 73)

# Lignes de données
for m, n, f, fp in zip(tab_stat['x'], tab_stat['n'], tab_stat['f'], tab_stat['fp']):
    print(f"{m:<22} | {n:>12} | {f:>14.2f} | {fp:>16.1f}%")

# Total
print("-" * 73)
total_n = sum(tab_stat['n'])
total_f = sum(tab_stat['f'])
total_fp = sum(tab_stat['fp'])
print(f"{'Total':<22} | {total_n:>12} | {total_f:>14.2f} | {total_fp:>16.1f}%")
print()


# Création du diagramme à bandes
plt.figure(figsize=(12, 6)) # Taille de la figure
plt.bar(modalites,effectifs, color='blue') # Création des barres
2
# Ajout de titres et labels
plt.title('Un titre de votre choix')
plt.ylabel ("les effectifs ni")
plt.xticks(range(len(effectifs)),modalites)
# Affichage du diagramme
plt.show()

# Création du diagramme circulaire

plt.figure(figsize=(12, 6)) # Taille de la figure
plt.pie(frequencesP,labels=modalites,autopct='%1.1f%%') # création du camembert
# Ajout du titre
plt.title('Diagramme circulaire des fréquences en %')
# Affichage du diagramme
plt.show()