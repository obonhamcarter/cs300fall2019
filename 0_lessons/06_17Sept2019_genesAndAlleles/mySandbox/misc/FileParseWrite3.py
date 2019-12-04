#*************************************
# Honor Code: This work is mine unless otherwise cited.
# Janyl Jumadinova
# CMPSC 300 Spring 2016
# Class Example
# Date: February 9, 2016

# Purpose: parsing a FASTA file and comparing two sequences
#*************************************

# Read input from a fasta file and print out their name and sequence
# Notes: In the first line of program, you may need to adjust the path to the file accordingly, 
# Iif not saved in the same directory where your program is
my_file = open('Diabetes.fasta') # open the file
count = 0
name=""
sequence=""
seqList=[]

# now parse through the whole file and save all sequences in a list
for line in my_file:	
	if count%2==0:
		name=line[1:-1] # remove the first and the last character
		print "name: ", name # print the name
	else:
		sequence=line.replace(" ","") # remove the spaces
		sequence=sequence.replace("\n","") # remove new lines
		sequence=sequence.upper() # convert the letters to upper case
		print "sequence: ", sequence # print the sequence
		seqList.append(sequence) # add the sequence to the list
	count+=1

print "List: ", seqList # print the list

my_file.close() # close the file

len1 = len(seqList[0]) # length of the first sequence in the list
len2 = len(seqList[1]) # length of the second sequence in the list
seq_a = seqList[0] # first sequence in the list
seq_b = seqList[1] # second sequence in the list

print "Comparison: ", cmp(seq_a, seq_b) # compares two strings for equality

# Creates a file and writes the mismatch letters
fileOutput = open('results.fasta','w')

for pos in range (0,min(len1,len2)) : # for all the characters in a shortest sequence
	if seq_a[pos] != seq_b[pos]: # if the letters are not the same
		fileOutput.write("Mismatched letter: "+seq_a[pos]+" at position: "+str(pos)+"\n") # write to the file the mismatched letter and its position

fileOutput.close() # close the output file

