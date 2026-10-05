/* Ch Jaillet
 * Info0301 - PFL
 */

#ifndef __FILE_H__
#define __FILE_H__

/////////////////////////////////////////////////////////
// partie generique uniquement //////////////////////////

typedef struct xFile File_;

void creerFile(File_ *);
void libererFile(File_ *);

_Bool fileVide(File_);

void enfiler(File_ *, Element);
void defiler(File_ *);

Element tete(File_);

#endif
