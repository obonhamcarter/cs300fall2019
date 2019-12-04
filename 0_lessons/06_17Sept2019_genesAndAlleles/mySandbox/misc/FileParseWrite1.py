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
		#sequence=line.strip()
		sequence=sequence.replace("\n","") # remove new lines
		sequence=sequence.upper() # convert the letters to upper case
		print "sequence: ", sequence # print the sequence
		seqList.append(sequence) # add the sequence to the list
	count+=1

print "List: ", seqList # print the list

my_file.close() # close the file
