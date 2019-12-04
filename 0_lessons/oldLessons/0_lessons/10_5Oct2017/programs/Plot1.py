from Bio.Blast import NCBIWWW # import the module related to BLAST
from Bio import SeqIO

record = SeqIO.parse("ls_orchid.fasta", format="fasta")


sizes = [len(rec) for rec in record]
print len(sizes), min(sizes), max(sizes)
print sizes

import pylab
pylab.hist(sizes, bins=20)
pylab.title("%i  sequences\nLengths %i to %i" \
            % (len(sizes),min(sizes),max(sizes)))
pylab.xlabel("Sequence length (bp)")
pylab.ylabel("Count")
pylab.show()

         
  