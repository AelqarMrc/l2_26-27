/* Ch Jaillet
 * Info0301 - PFL
 */

#ifndef __LISTEC_H__
#define __LISTEC_H__

// partie generique uniquement //////////////////////////
typedef struct xListeC ListeC;

///////////////////////////////
// comme d'habiture

void creerListeC(ListeC *);
void libererListeC(ListeC *);

_Bool listeCVide(ListeC);

void inserer  (ListeC *, Element);
void supprimer(ListeC *);

Element valeurCourante(ListeC);

///////////////////////////////
// deplacements

void allerDebut(ListeC *);
_Bool estDebut   (ListeC);

void allerFin(ListeC *);
_Bool estFin   (ListeC);

void avancer(ListeC *);

#endif
