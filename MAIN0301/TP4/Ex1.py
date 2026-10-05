import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. Création de l'échantillon
# ==========================================
def generer_echantillon(taille=1000):
    """
    Génère un échantillon de paires (prix, unités).
    X (Prix) : variable continue entre 10 et 70.
    Y (Unités) : variable discrète entre 0 et 100.
    """
    np.random.seed(42) # Pour la reproductibilité
    prix_X = np.random.uniform(10, 70, taille)
    unites_Y = np.random.randint(0, 101, taille)
    return prix_X, unites_Y

# ==========================================
# 2. Modalités, classes et centres (Formule de Yule)
# ==========================================
def calculer_nombre_classes_yule(n):
    """Calcule le nombre de classes selon la formule de Yule : k = 2.5 * N^(1/4)"""
    return int(round(2.5 * (n ** 0.25)))

def definir_modalites_ou_classes(variable, est_continu=True):
    """
    Définit les classes (si continu) ou modalités (si discret avec peu de valeurs).
    Ici, vu que Y peut prendre 101 valeurs pour N=1000, on le regroupera 
    également en classes pour éviter un tableau trop creux.
    """
    n = len(variable)
    k = calculer_nombre_classes_yule(n)
    
    # Création des intervalles (bins) et des centres
    bins = np.linspace(np.min(variable), np.max(variable), k + 1)
    centres = (bins[:-1] + bins[1:]) / 2
    return bins, centres

# ==========================================
# 4. & 5. Tableaux de contingence
# ==========================================
def calculer_tableau_contingence_effectifs(X, Y, bins_X, bins_Y):
    """Calcule le tableau de contingence des effectifs (nij)"""
    # np.histogram2d renvoie la matrice des effectifs et les bords des classes
    nij, _, _ = np.histogram2d(X, Y, bins=[bins_X, bins_Y])
    return nij

def calculer_tableau_contingence_frequences(nij):
    """Calcule le tableau de contingence des fréquences (fij)"""
    total = np.sum(nij)
    return nij / total

# ==========================================
# 6. Séries marginales
# ==========================================
def calculer_series_marginales(tableau):
    """
    Calcule les séries marginales.
    Renvoie la marge de X (somme sur les colonnes) et marge de Y (somme sur les lignes).
    """
    marge_X = np.sum(tableau, axis=1)
    marge_Y = np.sum(tableau, axis=0)
    return marge_X, marge_Y

# ==========================================
# 7. Étude statistique (Marginales)
# ==========================================
def etude_statistique_serie(effectifs, centres):
    """
    Calcule la moyenne, la variance et l'écart-type d'une série bivariée 
    à partir de ses effectifs et des centres de ses classes.
    """
    n_total = np.sum(effectifs)
    if n_total == 0:
        return np.nan, np.nan, np.nan
        
    moyenne = np.sum(effectifs * centres) / n_total
    variance = np.sum(effectifs * (centres - moyenne)**2) / n_total
    ecart_type = np.sqrt(variance)
    
    return moyenne, variance, ecart_type

# ==========================================
# 8. & 9. Séries conditionnelles
# ==========================================
def etudier_serie_conditionnelle_X_sachant_Y(nij, centres_X, j):
    """Étudie la série conditionnelle X / Y = y_j"""
    effectifs_cond = nij[:, j]
    moy, var, std = etude_statistique_serie(effectifs_cond, centres_X)
    return effectifs_cond, moy, var, std

def etudier_serie_conditionnelle_Y_sachant_X(nij, centres_Y, i):
    """Étudie la série conditionnelle Y / X = x_i"""
    effectifs_cond = nij[i, :]
    moy, var, std = etude_statistique_serie(effectifs_cond, centres_Y)
    return effectifs_cond, moy, var, std

# ==========================================
# 10. Vérification de l'indépendance
# ==========================================
def verifier_independance(fij):
    """
    Vérifie l'indépendance statistique : fij = fi. * f.j pour tout i, j.
    """
    f_X, f_Y = calculer_series_marginales(fij)
    # Produit externe des fréquences marginales pour obtenir la grille théorique
    fij_theorique = np.outer(f_X, f_Y)
    
    # On compare la matrice des fréquences réelles et théoriques (avec une tolérance)
    independant = np.allclose(fij, fij_theorique, atol=1e-3)
    return independant, fij_theorique

# ==========================================
# 11. Coefficient de corrélation de Pearson
# ==========================================
def calculer_correlation_pearson(X, Y):
    """
    Calcule le coefficient de corrélation linéaire de Pearson entre X et Y.
    """
    covariance = np.cov(X, Y, bias=True)[0, 1]
    std_X = np.std(X)
    std_Y = np.std(Y)
    
    if std_X > 0 and std_Y > 0:
        r = covariance / (std_X * std_Y)
    else:
        r = 0
    return r

# ==========================================
# 12. Nuage de points
# ==========================================
def afficher_nuage_points(X, Y):
    """Affiche le nuage de points de l'échantillon"""
    plt.figure(figsize=(8, 6))
    plt.scatter(X, Y, alpha=0.5, c='royalblue', edgecolors='k')
    plt.title('Relation entre le prix (X) et les unités vendues (Y)')
    plt.xlabel('Prix du produit (€)')
    plt.ylabel('Nombre d\'unités vendues')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

# ==========================================
# Bloc d'exécution principal (Démonstration)
# ==========================================
if __name__ == "__main__":
    # 1. Échantillon
    X, Y = generer_echantillon(1000)
    
    # 2. Classes (on groupe X et Y pour le tableau croisé)
    bins_X, centres_X = definir_modalites_ou_classes(X, est_continu=True)
    bins_Y, centres_Y = definir_modalites_ou_classes(Y, est_continu=True)
    
    # 4 & 5. Tableaux
    nij = calculer_tableau_contingence_effectifs(X, Y, bins_X, bins_Y)
    fij = calculer_tableau_contingence_frequences(nij)
    
    # 11. Corrélation
    r = calculer_correlation_pearson(X, Y)
    print(f"Coefficient de Pearson (r) : {r:.4f}")
    
    # Interprétation de Pearson
    if abs(r) < 0.3:
        print("Interprétation : Il n'y a pas ou très peu de corrélation linéaire entre le prix et les unités vendues.")
    elif abs(r) < 0.7:
        print("Interprétation : Corrélation linéaire modérée.")
    else:
        print("Interprétation : Forte corrélation linéaire.")

    # 12. Affichage
    # afficher_nuage_points(X, Y) # Décommentez pour afficher le graphique