EXE = a.out
CFLAGS = -Wall -Werror

# point d'entrée 
all : $(EXE)

# module objet 
point.o : point.c point.h
	gcc $(CFLAGS) $< -c

tab_point.o : tab_point.c point.h tab_point.h
	gcc $(CFLAGS) $< -c

main.o : main.c tab_point.c point.h tab_point.h
	gcc $(CFLAGS) $< -c

# règle principale
$(EXE) : main.o point.o tab_point.o -lm
	gcc $^ -o $@

#nettoyage
clean : 
	rm *.o

mrproper : 
	rm $(EXE)