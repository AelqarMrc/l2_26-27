/* Ch Jaillet
 * projet : TDA sequentiels
 * fichier : Pile_.h
 *******************
 */

#ifndef __PILE___H__
#define __PILE___H__

// generique : c'est dans l'implem. qu'on precisera
typedef struct xPile Pile_;

// les 5 fonctionnalites
void creerPile(Pile_* pp);

_Bool pileVide(Pile_ p);
Element sommet(Pile_ p);

void empiler(Pile_* pp, Element e);
void depiler(Pile_* pp);

// obligatoire aussi, pour qu'on puisse liberer la memoire si la creation a fait un malloc
void libererPile(Pile_* pp);

#endif
