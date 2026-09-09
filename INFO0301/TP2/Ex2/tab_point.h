#ifndef TAB__POINT_H
#define TAB__POINT_H
#define MAX 1000

typedef point Tab_point[MAX];
typedef struct 
{
    unsigned int i, j;
}indices;

// Indice des deux points les plus éloignés
    indices distMinMax(Tab_point t, int taille);

// Tri par distance à l'origine (croissant)
    void triDist(Tab_point t, int taille);

#endif