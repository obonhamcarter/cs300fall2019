# -*- coding: utf-8 -*-
#--- Ch1ProgrApp.py -------------------------------------------------------------------------------------------------------
# A Python program that reads a DNA sequence from a file and computes all ORFs.
#
# 
# Written by:   Nan Jiang, Melanie Chin              The College of Wooster
# Written for:  IDPT 200                             Feb. 9, 2015
#----------------------------------------------------------------------------------------------------------------------
import re

lines = []
with open('SREBF1.fasta') as f:
    for line in f:
        #line = line.strip()
        lines.append(line)

seq = ''.join(lines)
print seq

rgx = re.compile('(ATG)(...){1,}?(TAA|TAG|TGA)',re.IGNORECASE)
iterator = rgx.finditer(seq)
count = 0
for ORF in iterator:
    count = count + 1
    #print "ORF",count,":",ORF.group()
    #print "Position:",ORF.span(), '\n'
    
print 15*'-', "Results", 15*'-'
print "The sequence length is", len(seq)
print "I found",count,"genes"


