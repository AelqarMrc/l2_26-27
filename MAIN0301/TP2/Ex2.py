import math
import matplotlib.pyplot as plt

# Données de l'exercice 2 sous forme {modalite: effectif}
donnees = {1: 15, 2: 20, 3: 18, 4: 12, 5: 8, 6: 5}


# Conversion en liste brute pour faciliter les calculs et graphiques
def reconstruire_echantillon(tab: dict) -> list:
    echantillon = []
    for mod, eff in tab.items():
        echantillon.extend([mod] * eff)
    return echantillon


# 1. Calcul et affichage du tableau statistique complet
def calculer_tableau_statistique(tab: dict) -> dict:
    total = sum(tab.values())
    cumul_eff = 0
    cumul_freq = 0.0
    tableau_complet = {}

    for mod in sorted(tab.keys()):
        eff = tab[mod]
        freq = eff / total
        cumul_eff += eff
        cumul_freq += freq
        tableau_complet[mod] = {
            "effectif": eff,
            "frequence": freq,
            "eff_cumul": cumul_eff,
            "freq_cumul": cumul_freq,
        }
    return tableau_complet


def afficher_tableau_statistique(tableau_complet: dict) -> None:
    print(
        f"{'Visites':>8} | {'Effectif':>8} | {'Fréquence':>10} | {'Eff. Cumul':>10} | {'Fréq. Cumul':>11}"
    )
    print("-" * 58)
    for mod, vals in tableau_complet.items():
        print(
            f"{mod:>8} | {vals['effectif']:>8} | {vals['frequence']:>10.3f} | {vals['eff_cumul']:>10} | {vals['freq_cumul']:>11.3f}"
        )
    print("-" * 58)
    total_eff = sum(v["effectif"] for v in tableau_complet.values())
    print(f"{'Total':>8} | {total_eff:>8} | {1.0:>10.3f} |\n")


# 2. Mesures de tendance centrale
def calculer_moyenne(tab: dict) -> float:
    total_eff = sum(tab.values())
    somme_produits = sum(mod * eff for mod, eff in tab.items())
    return somme_produits / total_eff


def calculer_mode(tab: dict) -> list:
    max_eff = max(tab.values())
    return [mod for mod, eff in tab.items() if eff == max_eff]


def calculer_mediane(tab: dict) -> float:
    ech = reconstruire_echantillon(tab)
    n = len(ech)
    milieu = n // 2
    if n % 2 == 1:
        return float(ech[milieu])
    return (ech[milieu - 1] + ech[milieu]) / 2


# 3. Mesures de dispersion
def calculer_etendue(tab: dict) -> float:
    return max(tab.keys()) - min(tab.keys())


def calculer_ecart_absolu_total(tab: dict) -> float:
    moy = calculer_moyenne(tab)
    return sum(eff * abs(mod - moy) for mod, eff in tab.items())


def calculer_ecart_moyen(tab: dict) -> float:
    return calculer_ecart_absolu_total(tab) / sum(tab.values())


def calculer_variance(tab: dict) -> float:
    moy = calculer_moyenne(tab)
    total_eff = sum(tab.values())
    somme_carres = sum(eff * ((mod - moy) ** 2) for mod, eff in tab.items())
    return somme_carres / total_eff


def calculer_ecart_type(tab: dict) -> float:
    return math.sqrt(calculer_variance(tab))


def calculer_coefficient_variation(tab: dict) -> float:
    return calculer_ecart_type(tab) / calculer_moyenne(tab)


def calculer_quartiles(tab: dict) -> tuple[float, float]:
    ech = reconstruire_echantillon(tab)
    n = len(ech)
    idx_q1 = int(math.ceil(n / 4)) - 1
    idx_q3 = int(math.ceil(3 * n / 4)) - 1
    return ech[idx_q1], ech[idx_q3]


def calculer_ecart_interquartile(tab: dict) -> float:
    q1, q3 = calculer_quartiles(tab)
    return q3 - q1


# 4. Diagramme en bâtons
def tracer_diagramme_batons(tab: dict) -> None:
    modalites = list(tab.keys())
    effectifs = list(tab.values())

    plt.figure()
    plt.bar(modalites, effectifs, width=0.01)
    plt.xlabel("Nombre de visites mensuelles")
    plt.ylabel("Effectif")
    plt.title("Diagramme en bâtons des visites mensuelles")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


# 5. Boîte à moustaches
def tracer_boite_moustaches(tab: dict) -> None:
    ech = reconstruire_echantillon(tab)

    plt.figure()
    plt.boxplot(ech)
    plt.ylabel("Nombre de visites mensuelles")
    plt.title("Boîte à moustaches des visites mensuelles")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


if __name__ == "__main__":
    # 1. Tableau statistique
    tab_complet = calculer_tableau_statistique(donnees)
    print("Tableau statistique :")
    afficher_tableau_statistique(tab_complet)

    # 2. Tendance centrale
    print("--- Mesures de tendance centrale ---")
    print(f"Moyenne : {calculer_moyenne(donnees):.2f}")
    print(f"Mode(s) : {calculer_mode(donnees)}")
    print(f"Médiane : {calculer_mediane(donnees):.2f}\n")

    # 3. Dispersion
    print("--- Mesures de dispersion ---")
    print(f"Étendue : {calculer_etendue(donnees)}")
    print(f"Écart-absolu (somme) : {calculer_ecart_absolu_total(donnees):.2f}")
    print(f"Écart moyen : {calculer_ecart_moyen(donnees):.2f}")
    print(f"Variance : {calculer_variance(donnees):.2f}")
    print(f"Écart-type : {calculer_ecart_type(donnees):.2f}")
    print(f"Coefficient de variation : {calculer_coefficient_variation(donnees):.4f}")
    q1, q3 = calculer_quartiles(donnees)
    print(f"Q1 : {q1} | Q3 : {q3}")
    print(f"Écart interquartile (EIQ) : {calculer_ecart_interquartile(donnees)}")

    # 4 & 5. Graphiques
    tracer_diagramme_batons(donnees)
    tracer_boite_moustaches(donnees)