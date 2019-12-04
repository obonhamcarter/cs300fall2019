#!/usr/bin/env python3

from Bio import SeqIO
# ref: https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/genbank2fasta/
# date: 27 Sept 2019

prmpt = "\t Enter the genbank filename :"
gbk_filename = input(prmpt)
faa_filename = gbk_filename.replace(".","-") + "_proteins.fasta"

# gbk_filename = "NC_005213.gbk"
# faa_filename = "NC_005213_converted.faa"


input_handle  = open(gbk_filename, "r") # read mode
output_handle = open(faa_filename, "w") # write mode

for seq_record in SeqIO.parse(input_handle, "genbank") :
    print("\t GenBank record %s" % seq_record.id)
    for seq_feature in seq_record.features :
        if seq_feature.type=="CDS" :
            assert len(seq_feature.qualifiers['translation'])==1
            output_handle.write(">%s from %s\n%s\n" % (
                   seq_feature.qualifiers['gene'][0],
                   seq_record.name,
                   seq_feature.qualifiers['translation'][0]))

output_handle.close() # close the fasta file
input_handle.close() # close the GenBank file
