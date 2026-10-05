/* Ch Jaillet
 * Info0301 - PFL
 */

#ifndef __ELEMENT_H__
#define __ELEMENT_H__

//////////////////////////////////////////////
// partie generique //////////////////////////

typedef struct xElement Element;

void saisie(Element*);
void affichage(Element);
_Bool egaux(Element, Element);

//////////////////////////////////////////////
// partie specifique /////////////////////////

struct xElement {
	double x;
	int n;	
};
/* on ne peut pas retarder plus la definition du type de structure
 * le plus simple aurait donc ete de preciser le detail du struct avec le typedef 
 * (en haut de ce fichier) :
 **	    typedef struct {
 **          double x;
 **	    	int n;
 ** 	} Element;
 */

double valeurReelle(Element e);
int valeurEntiere(Element e);

#endif
