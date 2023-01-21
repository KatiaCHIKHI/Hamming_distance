CC=gcc

CFLAGS=-Wall -g


GCC1=-march=native -O1 -fopt-info-all=dist.gcc.optrpt
GCC2=-march=native -O2 -fopt-info-all=dist.gcc.optrpt
GCC3=-march=native -O3 -fopt-info-all=dist.gcc.optrpt
GCC4=-march=native -Ofast -fopt-info-all=dist.gcc.optrpt

ICC1=-xhost -O1 -qopt-report
ICC2=-xhost -O2 -qopt-report
ICC3=-xhost -O3 -qopt-report
ICC4=-xhost -Ofast -qopt-report



all: genseq dist

dist: dist.c
	$(CC) $(CFLAGS) $(GCC1) -O1 $< -o gcc/O1/$@
	icc $(CFLAGS) $(ICC1) -O1 $< -o icc/O1/$@
	icx $(CFLAGS) $(ICC1) -O1 $< -o icx/O1/$@

	$(CC) $(CFLAGS) $(GCC2) -O2 $< -o gcc/O2/$@
	icc $(CFLAGS) $(ICC2) -O2 $< -o icc/O2/$@
	icx $(CFLAGS) $(ICC2) -O2 $< -o icx/O2/$@

	$(CC) $(CFLAGS) $(GCC3) -O3 $< -o gcc/O3/$@
	icc $(CFLAGS) $(ICC3) -O3 $< -o icc/O3/$@
	icx $(CFLAGS) $(ICC3) -O3 $< -o icx/O3/$@

	$(CC) $(CFLAGS) $(GCC4) -Ofast $< -o gcc/Ofast/$@
	icc $(CFLAGS) $(ICC4) -Ofast $< -o icc/Ofast/$@
	icx $(CFLAGS) $(ICC4) -Ofast $< -o icx/Ofast/$@

genseq: genseq.c
	cd gcc && mkdir -p O1 O2 O3 Ofast
	cd icc && mkdir -p O1 O2 O3 Ofast
	cd icx && mkdir -p O1 O2 O3 Ofast
	$(CC) -march=native $(CFLAGS) -Ofast $< -o gcc/O1/$@
	icc -march=native $(CFLAGS) -Ofast $< -o icc/O1/$@
	icx -march=native $(CFLAGS) -Ofast $< -o icx/O1/$@

	$(CC) -march=native $(CFLAGS) -Ofast $< -o gcc/O2/$@
	icc -march=native $(CFLAGS) -Ofast $< -o icc/O2/$@
	icx -march=native $(CFLAGS) -Ofast $< -o icx/O2/$@

	$(CC) -march=native $(CFLAGS) -Ofast $< -o gcc/O3/$@
	icc -march=native $(CFLAGS) -Ofast $< -o icc/O3/$@
	icx -march=native $(CFLAGS) -Ofast $< -o icx/O3/$@

	$(CC) -march=native $(CFLAGS) -Ofast $< -o gcc/Ofast/$@
	icc -march=native $(CFLAGS) -Ofast $< -o icc/Ofast/$@
	icx -march=native $(CFLAGS) -Ofast $< -o icx/Ofast/$@

run:
	cd gcc/O1 && ./genseq s1.dna 620000 && ./genseq s2.dna 620000 && ./dist s1.dna s2.dna > resultO1.csv
	cd icc/O1 && ./genseq s1.dna 620000 && ./genseq s2.dna 620000 && ./dist s1.dna s2.dna > resultO1.csv
	cd icx/O1 && ./genseq s1.dna 620000 && ./genseq s2.dna 620000 && ./dist s1.dna s2.dna > resultO1.csv

	cd gcc/O2 && ./genseq s1.dna 620000  && ./genseq s2.dna 620000  && ./dist s1.dna s2.dna > resultO2.csv
	cd icc/O2 && ./genseq s1.dna 620000  && ./genseq s2.dna 620000  && ./dist s1.dna s2.dna > resultO2.csv
	cd icx/O2 && ./genseq s1.dna 620000  && ./genseq s2.dna 620000  && ./dist s1.dna s2.dna > resultO2.csv

	cd gcc/O3 && ./genseq s1.dna 620000 && ./genseq s2.dna 620000 && ./dist s1.dna s2.dna > resultO3.csv
	cd icc/O3 && ./genseq s1.dna 620000 && ./genseq s2.dna 620000 && ./dist s1.dna s2.dna > resultO3.csv
	cd icx/O3 && ./genseq s1.dna 620000 && ./genseq s2.dna 620000 && ./dist s1.dna s2.dna > resultO3.csv

	cd gcc/Ofast && ./genseq s1.dna 620000 && ./genseq s2.dna 620000 && ./dist s1.dna s2.dna > resultOfast.csv
	cd icc/Ofast && ./genseq s1.dna 620000 && ./genseq s2.dna 620000 && ./dist s1.dna s2.dna > resultOfast.csv
	cd icx/Ofast && ./genseq s1.dna 620000 && ./genseq s2.dna 620000 && ./dist s1.dna s2.dna > resultOfast.csv

plot:
	python3 plot.py

clean:
	rm -Rf *~ */genseq */dist */*.optrpt */*.dna */*.csv *.png *.optrpt *.opt.yaml
