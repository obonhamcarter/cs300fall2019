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
        
my_file.close()

for i in range(0,len(seq),3):
    if seq[i:i+3]=="ATG":
        count += 1

print "Number of ATGs: ", count
