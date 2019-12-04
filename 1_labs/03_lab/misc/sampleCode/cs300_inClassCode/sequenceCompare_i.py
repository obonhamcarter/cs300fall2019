#!/usr/bin/env python3

# date: 12 Sept 2019

def help():
    """ This is a function to help the user """
    print(" \t This is the help() function() ")
    print(" \t The sequence comparison tool")
    print(" \t Usage: python3 sequenceCompare_i.py")
# end of help()

def begin():
    """ This is the diver funcion of the program"""
    print("\t Welcome to the program!")
    prmpt = " Enter sequence :"
    # first sequence
    seq1_str = input(prmpt)
    print(" \t First sequence is  :", seq1_str)

    # second sequence
    seq2_str = input(prmpt)
    print(" \t Second sequence is :", seq2_str)
    compareSequences(seq1_str, seq2_str) # call the function to compare the sequences

# end of begin()


def compareSequences(seq1_str, seq2_str):
    """ compares the sequences base by base"""
    for i in range(len(seq1_str)):
        # check to see whether the bases are the same going through the sequences
        if seq1_str[i] != seq2_str[i]: # are bases the same at the same position?
            print("\t Bases not the same at pos: ",i)
            print("\t first seq char   : ", seq1_str[i])
            print("\t second  seq char : ", seq2_str[i])
# end of compareSequences()

##############################################
# the program runs using the below functions #
##############################################

help()
begin()
