'''*************************************
 Honor Code: This work is mine unless otherwise cited.
 Oliver Bonham-Carter
 CMPSC 300 Fall 2017
 Class Example
 Date: 26 Sept 2017

 Purpose: illustrating DNA decoding algorithms using BioPython: 
		   manipulation, transcription, translation
*************************************'''
from Bio.Seq import Seq
#import the IUPAC alphbet definitions
from Bio.Alphabet import IUPAC

#define the variable "myalpha" and assign to it the value "unambiguous_dna"
my_alpha = IUPAC.unambiguous_dna

# Step 0: Initialization and Read in Sequences
infile1 = open('test.txt', 'r') #'r' opens a file for reading only; the file pointer is placed at the beginning of the file MutantAWildType

seq1 = ""
output1 = ""
output2=""
output3=""

infile1.readline()  # bypass > header line
for line in infile1:
    line = line.replace('\n', '')
    seq1 = seq1 + line
    
# convert to all capital letters
seq1=seq1.upper()
print seq1

# Convert seq1 string into a a Sequence object, so we can use Seq functions
dna_seq = Seq(seq1, my_alpha)

# Step 1: DNA Manipulation
# input
temp = raw_input('Is it template or nontemplate? ')
orient = raw_input ('Enter the orientation 5-3 or 3-5: ')

if temp=='template':
	if orient=='3-5':
		output1 = dna_seq.complement()
	elif orient=='5-3':
		output1 = dna_seq.reverse_complement()
elif temp=='nontemplate':
	if orient=='3-5':
		output1 = Seq(seq1[::-1]) # reverse string 
	elif orient=='5-3':
		output1 = dna_seq

print "DNA Manipulation output: ", output1

# Step 2: Transcription
# Assumes nontemplate 5'-3' orientation as an input
output2 = output1.transcribe()

print "Transcription output: ", output2

# Step 3: Translation

output3 = output2.translate()
print "Translation output: ", output3




























