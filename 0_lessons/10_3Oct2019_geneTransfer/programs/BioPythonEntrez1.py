# Reading a fasta file from the internet

# Import what you need
from Bio import Entrez
from Bio import SeqIO


# Set your email address for accessing Entrez.
# This is used to keep track of your usage.
# In case of excessive usage of the E-utilities, NCBI will attempt to contact
# a user at the email address provided before blocking access to the
# E-utilities.
Entrez.email = 'jjumadinova@allegheny.edu'

# Use the Entrez.efetch method to get a handle for the file by its id number
handle = Entrez.efetch(db="nucleotide", rettype="fasta", id="87042723")

# Read a record from the file through the handle
seq_record = SeqIO.read(handle, "fasta")

# close the handle
handle.close()

# print information from the record
print "%s with %i features" % (seq_record.id, len(seq_record.features))

