'''
Exploring Bioinformatics: A Project-Based Approach
Caroline St.Clair and Jonathan Visick

Chapter 2 - Skills 1 Solution
'''
import sys

# Step 1: Initialization and Read in Sequences

infile1 = open('wildtype.txt', 'r')
infile2 = open('mutantB.txt', 'r')
outfile = open('ch2sk1out.txt', 'w')

seq1 = ""
infile1.readline()  # bypass > header line
for line in infile1:
    line = line.replace('\n', '')
    seq1 = seq1 + line

seq2 = ""
infile2.readline()  # bypass > header line
for line in infile2:
    line = line.replace('\n', '')
    seq2 = seq2 + line

if len(seq1) != len(seq2):
    print "Sequences invalid - unequal length"
    sys.exit()

# Step 2: Transcription

seq1 = seq1.replace('T', 'U')

# convert strings to lists in order to mutate
seq1List = list(seq1)
seq2List = list(seq2)
for idx, value in enumerate(seq1List):
    if seq1List[idx] == 'T':
        seq1List[idx] = 'U'
    if seq2List[idx] == 'T':
        seq2List[idx] = 'U'

# convert list to strings for easy use of substring
seq1 = ''.join(seq1List)
seq2 = ''.join(seq2List)       

# Step 3: Translation

aminoacid1 = aminoacid2 = ''
codes = dict(GCA='A', GCC='A', GCG='A',GCU='A',
             AGA='R', AGG='R', CGA='R', CGC='R', CGG='R', CGU='R',
             AAU='N', AAC='N',
             GAC='D', GAU='D',
             UGC='C', UGU='C',
             GAA='E', GAG='E',
             CAA='Q', CAG='Q',
             GGA='G', GGC='G', GGG='G', GGU='G',
             CAC='H', CAU='H',
             AUA='I', AUC='I', AUU='I',
             CUA='L', CUC='L', CUG='L', CUU= 'L', UUA='L', UUG='L',
             AAA='K',AAG='K', AUG='M',
             UUC='F', UUU='F',
             CCA='P', CCC='P', CCG='P', CCU='P', 
             AGC='S', AGU='S', UCA='S', UCC='S', UCG= 'S', UCU='S', 
             ACA='T', ACC='T', ACG='T', ACU='T',
             UGG='M',
             UAC='Y', UAU='Y', GUA='V', GUC='V', GUG='V', GUU='V',
             UAA='-', UAG='-', UGA='-')

for i in range(0, len(seq1), 3):
    aminoacid1 = aminoacid1 + codes[seq1[i:i+3]]
    aminoacid2 = aminoacid2 + codes[seq2[i:i+3]]

# Step 4: String Comparison
   
mctr = 0
for i in range(0, len(aminoacid1)):
    if (aminoacid1[i] != aminoacid2[i]):
        mctr+=1
        print aminoacid1[i] + str(i+1) + aminoacid2[i]
        outfile.write(aminoacid1[i] + str(i+1) + aminoacid2[i] + '\n')
print "Number of mutations: " + str(mctr)
outfile.write("Number of mutations: " + str(mctr) + '\n')

print seq1
print aminoacid1
outfile.write(seq1 + '\n')
print seq2
print aminoacid2
outfile.write(seq2 + '\n') 