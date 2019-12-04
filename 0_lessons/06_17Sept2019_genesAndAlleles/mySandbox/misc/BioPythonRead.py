#*************************************
# Honor Code: This work is mine unless otherwise cited.
# Janyl Jumadinova
# CMPSC 300 Spring 2016
# Class Example
# Date: February 11, 2016

# Purpose: Reading file with BioPython
#*************************************

from Bio import SeqIO

my_file = open('Diabetes.fasta')
listt=[]

for record in SeqIO.parse(my_file,'fasta'):
	id = record.id
	seq = record.seq
	print 'Name: ', id 
	print 'Size: ', len(seq)
	print 'Sequence: ', seq
	
	if "tgc" in seq and "cgc" in seq:
		listt.append(record)
my_file.close()


output_file = open("new_record.fasta", "w")
SeqIO.write(listt, output_file, "fasta")
output_file.close()
