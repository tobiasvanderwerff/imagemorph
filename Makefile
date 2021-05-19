FLAGS =  -pedantic -Wunused -Wunused-function -Wunused-parameter -Wunused-variable -Wall 
#        -pg
#
imagemorph:	imagemorph.o Makefile
	gcc $(FLAGS) imagemorph.o -static -static-libgcc -lm  -o imagemorph

imagemorph.o: imagemorph.c
	gcc $(FLAGS) -fPIC -c imagemorph.c

imagemorph.so: imagemorph.o
	gcc $(FLAGS) -shared imagemorph.o -o imagemorph.so

clean:
	\rm imagemorph imagemorph.o imagemorph.so

# -fPIC: position independent code, required for dynamic linking
# -c: don't run the linker (no executable)

