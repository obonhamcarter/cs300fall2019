#!/usr/bin/env python

from Bio.Seq import Seq


dna_str = "atgcgctttcccccccccc"

sequence = Seq(dna_str)
RNAfromDNA_str  = Seq.transcribe(sequence) # convert to RNA
DNAfromRNA_str  = Seq.back_transcribe(sequence) # convert the RNA back to DNA
PROTfromRNA_str = Seq.translate(RNAfromDNA_str)

print "  Original seqDNA    :",dna_str,"Length :",len(dna_str)
print "  DNA to RNA         :",RNAfromDNA_str
print "  RNA to DNA         :",DNAfromRNA_str
print "  PROT from RNA      :",PROTfromRNA_str

