#!/usr/bin/env python

def help():
    print " CS390 : Bioinformatics"
    print " Date  : 12 September 2017"
    print " Author: Oliver Bonham-Carter"
    print " A program to compare two sequences going position by position."
    print " Usage programName and then enter two sequences of the same length."
#end of help()


def compareSeq(seqA_str, seqB_str):
# method to compare the inputted sequences
    #print " seqA_str :", seqA_str
    #print " seqB_str :", seqB_str

    pos_list = [] # define a list

    for i in range(len(seqA_str)):
#        print "  checking character. seqA =",seqA_str[i], seqB_str[i],"= seqB"
        if seqA_str[i] != seqB_str[i]:
            print "   Sequences not equal at position: ", i
#            print "   seqA_str[i]",seqA_str[i]
#            print "   seqB_str[i]",seqB_str[i]
            pos_list.append(i) # add the position differences to the list (like an array)
    return pos_list

#end of compareSeq()



def enterSeqs():
#method to enter the seqs
    prmpt = "    Enter SeqA :"
    seqA_str = string.lower(raw_input(prmpt))

    prmpt = "    Enter SeqB :"
    seqB_str = string.lower(raw_input(prmpt))


#    print " sending the strings to the method called compareSeq()"
    if len(seqB_str) != len(seqA_str): #same length strings
        enterSeqs() # recursive call to ensure that sequences are same length.
    positionsOfDifference_list = compareSeq(seqA_str, seqB_str) #send seqs to be compared
    return positionsOfDifference_list # send this back to the begin() method
#end of enterSeqs()



def begin():
    print "\n ____Program started_____"
    help()
    print "   This is the beginning function."
    positions_list = enterSeqs()# get seqs.
    print "   The sequences differ at the following locations: ",positions_list
    print " ____Program ended_____"
#end of begin() 

import string 
begin() 
