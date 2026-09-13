#ifndef POINT_H
#define POINT_H

typedef struct xpoint
{
    double x,y;
}point;

// Fonctions de remplissage et d'affichage
    void remplir(point* pp);
    void affichage(point p);

// Plus petite distance à l'origine
    double distanceO(point p);

#endif