from Bio.Blast import NCBIWWW # import the module related to BLAST
# Import the NCBIXML library, needed to parse the BLAST results
from Bio.Blast import NCBIXML

#help(NCBIWWW.qblast) - to get information on the commands (type q to exit)

#(which BLAST algorithm to use, what type of database to search, sequence or identifier)
result_handle = NCBIWWW.qblast("blastn", "nt", "87042723") #nt is nucleotide database, 87042723 is a GI for S.agalactiae ermB

# save the output in xml format
save_file = open("my_blast1.xml", "w")
save_file.write(result_handle.read())
save_file.close()

result_handle.close()

# open for parsing
result_handle = open("my_blast1.xml")

# use NCBIXML library to parse the results
blast_records = NCBIXML.parse(result_handle)

# Get a BLAST record
blast_record = blast_records.next()

# we can print out some summary info about all hits in our blast report
# beyond a particular threshold.

# Set the threshold value
E_VALUE_THRESH = 0.08

for alignment in blast_record.alignments:
     for hsp in alignment.hsps:            # hsp = high-scoring segment pair
         if hsp.expect < E_VALUE_THRESH:
             print '****Alignment****'
             print 'sequence:', alignment.title
             print 'length:', alignment.length
             print 'e value:', hsp.expect
             print hsp.query[0:75] + '...'
             print hsp.match[0:75] + '...'
             print hsp.sbjct[0:75] + '...'



