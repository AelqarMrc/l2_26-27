EXE = a.out
CFLAGS = -Wall -Werror

# point d'entrée

all : $(EXE)

# module objet
temps.o : temps.c temps.h
	gcc $(CFLAGS) $< -c

main.o : main.c temps.c temps.h
	gcc $(CFLAGS) $< -c
	

# règle principale 
$(EXE) : main.o temps.o
	gcc $^ -o $@

#nettoyage

clean :
	rm *.o

mrproper :
	rm $(EXE)