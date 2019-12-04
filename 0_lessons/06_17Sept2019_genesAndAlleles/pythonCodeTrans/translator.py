#!/usr/bin/env python
import sys
import Bio
import random
from Bio import SeqIO, SeqFeature
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import os
import string

# note: If the biopython libs do not load run this,
# export PYTHONPATH=/home/obcarter/biopython/biopython-1.58/

dataDir = "out/"
#dataDir = "/home/obcarter/outhouse/restSiteProj/inter/Bac/" #biobase


def help():
        print """

    Date: 21 Sept 2017: translator.py : Oliver Bonham-Carter 
    --------------------------------------------------------------------
        Program to convert DNA code to RNA and then to protein code.  
        The RNA code is then translated back to DNA for comparison.

        usage: programName <anychar>
        the char here does not have a function but is necessary to run program 

"""

        print "\n   output_dir: ",dataDir
##########################################
        rightversion()
##########################################
# check that the output directory exists #
        tmp = checkDataDir()
##########################################

        return ""
#end of help()

def rightversion():
# function to determine whether biopython 1.58 is running.
        try:
                if Bio.__version__ == "1.58":
                        print "   Using Biopython version: ",Bio.__version__
                        return
        except:
                        print "   Wrong Biopython version"
                        print """   Use: export PYTHONPATH=/home/obcarter/biopython/biopython-1.58/"""
                        sys.exit(0)

        return ""
#end of rightversion()

def checkDataDir():
#function to determine whether a data output directory exists. 
#if the directory doesnt exist, then the program ends
#       print "Checking the dataDir ||",dataDir,"|| does it exist?"
	filename = "check_" + str(random.random())+".chk"
        try:
                f = open(dataDir+filename,"w")
                #f = open(handle,'r')
                f.close()
                os.remove(dataDir+filename)
                return 1
        except IOError:
                print "  PROBLEM: output_dir doesn't exist"
                exit()
                return 0
#end of checkDataDir()



def begin(tmp):

##########################################
# check that the output directory exists #
        #tmp = checkDataDir()		 #
##########################################
# using biopython 1.58?
        rightversion()
        prompt = "   Enter a sequence of DNA         : "
        input = raw_input(prompt)
#        print "  Type of input :",type(input)
        sequence = Seq(input)
#        print "  Sequence: ",sequence
        RNASequence = Seq.transcribe(sequence)
        print "   Transcription (DNA to RNA code) :",str(RNASequence)

        RNAbacktoDNA = Seq.back_transcribe(RNASequence)
        print "   RNA translation back to DNA     :",str(RNAbacktoDNA)

        PROTSequence = Seq.translate(RNASequence)
        print "   Protein code                    :",str(PROTSequence)


#        RNAbacktoDNA = Seq.back_transcribe(RNASequence)
#        print "   RNA translation back to DNA     :",str(RNAbacktoDNA)


#        print "  PROT back to DNA: ",Seq.back_transcribe(PROTSequence)
	return ""
#end of begin()

if __name__ == '__main__':
#	if len(sys.argv) == 2: #one option added to command line
#	begin(sys.argv[1])

    if len(sys.argv) == 2:
         begin(sys.argv[1])
    else:
         print help()
         sys.exit(0)

