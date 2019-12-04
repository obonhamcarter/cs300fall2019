#!/usr/bin/env python3

# 12 September 2019

# load my biopython library
from Bio.Seq import Seq

# define my DNA sequence (randomly made)
dna_str = "atgcgcgctagatcgatagta"

sequence = Seq(dna_str)

#make some variables to hold strings of the translated code

# give me RNA from the DNA
RNAfromDNA_str = Seq.transcribe(sequence) #transcription step: converting dna to rna
# give me DNA from the RNA
DNAfromRNA_str = Seq.back_transcribe(sequence)
# give me the protein from the dna
PROTfromRNA_str = Seq.translate(RNAfromDNA_str)

# print the output of the string variables

print("\t 1 Original DNA     :", dna_str, ", length is :", len(dna_str))
print("\t 1 RNA from DNA     :", RNAfromDNA_str)
print("\t 1 DNA from RNA     :", DNAfromRNA_str)
print("\t 1 PROTEIN from RNA :",PROTfromRNA_str)



##################################################
# new sequence
##################################################
dna_str = "atgcgcgctagattcgatagta"

sequence = Seq(dna_str)

#make some variables to hold strings of the translated code

# give me RNA from the DNA
RNAfromDNA_str = Seq.transcribe(sequence) #transcription step: converting dna to rna
# give me DNA from the RNA
DNAfromRNA_str = Seq.back_transcribe(sequence)
# give me the protein from the dna
PROTfromRNA_str = Seq.translate(RNAfromDNA_str)

# print the output of the string variables

print("\n\t 2 Original DNA     :", dna_str, ", length is :", len(dna_str))
print("\t 2 RNA from DNA     :", RNAfromDNA_str)
print("\t 2 DNA from RNA     :", DNAfromRNA_str)
print("\t 2 PROTEIN from RNA :",PROTfromRNA_str)
