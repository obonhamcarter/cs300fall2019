#!/usr/bin/env python3

# file: dnaManipAlgorithm.py
# program to convert an inputted sequence to another. 
# The algorthm is based on the DNA Manipulation Algorithm

from Bio.Seq import Seq

# For debugging, this string could replace the user-input code to speed things up
#dna_str = "atgccttttcccccgctagatcgatccccccccccccccccccccccc"


prompt = "\t  Enter the sequence :"
dnaSeq_str = input(prompt).lower()

prompt = "\t Template or non-template? Enter 't' or 'nt' :"
temp_str = input(prompt).lower()

prompt = "\t 3' to 5' or 5' to 3'? Enter '3-5' or '5-3' :"
orient_str = input(prompt)
print("\t + User picks option: ",orient_str)
dnaSeq_str = Seq(dnaSeq_str)
print("\t Original sequence :",dnaSeq_str)


# the algoritm to determine the sequence primality, conversion and output
if temp_str.lower() == 't':
    print("\t + User picks option: t")
    if orient_str =='3-5': # t and 3-5, output is same sequence
        print("\t seq is: t and 3'-5'")
        print("\t No change to sequence")

    elif orient_str == '5-3': # t and 5-3, output is inversed seq
        print("\t t and 5'-3'")
        dnaSeq_str = dnaSeq_str[::-1]
    else:
        print("\t Unknown primality")
        exit()

elif temp_str.lower() == 'nt':
    print("\t User picks option: nt")
    if orient_str =='3-5':
        print("\t nt and 3'- 5'")
        dnaSeq_str = dnaSeq_str.reverse_complement()

    elif orient_str =='5-3':
        print("\t nt and 5'-3'")
        dnaSeq_str = dnaSeq_str.complement()
    else:
        print("\t Unknown primality")
        exit()

else: 
    print("\t Unknown template type")
    exit()
print("\t + End of DNA Manipulation algorithm. DNASeq is: ",dnaSeq_str,"\n")


# if you want to add some translation functionality ...
print("\t __Translation__")
sequence = dnaSeq_str
RNAfromDNA_str  = Seq.transcribe(sequence) # gives RNA sequence
DNAfromRNA_str  = Seq.back_transcribe(RNAfromDNA_str) # gives DNA sequence from the RNA conversion
PROTfromRNA_str = Seq.translate(RNAfromDNA_str)


print(" Original DNA  :",dnaSeq_str)
print(" RNA from DNA  :",RNAfromDNA_str)
print(" DNA from RNA  :",DNAfromRNA_str)
print(" PROT from RNA :",PROTfromRNA_str)
print(" End of program!")
