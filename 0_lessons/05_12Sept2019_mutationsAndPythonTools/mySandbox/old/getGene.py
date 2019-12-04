# biopython

# install biopython
# python3 -m pip install biopython


#
from Bio import Entrez
from Bio import SeqIO
Entrez.email = "A.N.Other@example.com"
with Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id="6273291") as handle:
    seq_record = SeqIO.read(handle, "fasta")
print("%s with %i features" % (seq_record.id, len(seq_record.features)))
handle = Entrez.einfo() # or esearch, efetch, ...
record = Entrez.read(handle)
print(handle.readline().strip())

handle.close()
