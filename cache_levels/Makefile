CC=gcc

CFLAGS=-Wall -g

OFLAGS=-march=native -O1 -fopt-info-all=dist.gcc.optrpt
INTEL_FLAGS=-xhost -O1 -qopt-report

all: genseq dist

dist: dist.c
	$(CC) $(CFLAGS) $(OFLAGS) $< -o gcc/$@
	icc $(CFLAGS) $(INTEL_FLAGS) $< -o icc/$@
	icx $(CFLAGS) $(INTEL_FLAGS) $< -o icx/$@

genseq: genseq.c
	$(CC) -march=native $(CFLAGS) -Ofast $< -o gcc/$@
	icc -march=native $(CFLAGS) -Ofast $< -o icc/$@
	icx -march=native $(CFLAGS) -Ofast $< -o icx/$@

run:
	cd gcc && ./genseq s1.dna 120000 && ./genseq s2.dna 120000 && ./dist s1.dna s2.dna > resultL1.csv
	cd icc && ./genseq s1.dna 120000 && ./genseq s2.dna 120000 && ./dist s1.dna s2.dna > resultL1.csv
	cd icx && ./genseq s1.dna 120000 && ./genseq s2.dna 120000 && ./dist s1.dna s2.dna > resultL1.csv

	cd gcc && ./genseq s1.dna 500000 && ./genseq s2.dna 500000 && ./dist s1.dna s2.dna > resultL2.csv
	cd icc && ./genseq s1.dna 500000 && ./genseq s2.dna 500000 && ./dist s1.dna s2.dna > resultL2.csv
	cd icx && ./genseq s1.dna 500000 && ./genseq s2.dna 500000 && ./dist s1.dna s2.dna > resultL2.csv

	cd gcc && ./genseq s1.dna 2800000 && ./genseq s2.dna 2800000 && ./dist s1.dna s2.dna > resultL3.csv
	cd icc && ./genseq s1.dna 2800000 && ./genseq s2.dna 2800000 && ./dist s1.dna s2.dna > resultL3.csv
	cd icx && ./genseq s1.dna 2800000 && ./genseq s2.dna 2800000 && ./dist s1.dna s2.dna > resultL3.csv

plot:
	python3 plot.py

clean:
	rm -Rf *~ */genseq */dist */*.optrpt */*.dna */*.csv *.png *.optrpt *.opt.yaml
