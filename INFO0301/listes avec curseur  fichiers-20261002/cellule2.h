/* Ch Jaillet
 * Info0301 - PFL
 */

#ifndef __CELLULE2_H__
#define __CELLULE2_H__

typedef struct xcell2 {
	Element val;
	struct xcell2 * pred, 
	              * succ;
} cellule2;

cellule2* nouvelleCellule2(Element, cellule2*, cellule2*);

#endif
