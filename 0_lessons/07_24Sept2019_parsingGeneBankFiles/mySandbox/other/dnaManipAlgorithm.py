#!/usr/bin/env python3

from Bio.Seq import Seq

#dna_str = "atgccttttcccccgctagatcgatccccccccccccccccccccccc"

prompt = "\t  Enter the sequence :"
dnaSeq_str = input(prompt).lower()


prompt = "\t Template or non-template? Enter 't' or 'nt' :"
temp_str = input(prompt).lower()


prompt = "\t 3' to 5' or 5' to 3'? Enter '3-5' or '5-3' :"
orient_str = input(prompt).lower


dnaSeq_str = Seq(dnaSeq_str)


print("\t Original sequence :",dnaSeq_str)


if temp_str.lower() == 't':
        if orient_str =='3-5': # t and 3-5, output is same sequence
                print(" No change to sequence")

        elif orient_str == '5-3': # t and 5-3, output is inversed seq
                dnaSeq_str = dnaSeq_str[::-1]
                

elif temp_str.lower() == 'nt':
        if orient_str =='3-5':
#                dnaSeq_str = Seq(dnaSeq_str)
                dnaSeq_str = dnaSeq_str.reverse_complement()


        elif orient_str =='5-3':
#                dnaSeq_str = Seq(dnaSeq_str)
                dnaSeq_str = dnaSeq_str.complement()

print("\t End of DNA Manipulation algorithm. DNASeq is: ",dnaSeq_str)


# if you want to add some translation functionality ...
sequence = dnaSeq_str
RNAfromDNA_str  = Seq.transcribe(sequence) # gives RNA sequence
DNAfromRNA_str  = Seq.back_transcribe(RNAfromDNA_str) # gives DNA sequence from the RNA conversion
PROTfromRNA_str = Seq.translate(RNAfromDNA_str)


print(" Original DNA  :",dnaSeq_str)
print(" RNA from DNA  :",RNAfromDNA_str)
print(" DNA from RNA  :",DNAfromRNA_str)
print(" PROT from RNA :",PROTfromRNA_str)
print(" End of program!")
