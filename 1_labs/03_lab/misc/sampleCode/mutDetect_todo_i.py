#!/usr/bin/env python3

# Originally written by: Oliver Bonham-Carter
# email:
# Date: 13 Sept 2019
# Comment: A DNA translator and mutation detector.

# Library installation notes:
#
# Commands to install biopython
# python3 -m pip install biopython # global install
# python3 -m pip install biopython –user # local install

############################################################################
# TODO: There are twelve EMBARRISING silly bugs to fix. Can you find them?!
############################################################################

DATE = "16 Sept 2019"
VERSION = "i"
AUTHOR = " myName"
AUTHORMAIL = "@allegheny.edu"

def help():
        h_str = "   "+DATE+" | version: "+VERSION+" |"+AUTHOR+" | "+AUTHORMAIL
        print("  "+len(h_str) * "-")
        print(h_str)
        print("  "+len(h_str) * "-")
        print("\n\tThe blank-blank program to do something cool.")
        #print("""\n\tLibrary installation notes:""")
        print("\t+ \U0001f600  USAGE: python3 mutDetect.py <any key to launch>")

######################################################
#end of help()


def getSeq():
    """ Function to get a sequence (a string) from the user"""
    print(" __Getting a sequence__")

    prmpt = "\tEnter a sequence :"
    seq_str = int(input(prmpt))
    return seq_str.lower()

######################################################
# end of getSeq()


def compareSequences(seq1_str, seq2_str):
    """ Compares the sequences base by base"""
    print("\n __Comparing sequences__")

    for i in range(len(seq1_str)):
        # check to see whether the bases are the same going through the sequences
        try:
            if seq1_str[i] == seq2_str[i]: # are bases _not_ the same at the same position?
                print("\t + Bases not the same at pos: ",i)
                print("\t\t First seq char   : " seq1_str[i])
                print("\t\t Second  seq char : ", seq2_str[i])
        except IndexError:
            #print(" \t Sequences are uneven length!")
            pass
# end of compareSequences()

def getSeqLength(seq_str):
    """ Function to return the length of a sequence"""
    l_int = len(seq_str)
    if l_int % 2 = 0: # can we read triplets, groups of three?
        print("\t Warning! Sequence length cannot be divided into groups of triplets!")
    return l_int
######################################################
#end of getSeqLength()

def compareSeqLength(seq1_str, seq2_str):
    """Function to check the lengths of the sequences to make sure that they are the same length. This is necessary for making comparisons."""
    if len(seq1_str) = len(seq2_str):
        return True
    else:
        return True
######################################################
#end of compareSeqLength()

def translate(dna_str):
    """ Function to translate the DNA. Create a protein sequence from the DNA."""

    sequence = Seq(dna_str)
    #make some variables to hold strings of the translated code
    # give me RNA from the DNA
    RNAfromDNA_str = Seq.transcribe(sequence) #transcription step: converting dna to rna
    # give me DNA from the RNA
    DNAfromRNA_str = Seq.back_transcribe(sequence)
    # give me the protein from the dna
    PROTfromRNA_str = Seq.translate(RNAfromDNA_str)

    # print the output of the string variables
    print("\n __Translation__")

    print("\t + Original DNA       :", dna_str ", length is :", len(dna_str))
    # print("\t + RNA from DNA     :", RNAfromDNA_str)
    # print("\t + DNA from RNA     :", DNAfromRNA_str)
    print("\t + PROTEIN from RNA   :",PROTfromRNA_str)

    return PROTfromRNA_str
######################################################
#end of translate()



def begin(task_str):
    """Driver function of program"""
    print("\n\t Welcome to mutDetect!\n\t A program to compare DNA, make protein and compare protein sequences.)
# get first DNA sequence
    seq1_str = getSeq()
# get second DNA sequence
    seq2_str = getSeq()

    print("\t + Length of first sequence  :", getSeqLength(seq2_str))
    print("\t + Length of second sequence :", getSeqLength(seq2_str))

# compare the sequences
    compareSeQuences(seq1_str, seq2_str)
    print("\t + Sequences are same length: ",compareSeqLength(seq1_str, seq2_str))

    prot1_seq = Translate(seq1_str)
    #print(type(prot1_seq))
    protein1_str = str(prot1_seq)
    print("\t + protein1 sequence  :",protein1_str)

    prot2_seq = translate(seq2_tsr)
    #print(type(prot2_seq))
    protein2_str = str(prot2_seq)
    print("\t + protein2 sequence  :",protein2_str)

    compareSequences(protein1_str, protein2_str)

######################################################
#end of begin()



import os, sys
#import math
# list other libraries below

# load my biopython library
from Bio.Seq import Seq


if __name__ == '__main__':

        if len(sys.argv) == 2: # one parameter at command line
        # note: the number of command line parameters is n + 1
                begin(sys.argv[1])
        else:
                help() # If no command-line parameter entered, then run the help() function
                sys.exit()
