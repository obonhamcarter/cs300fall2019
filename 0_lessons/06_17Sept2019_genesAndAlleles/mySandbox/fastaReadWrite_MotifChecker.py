#!/usr/bin/env python3

#*******************************
# CMPSC 300 Fall 2019
# Class Example
# Date: 20 Sept, 2019
# Purpose: Reading and writing FASTA files using the BioPython libraries
#*************************************

from Bio import SeqIO

# biopython install note:
# python3 -m pip install biopython # global install


listt=[]
motifs_list = ["tgc", "cgc", "aaa"]

def checkSeq(record):
	"""Locate a motif in a sequence"""
	#print("\t checkSeq() received sequence :",record, type(record))
	seq = record.seq.lower()
	for m in motifs_list:
		if m in seq:
			print("\t + ",m,"found at position :",seq.find(m))
			listt.append(record) # save the Sequence for which this motif was found
		else:
			pass
			#print("\t Not found ...")
	print("")
# end of checkSeq()

def main():
	"""Driver function for program"""
	# user can enter a filename
	# myFile_str = input("  Enter fasta File :")

	# pre-programmed file names
	# myFile_str = "Diabetes.fasta"
	myFile_str = "NM_001005291.3.fa"

	# open the file, get data_str and then close the file
	data_str = open(myFile_str)
	data_str.close()

	for record in SeqIO.parse(myFile_str,'fasta'):
		id = record.id
		seq = record.seq
		print("\t + Name: ", id)
		print("\t + Size: ", len(seq))
		print("\t + Sequence: ", seq)
		#print("checking for tga and cgc found in seq ...")
		checkSeq(record)
		#myFile_str.close()
#save the file so as to add it to a log of treated files. 
		outFileName_str = myFile_str + "_out.fasta"
		#output_file = open("new_record.fasta", "w")
		outputFile_str = open(outFileName_str,"w")

		SeqIO.write(listt, outputFile_str, "fasta")
		outputFile_str.close()
# end of main()

main() # run the program here
