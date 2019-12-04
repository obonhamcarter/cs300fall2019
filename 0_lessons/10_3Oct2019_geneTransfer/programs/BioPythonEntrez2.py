# Reading a multiple files from the internet

from Bio import Entrez
Entrez.email = 'jjumadinova@allegheny.edu'

from Bio import SeqIO

# Use the Entrez.efetch method to get a handle for the file by its id number
handle = Entrez.efetch(db="protein", id="349839,349840", rettype="fasta", retmode="text")

# read multiple records through the handle
records = SeqIO.parse(handle, "fasta")

for seq_record in records:
    print("%s %s..." % (seq_record.id, seq_record.description[:50]))
    print("Sequence length %i, %i features "
          % (len(seq_record), len(seq_record.features)))


# close the handle
handle.close()
