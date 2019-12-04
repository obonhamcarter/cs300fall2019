

from Bio import AlignIO
alignments = AlignIO.parse("ermBsequences.txt", "fasta")
for alignment in alignments:
    print alignment
    print
    
    
for alignment in AlignIO.parse(handle, "fasta", seq_count=2):
    print "Alignment length %i" % alignment.get_alignment_length()
    for record in alignment:
        print "%s - %s" % (record.seq, record.id)
    print
