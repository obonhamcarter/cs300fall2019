# Reading a multiple files from the internet
# Save the output into a file

from Bio import Entrez
from Bio import SeqIO
Entrez.email = "jjumadinova@allegheny.edu"

# search Entrez for a gene
search = Entrez.read(Entrez.esearch(db='nucleotide', term='ermB[gene]', retmode='xml'))
mylist = search["IdList"]

# Use the Entrez.efetch method to get a handle for the file by its id number
handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text",
                       id=', '.join(mylist))

# create an output file
output_file = open("ermB_record.fasta", "w")

# read multiple records through the handle and print some info
for seq_record in SeqIO.parse(handle, "gb"):
    print("%s %s..." % (seq_record.id, seq_record.description[:50]))
    print("Sequence length %i, %i features, from: %s"
          % (len(seq_record), len(seq_record.features), seq_record.annotations["source"]))
          # output seqs to the file
    SeqIO.write(seq_record, output_file, "fasta")

output_file.close()
handle.close()

