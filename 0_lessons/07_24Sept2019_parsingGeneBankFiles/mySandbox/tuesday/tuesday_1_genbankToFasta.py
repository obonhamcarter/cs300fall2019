#!/usr/bin/env python3

# Date: 23 Sept 2019
# Program to convert a genbank file to a fasta file.
# ref: https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/genbank2fasta/

from Bio import SeqIO



# #### get a simple GenBank file to convert into a fasta file.
#
# - PubMed: nucleotide search(M55025.1)
# - link: https://www.ncbi.nlm.nih.gov/nuccore/M55025.1
# - send to: GenBank file
# - cover code: geneToFasta.py to conver genbank files to fasta format.
# - code ref:  https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/genbank2fasta/
#
# - future code ideas; parsing out features: https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/genbank/
#



prmpt = "\t Enter the genbank filename :"
gbk_filename = input(prmpt)
faa_filename = gbk_filename.replace(".","-") + ".fasta"

#gbk_filename = "NC_005213.gbk"
#faa_filename = "NC_005213_converted.fna"

input_handle  = open(gbk_filename, "r") # read mode
output_handle = open(faa_filename, "w") # write mode

for seq_record in SeqIO.parse(input_handle, "genbank") :
    print("\t GenBank record %s" % seq_record.id)
    output_handle.write(">%s %s\n%s\n" % (
           seq_record.id,
           seq_record.description,
           seq_record.seq))

output_handle.close() # close fasta file
input_handle.close() # close GenBank file
