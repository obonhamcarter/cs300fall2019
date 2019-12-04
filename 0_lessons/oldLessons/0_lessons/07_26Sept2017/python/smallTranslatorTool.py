#!/usr/bin/env python

from Bio.Seq import Seq

dna_str = "atgccttttcccccgctagatcgatccccccccccccccccccccccc"

sequence = Seq(dna_str)

RNAfromDNA_str  = Seq.transcribe(sequence) # gives RNA sequence
DNAfromRNA_str  = Seq.back_transcribe(RNAfromDNA_str) # gives DNA sequence from the RNA conversion
PROTfromRNA_str = Seq.translate(RNAfromDNA_str)


print " Original DNA  :",dna_str
print " RNA from DNA  :",RNAfromDNA_str
print " DNA from RNA  :",DNAfromRNA_str
print " PROT from RNA :",PROTfromRNA_str
print " End of program!"
