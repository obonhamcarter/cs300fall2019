from Bio.Blast import NCBIWWW # import the module related to BLAST
from Bio import SeqIO
from Bio.Blast import NCBIXML

record = SeqIO.read("ermBsequence.txt", format="fasta")

#(which BLAST algorithm to use, what type of database to search, sequence or identifier)
result_handle = NCBIWWW.qblast("blastn", "nt", record.format("fasta")) #nt is nucleotide database, record contain the sequence from the file

# use NCBIXML library to parse the results
blast_records = NCBIXML.parse(result_handle)

# Get a BLAST record
blast_record = blast_records.next()

"""
    Use matplotlib to generate a histogram of Blast bit-score values.
    """
        
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plot


scores = []
    #for blast_record in blast_records.itervalues():
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        scores.append(hsp.score)

plot.hist(scores, len(scores) / 10, facecolor='y')
plot.xlabel('Score')
plot.ylabel('Count')
plot.title('Blast Scores')
plot.grid(True) # Show grid lines
plot.savefig(os.path.join('data_files', 'blast_score_hist.png'))
plot.cla()
