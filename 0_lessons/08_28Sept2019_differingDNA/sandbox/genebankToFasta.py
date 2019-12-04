#!/usr/bin/env python3
# date: 24 Sept 2019
# inclass coding

# load the biopython library
from Bio import SeqIO

prmpt = "\t Enter the GenBank file name :"
gbk_filename = input(prmpt) # prompt the user to enter a filename for a genbank file

#genbankfilename  filenames look like this --> "myGBfile-gb.fasta"
faa_filename = gbk_filename.replace(".","-") + ".fasta"

# open the files for working
input_handle = open(gbk_filename,"r") # open file for reading (genbank input)
output_handle = open(faa_filename,"w") # open file for writing (fasta output)

# parse the genbank file for relevant information
for seq_record in SeqIO.parse(input_handle, "genbank"):
    print("\t Genbank record: %s" % seq_record.id)
    output_handle.write(">%s %s\n%s\n" % (seq_record.id, seq_record.description, seq_record.seq))

# close the files
output_handle.close() # close the fasta file
input_handle.close() # close the genbank file
