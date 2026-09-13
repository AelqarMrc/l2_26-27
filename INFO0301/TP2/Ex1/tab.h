#ifndef TAB_H
#define TAB_H
#define MAX 100
typedef double Tab1D[MAX];

// Remplissage et affichage
    void saisir(Tab1D t, int taille);
    void affichage(Tab1D t, int taille);

// Calculs divers
    int sommeTab(double t1[MAX], double t2[MAX], int taille);
    double produitTab(double t1[MAX], double t2[MAX], int taille);
    int indiceMin(double t1[MAX], int taille);
    int valMax(double t1[MAX], int taille);

// Fonctions de recherches
    int rechercheSeq(Tab1D t, int taille);
    int rechercheDich(Tab1D t, int taille);

// Fonctions de tri
    void triSE(Tab1D t, int taille);
    void triIns(Tab1D t, int taille);
    void triBulles(Tab1D t, int taille);

#endif