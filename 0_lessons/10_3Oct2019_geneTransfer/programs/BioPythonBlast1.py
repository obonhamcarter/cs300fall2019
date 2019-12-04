from Bio.Blast import NCBIWWW # import the module related to BLAST

#help(NCBIWWW.qblast) - to get information on the commands (type q to exit)

#(which BLAST algorithm to use, what type of database to search, sequence or identifier)
result_handle = NCBIWWW.qblast("blastn", "nt", "87042723") #nt is nucleotide database, 87042723 is a GI for S.agalactiae ermB

# save the output in xml format
save_file = open("my_blast1.xml", "w") 
save_file.write(result_handle.read())
save_file.close()

result_handle.close()



