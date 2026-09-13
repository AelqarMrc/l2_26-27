#ifndef TEMPS_H
#define TEMPS_H

typedef struct temps
{
    int h, m;
    double s;
}temps;

temps creer(int h, int m, double s);
_Bool correct(temps t);

void afficher (temps t);
temps normaliser(temps t);
temps creer2(void);
void saisir(temps *pt);

#endif