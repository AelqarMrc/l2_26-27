/* Ch Jaillet
 * Info0301 - PFL
 */

#ifndef __CELLULE_H__
#define __CELLULE_H__

typedef struct xcell {
    Element val;
    struct xcell* svt;
} cellule;

cellule* nouvelleCellule(Element, cellule*);

#endif
