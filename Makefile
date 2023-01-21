# MAIN MAKEFILE, RUN FROM HERE

all:
	cd initial && mkdir -p gcc icc icx && ${MAKE}
	cd memory_align && mkdir -p gcc icc icx && ${MAKE}
	cd custom_popcount && mkdir -p gcc icc icx && ${MAKE}
	cd unroll && mkdir -p gcc icc icx && ${MAKE}
	cd compiler_vectorization && mkdir -p gcc icc icx && ${MAKE} 
	cd omp_vectorization && mkdir -p gcc icc icx && ${MAKE} 
	cd omp_parallelization && mkdir -p gcc icc icx && ${MAKE}  
	cd cache_levels && mkdir -p gcc icc icx && ${MAKE}
	cd oflags && mkdir -p gcc icc icx && ${MAKE}
	

run: 
	cd initial && ${MAKE} run
	cd memory_align && ${MAKE} run
	cd custom_popcount && ${MAKE} run
	cd unroll && ${MAKE} run
	cd compiler_vectorization && ${MAKE} run
	cd omp_vectorization && ${MAKE} run
	cd omp_parallelization && ${MAKE} run
	cd cache_levels && ${MAKE} run
	cd oflags && ${MAKE} run

plot:
	cd initial && ${MAKE} plot
	cd memory_align && ${MAKE} plot
	cd custom_popcount && ${MAKE} plot
	cd unroll && ${MAKE} plot
	cd compiler_vectorization && ${MAKE} plot
	cd omp_vectorization && ${MAKE} plot
	cd omp_parallelization && ${MAKE} plot
	cd cache_levels && ${MAKE} plot
	cd oflags && ${MAKE} plot

clean:
	cd initial && ${MAKE} clean
	cd memory_align && ${MAKE} clean
	cd custom_popcount && ${MAKE} clean
	cd unroll && ${MAKE} clean
	cd compiler_vectorization && ${MAKE} clean
	cd omp_vectorization && ${MAKE} clean
	cd omp_parallelization && ${MAKE} clean
	cd cache_levels && ${MAKE} clean
	cd oflags && ${MAKE} clean