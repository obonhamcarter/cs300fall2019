#!/usr/bin/env python3

#*******************************
# CMPSC 300 Fall 2019
# Class Example
# Date: 24 Sept, 2019
# Purpose: Reading and writing FASTA files using the BioPython libraries
#*************************************

from Bio import SeqIO

# biopython install note:
# python3 -m pip install biopython # global install


foundIn_list=[] # a list to hold all sequences from fasta file in which the motifs were found. 
motifs_list = ["tgc", "cgc", "aaa"]

DATE = "24 Sept 2019"
VERSION = "i"
AUTHOR = " myName"
AUTHORMAIL = "@allegheny.edu"

# directories
#OUTPUT_DIR = "/tmp/0out/" # all results are saved in this local directory
OUTPUT_DIR = "0out/" # all results are saved in this local directory
INPUT_DIR = "data/"


def help():
        h_str = "   "+DATE+" | version: "+VERSION+" |"+AUTHOR+" | "+AUTHORMAIL
        print("  "+len(h_str) * "-")
        print(h_str)
        print("  "+len(h_str) * "-")

        print("\n\tThe fastaReadWrite_motifChecker.py .")

        #print("""\n\tLibrary installation notes:""")
        print("\t+ \U0001f600  USAGE: programName <any key to launch>")
#        print("\t+ INPUT directory (your data files are here)     : ",INPUT_DIR)
#        print("\t+ OUTPUT directory (your output is placed here)  : ",OUTPUT_DIR)

#end of help()

def checkSeq(record):
	"""Locate a motif in a sequence"""
	#print("\t checkSeq() received sequence :",record, type(record))
	seq = record.seq.lower()
	for motif in motifs_list:
		if motif in seq:
			print("\t + ",motif,"found at position :",seq.find(motif))
			foundIn_list.append(record) # save the Sequence for which this motif was found
			#print(" foundIn_list: sequence found: ",foundIn_list)
		else:
			pass
			#print("\t Not found ...")
	print("")
# end of checkSeq()

def main(myFile_str):
	"""Driver function for program"""
	# user can enter a filename
	# myFile_str = input("  Enter fasta File :")

	# pre-programmed file names
	# myFile_str = "Diabetes.fasta"
	# myFile_str = "NM_001005291.3.fa"

	print("\t Loading file :",myFile_str)
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
		# outFileName_str = myFile_str + "_out.fasta"
		# #output_file = open("new_record.fasta", "w")
		# outputFile_str = open(outFileName_str,"w")
		#
		# SeqIO.write(foundIn_list, outputFile_str, "fasta")
		# outputFile_str.close()
		saver(myFile_str)
# end of main()


def saver(myFile_str):
	"""function to save the fasta file to show that it has been processed """
	print("\t saving sequences for which the motifs were found ... ")
	print("\t myFile_str :",myFile_str)
#	print("\t foundIn_list :",foundIn_list)
	outFilename_str = myFile_str + "_out.fasta"
	#output_file = open("new_record.fasta", "w")

	outputFile_str = open(outFilename_str,"w")

	SeqIO.write(foundIn_list, outputFile_str, "fasta")
	outputFile_str.close()
# end of saver()

#main() # run the program here

import os, sys

if __name__ == '__main__':

        if len(sys.argv) == 2: # one parameter at command line
        # note: the number of command line parameters is n + 1
                main(sys.argv[1])#,sys.argv[2])#,sys.argv[3], sys.argv[4]),sys.argv[5])
        else:
                help()
                sys.exit()
