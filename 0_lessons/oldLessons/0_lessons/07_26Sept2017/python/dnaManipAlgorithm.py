#!/usr/bin/env python

from Bio.Seq import Seq
import string

#dna_str = "atgccttttcccccgctagatcgatccccccccccccccccccccccc"

prompt = "  Enter the sequence :"
dnaSeq_str = string.lower(raw_input(prompt))


prompt = "  Template or non-template? Enter 't' or 'nt' :"
temp_str = string.lower(raw_input(prompt))


prompt = "  3' to 5' or 5' to 3'? Enter '3-5' or '5-3' :"
orient_str = string.lower(raw_input(prompt))


dnaSeq_str = Seq(dnaSeq_str)


print "  Original sequence :",dnaSeq_str


if string.lower(temp_str) == 't':
        if orient_str =='3-5': # t and 3-5, output is same sequence
                print " No change to sequence"

        elif string.lower(orient_str) =='5-3': # t and 5-3, output is inversed seq
                dnaSeq_str = dnaSeq_str[::-1]
                

elif string.lower(temp_str) == 'nt':
        if orient_str =='3-5':
#                dnaSeq_str = Seq(dnaSeq_str)
                dnaSeq_str = dnaSeq_str.reverse_complement()



        elif string.lower(orient_str) =='5-3':
#                dnaSeq_str = Seq(dnaSeq_str)
                dnaSeq_str = dnaSeq_str.complement()

print "  End of DNA Manipulation algorithm. DNASeq is: ",dnaSeq_str



#sequence = dnaSeq_str
#RNAfromDNA_str  = Seq.transcribe(sequence) # gives RNA sequence
#DNAfromRNA_str  = Seq.back_transcribe(RNAfromDNA_str) # gives DNA sequence from the RNA conversion
#PROTfromRNA_str = Seq.translate(RNAfromDNA_str)


#print " Original DNA  :",dnaSeq_str
#print " RNA from DNA  :",RNAfromDNA_str
#print " DNA from RNA  :",DNAfromRNA_str
#print " PROT from RNA :",PROTfromRNA_str
#print " End of program!"
