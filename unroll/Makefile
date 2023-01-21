CC=gcc

CFLAGS=-Wall -g

OFLAGS=-march=native -O1 -fopt-info-all=dist.gcc.optrpt
INTEL_FLAGS=-xhost -O1 -qopt-report

all: genseq dist_gcc dist_icc 

dist_gcc: dist_gcc.c
	$(CC) $(CFLAGS) $(OFLAGS) $< -o gcc/$@

dist_icc: dist_icc.c
	icc $(CFLAGS) $(INTEL_FLAGS) $< -o icc/$@
	icx $(CFLAGS) $(INTEL_FLAGS) $< -o icx/$@

genseq: genseq.c
	$(CC) -march=native $(CFLAGS) -Ofast $< -o gcc/$@
	icc -march=native $(CFLAGS) -Ofast $< -o icc/$@
	icx -march=native $(CFLAGS) -Ofast $< -o icx/$@

run:
	cd gcc && ./genseq s1.dna 60000 && ./genseq s2.dna 60000 && ./dist_gcc s1.dna s2.dna > result.csv
	cd icc && ./genseq s1.dna 60000 && ./genseq s2.dna 60000 && ./dist_icc s1.dna s2.dna > result.csv
	cd icx && ./genseq s1.dna 60000 && ./genseq s2.dna 60000 && ./dist_icc s1.dna s2.dna > result.csv

plot:
	python3 plot.py

clean:
	rm -Rf *~ */genseq */dist */dist_gcc */dist_icc */*.optrpt */*.dna */*.csv *.png *.optrpt *.opt.yaml
