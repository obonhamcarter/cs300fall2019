#!/usr/bin/env python

#*******************************
# CMPSC 300 Fall 2017
# Class Example
# Date: 20 Sept, 2017

# Purpose: Reading and writing FASTA files using the BioPython libraries
#*************************************

from Bio import SeqIO

myFile_str = input("  Enter fasta File :")
data_str = open(myFile_str)
data_str.close()

#my_file = open('Diabetes.fasta')
listt=[]

#for record in SeqIO.parse(my_file,'fasta'):
for record in SeqIO.parse(myFile_str,'fasta'):
	id = record.id
	seq = record.seq
	print("Name: ", id)
	print("Size: ", len(seq))
	print("Sequence: ", seq)
	print("checking for tga and cgc found in seq ...")
	if "tgc" in seq and "cgc" in seq:
		print("\t + found: ",seq)
		listt.append(record) # save the Sequence for which this motif was found
	else:
		print("\t Not found ...")
#myFile_str.close()

outFileName_str = myFile_str + "_out.fasta"
#output_file = open("new_record.fasta", "w")
outputFile_str = open(outFileName_str,"w")

SeqIO.write(listt, outputFile_str, "fasta")
outputFile_str.close()
