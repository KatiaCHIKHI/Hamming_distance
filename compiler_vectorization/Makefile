CC=gcc

CFLAGS=-Wall -g

OFLAGS=-march=native -ftree-vectorize -fopt-info-vec-optimized -O3 -fopt-info-all=dist.gcc.optrpt
INTEL_FLAGS=-xhost  -xAVX -qopt-report=5 -qopt-report-phase=vec -O3 -qopt-report
INTELx_FLAGS=-xhost -O3 -qopt-report

all: genseq dist

dist: dist.c
	$(CC) $(CFLAGS) $(OFLAGS) $< -o gcc/$@
	icc $(CFLAGS) $(INTEL_FLAGS) $< -o icc/$@
	icx $(CFLAGS) $(INTELx_FLAGS) $< -o icx/$@

genseq: genseq.c
	$(CC) -march=native $(CFLAGS) -Ofast $< -o gcc/$@
	icc -march=native $(CFLAGS) -Ofast $< -o icc/$@
	icx -march=native $(CFLAGS) -Ofast $< -o icx/$@

run:
	cd gcc && ./genseq s1.dna 60000 && ./genseq s2.dna 60000 && ./dist s1.dna s2.dna > result.csv
	cd icc && ./genseq s1.dna 60000 && ./genseq s2.dna 60000 && ./dist s1.dna s2.dna > result.csv
	cd icx && ./genseq s1.dna 60000 && ./genseq s2.dna 60000 && ./dist s1.dna s2.dna > result.csv

plot:
	python3 plot.py

clean:
	rm -Rf *~ */genseq */dist */*.optrpt */*.dna */*.csv *.png *.optrpt *.opt.yaml
