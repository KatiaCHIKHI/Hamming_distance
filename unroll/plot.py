import matplotlib.pyplot as plt
import numpy as np
import csv

gcc_gib=0.0
icc_gib=0.0
icx_gib=0.0

gcc_ns=0.0
icc_ns=0.0
icx_ns=0.0

with open('gcc/result.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=' ')
    for row in lines:
        if row[0] == "bandwidth(GiB/s)":
            gcc_gib = float(row[1])
        elif row[0] == "elapsed_time(ns)":
            gcc_ns = float(row[1])

with open('icc/result.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=' ')
    for row in lines:
        if row[0] == "bandwidth(GiB/s)":
            icc_gib = float(row[1])
        elif row[0] == "elapsed_time(ns)":
            icc_ns = float(row[1])

with open('icx/result.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=' ')
    for row in lines:
        if row[0] == "bandwidth(GiB/s)":
            icx_gib = float(row[1])
        elif row[0] == "elapsed_time(ns)":
            icx_ns = float(row[1])

# creating the dataset for gib/s
data_gib = {'gcc':gcc_gib, 'icc':icc_gib, 'icx':icx_gib}
compilers_gib = list(data_gib.keys())
values_gib = list(data_gib.values())

# creating the dataset for nanoseconds
data_ns = {'gcc':gcc_ns, 'icc':icc_ns, 'icx':icx_ns}
compilers_ns = list(data_ns.keys())
values_ns = list(data_ns.values())

fig = plt.figure(figsize = (12, 8))
plt.suptitle("Performance des differents compilateurs C pour calculer la distance Hamming des séquences ADN\n (GCC UNROLL 4 vs ICC/ICX UNROLL 4)")


plt.subplot(1,2,2)

# creating the bar plot
plt.bar(compilers_gib, values_gib, color ='maroon',
        width = 0.4)

#add value labels above bars
for i in range(len(compilers_gib)):
        plt.text(i,values_gib[i],values_gib[i])
plt.xlabel("Compilers")
plt.ylabel("GiB/s")



plt.subplot(1,2,1)

plt.bar(compilers_ns, values_ns, color ='blue',
        width = 0.4)

#add value labels above bars
for i in range(len(compilers_ns)):
        plt.text(i,values_ns[i],values_ns[i])
        
plt.xlabel("Compilers")
plt.ylabel("nanoseconds")


plt.savefig("results.png")