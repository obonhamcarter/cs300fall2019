from Bio import SeqIO
from Bio.Seq import Seq

my_file = open('test.fasta') 
my_list = [] # create empty list
count = 0 
loc = 0 # location of the first atg will be stored here

for record in SeqIO.parse(my_file,'fasta'):
	id = record.id
	seq = record.seq
	print 'Name: ', id 
	print 'Size: ', len(seq)
        
        # if there is at least one ATG in the sequence
        if "ATG" in seq:
            loc = seq.find("ATG")
	
my_file.close()

# output
print "The first ATG is at location", loc
print "Number of ATGs: ", seq.count("ATG")
