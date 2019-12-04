from Bio import Entrez
Entrez.email = "Your.Name.Here@example.org"
handle = Entrez.einfo() # or esearch, efetch, ...
record = Entrez.read(handle)
handle.close()


#handle = Entrez.esummary(db="pubmed", id="19304878,14630660", retmode="xml")
# records = Entrez.parse(handle)
# for record in records:
#   # each record is a Python dictionary or list.
#   print(record['Title'])
# #Biopython: freely available Python tools for computational molecular biology and bioinformatics.
# #PDB file parser and structure class implemented in Python.
# handle.close()


handle = Entrez.efetch(db="nucleotide", id="AY851612", rettype="gb", retmode="text")
print(handle.readline().strip())
