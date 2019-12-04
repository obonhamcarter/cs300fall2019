#!/usr/bin/env python

#*******************************
# CMPSC 300 Fall 2017
# Lab 5
# Date: 04 October, 2017
# Purpose: This program can manipulate sequences, transcribe and translate them and find mutations or general differences 
# by comarison between sequences.
#*************************************

from Bio import SeqIO
from Bio.Seq import Seq

def begin():
#Set to open the file saved in the directory
    file1 = raw_input(" Enter File 1: ")
    file2 = raw_input(" Enter File 2: ")

    seq1_str = ""
    seq2_str = ""
    seq_list = []

    for record in SeqIO.parse(file1, "fasta"):
        seq1_str = record.seq

    for record in SeqIO.parse(file2, "fasta"):
        seq2_str = record.seq


    print " Your first sequence is the following  : ",seq1_str
    seq_list.append(seq1_str)

    print " Your second sequence is the following : ",seq2_str
    seq_list.append(seq2_str)

#store the sequences in a list. 
# dna1 and dna2 sequences are stored at seq_list[0] and seq_list[1] 



    RNAfromDNA1_str = Seq.transcribe(seq1_str) #gives RNA1 sequence
    seq_list.append(seq1_str)

    RNAfromDNA2_str = Seq.transcribe(seq2_str) #gives RNA2 sequence
    seq_list.append(seq2_str)


    DNAfromRNA1_str = Seq.back_transcribe(RNAfromDNA1_str) #gives DNA1 sequence from the RNA converse
    seq_list.append(DNAfromRNA1_str)

    DNAfromRNA2_str = Seq.back_transcribe(RNAfromDNA2_str) #gives DNA2 sequence from the RNA converse
    seq_list.append(DNAfromRNA2_str)

    PROTfromRNA1_str = Seq.translate(RNAfromDNA1_str) #gives Protein1
    seq_list.append(PROTfromRNA1_str)

    PROTfromRNA2_str = Seq.translate(RNAfromDNA2_str) #gives Protein2
    seq_list.append(PROTfromRNA2_str)


    # show that strings are stored in the list.
    for i in range(len(seq_list)):
        thisSeq_str = seq_list[i]
        print " Stored sequence : ",i,"  ",thisSeq_str[:20], "..."



    print " ___ First sequence: up to twenty chars___"
    print " Original  DNA  :",seq1_str[:20]," ..."
    print " RNA from  DNA  :",RNAfromDNA1_str[:20]," ..."
    print " DNA from RNA  :",DNAfromRNA1_str[:20]," ..."
    print " PROT from RNA1 :",PROTfromRNA1_str[:20]," ..."


    return seq1_str, seq2_str
#end of begin()

def compareSequences(seq1,seq2):
    print " compareSequences() seq1 : ", seq1[:20],"..."
    print " compareSequences() seq2 : ", seq2[:20],"..."

    print " TODO : Now all you have to do is to send each pair"
    print " of sequences in the same way that these DNA sequences"
    print " were sent to this method.  Then build the comparison" 
    print " algorithm and see where the differences are found. "

#end of compareSequences()

seq_list = begin()
print "   After running the begin() method, we have the following sequences:"
print "   DNA Seq1_str[:20]",seq_list[0][:20]," ..."
print "   DNA Seq2_str[:20]",seq_list[1][:20]," ..."

print " Comparing the DNA sequences..."
compareSequences(seq_list[0], seq_list[1])
