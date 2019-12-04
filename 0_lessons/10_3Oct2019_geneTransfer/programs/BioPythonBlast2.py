from Bio.Blast import NCBIWWW # import the module related to BLAST
from Bio import SeqIO

record = SeqIO.read("ermBsequence.txt", format="fasta")

#(which BLAST algorithm to use, what type of database to search, sequence or identifier)
result_handle = NCBIWWW.qblast("blastn", "nt", record.format("fasta")) #nt is nucleotide database, record contain the sequence from the file

# save the output in xml format
save_file = open("my_blast2.xml", "w")
save_file.write(result_handle.read())
save_file.close()
result_handle.close()


