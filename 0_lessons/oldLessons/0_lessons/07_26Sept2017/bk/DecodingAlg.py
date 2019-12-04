'''*************************************
 Honor Code: This work is mine unless otherwise cited.
 Janyl Jumadinova
 CMPSC 300 Spring 2016
 Class Example
 Date: February 18, 2016

 Purpose: illustrating DNA decoding algorithms: 
		   manipulation, transcription, translation
*************************************'''

# Step 0: Initialization and Read in Sequences
infile1 = open('test.txt', 'r') #'r' opens a file for reading only; the file pointer is placed at the beginning of the file MutantAWildType

seq1 = ""
output1 = ""
output2=""
output3=""

infile1.readline()  # bypass > header line
for line in infile1:
    line = line.replace('\n', '')
    seq1 = seq1 + line
    
# convert to all capital letters
seq1=seq1.upper()
print seq1

# Step 1: DNA Manipulation
# input
temp = raw_input('Is it template or nontemplate? ')
orient = raw_input ('Enter the orientation 5-3 or 3-5: ')

if temp=='template':
	if orient=='3-5':
		output1 = seq1
	elif orient=='5-3':
		output1 = seq1[::-1] # reverse string
elif temp=='nontemplate':
	if orient=='3-5':
		for c in reversed(seq1):
			if c=='A':
				output1 += 'T'
			elif c=='C':
				output1 += 'G'
			elif c=='G':
				output1 += 'C'
			else: # c is 'T'
				output1 += 'A'
	elif orient=='5-3':
		for c in seq1:
			if c=='A':
				output1 += 'T'
			elif c=='C':
				output1 += 'G'
			elif c=='G':
				output1 += 'C'
			else: # c is 'T'
				output1 += 'A'

print "DNA Manipulation output: ", output1

# Step 2: Transcription

output2 = output1.replace('A','U')
output2 = output2.replace('T','A')
output2 = output2.replace('G','c')
output2 = output2.replace('C','G')
output2 = output2.upper()

print "Transcription output: ", output2

# Step 3: Translation
# dictionary: key-value, codon in mRNA-amino acid
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

for i in range(0, len(output2), 3):
	output3 += codes[output2[i:i+3]]
print "Translation output: ", output3




























