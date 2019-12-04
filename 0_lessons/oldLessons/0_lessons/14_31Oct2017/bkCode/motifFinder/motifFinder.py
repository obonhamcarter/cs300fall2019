#!/usr/bin/env python
import numpy as np
from collections import defaultdict
from Bio import SeqIO
#seq = "ASGTTTTGAAASGTTTTGAAASGTTTTGAAASGTTTTGAAASGTTTTGAAASGTTTTGAAASGTTTTGAA"

# reads and concatenates 10 promoter sequences
def readSeq():
    seq = ''
    handle = open("Genes10/all.fasta", "rU")
    for record in SeqIO.parse(handle, "fasta") :
        seq = seq + str(record.seq)
    handle.close()
    return seq

# computes frequency of all sixmers
def compute_frequency(counts, seq):
    for i in range(len(seq)-5):
        key = seq[i:i+6]
        counts[key] += 1
    return counts

# shuffles nucleotides in a sequence
def shuffle(seq):
    idx = np.random.permutation(len(seq))
    outSeq = ''
    for i in idx:
        outSeq = outSeq + seq[i]
    return outSeq

def main():
    promoterSeq = readSeq()
    
    # counts holds the frequencies of the sixmers
    counts = defaultdict(int)
    counts = compute_frequency(counts, promoterSeq)
    
    # countsRand holds the frequencies of the sixmers in the shuffled sequence
    countsRand = defaultdict(int)
    
    # shuffle and compute frequencies over 1000 runs
    for i in range(1000):
        countsRand = compute_frequency(countsRand, shuffle(promoterSeq))

    # ratioDict holds the sixmers and their corresponding ratio f/f_random
    ratioDict = defaultdict(float)
    for i in countsRand:
        countsRand[i] = countsRand[i]/1000.0
        ratioDict[i] = counts[i]/float(countsRand[i])
        #print i, counts[i], countsRand[i], counts[i]/float(countsRand[i])

    # display sixmer, true frequency, and frequency in randomized sequence in ordered of ratio f/f_random
    for key, value in sorted(ratioDict.iteritems(), key=lambda (k, v): (v, k)):
        print "%s: %s      %s       %.2f" % (key, counts[key], countsRand[key], value)
        
main()        
        
