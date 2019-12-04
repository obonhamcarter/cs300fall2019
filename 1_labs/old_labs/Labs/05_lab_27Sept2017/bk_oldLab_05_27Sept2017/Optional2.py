'''
Exploring Bioinformatics: A Project-Based Approach
Caroline St.Clair and Jonathan Visick

Chapter 2 - On Your Own Solution
'''
import sys

# Step 1: Initialization and Read in Sequences

infile1 = open('cftrdna.txt', 'r')
infile2 = open('tomallele.txt', 'r')
outfile = open('ch2out.txt', 'w')

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


# convert to uppercase
seq1 = seq1.upper()
seq2 = seq2.upper()

# prompt user for info on non-template or template strand and order
temp = raw_input("(T)emplate Strand or (N)on-Template Strand")
order = raw_input("(5)-3 or (3)-5")
basepair = {'A':'U', 'T':'A', 'C':'G', 'G':'C'}

            
# Step 2: Transcription

# convert strings to lists in order to mutate
seq1List = list(seq1)
seq2List = list(seq2)
# get sequence in mRNA 5-3 order
if (temp == 'N'):
    if (order == 3):  
        # flip and convert T to U
        seq1List.reverse()
        seq2List.reverse()
    # need separate for loops since lengths may be different
    for idx, value in enumerate(seq1List):
        if seq1List[idx] == 'T':
            seq1List[idx] = 'U'
    for idx, value in enumerate(seq2List):
        if seq2List[idx] == 'T':
            seq2List[idx] = 'U'
elif (temp == 'T'):
    if (order == 5):
        # flip
        seq1List.reverse()
        seq2List.reverse()
    # convert to base pairs
    seq1List = [basepair[elem] for elem in seq1List]
    seq2List = [basepair[elem] for elem in seq2List]

# Lists now in mRNA form 5' to 3' order    

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

# need separate for loops since lengths may be different
for i in range(0, len(seq1)-3, 3):
    aminoacid1 = aminoacid1 + codes[seq1[i:i+3]]
for i in range(0, len(seq2)-3, 3):
    aminoacid2 = aminoacid2 + codes[seq2[i:i+3]]
print "Sequence 1 Nucleotides: " + seq1
print "Sequence 2 Nucleotides: " + seq2
print "Sequence 1 Amino Acids: " + aminoacid1
print "Sequence 2 Amino Acids: " + aminoacid2
outfile.write("Sequence 1 Nucleotides: " + seq1)
outfile.write("Sequence 2 Nucleotides: " + seq2)
outfile.write("Sequence 1 Amino Acids: " + aminoacid1)
outfile.write("Sequence 2 Amino Acids: " + aminoacid2)
# Step 4: String Comparison
choice = raw_input("Compare (N)ucleotide or (A)Amino Acid Sequences")
if (choice == 'N'):
    compseq1 = seq1
    compseq2 = seq2
else:    
    compseq1 = aminoacid1
    compseq2 = aminoacid2

if (len(compseq1) == len(compseq2)):    
    mctr = 0
    for i in range(0, len(compseq1)):
        if (compseq1[i] != compseq2[i]):
            mctr+=1
            print compseq1[i] + str(i+1) + compseq2[i]
            outfile.write(compseq1[i] + str(i+1) + compseq2[i])
            
    print "Number of mutations: " + str(mctr)
    outfile.write("Number of mutations: " + str(mctr))
else:
    numCDN = abs(len(compseq1) - len(compseq2))
    mostMismatches = len(compseq1)
    bestDelItr = 0
    # deletion event
    delStr = "-" * numCDN

    # delItr will determine the location of the consecutive deleted nucleotides within
    # the input string

    maxitr = len(compseq1) - len(compseq2) - numCDN
 
    for delItr in range(0, len(compseq2)+1):
        str2mod = compseq2[:delItr] + delStr + compseq2[delItr:]
        # now determine mismatches of the equal length strings compseq1 and str2mod
        mismatch = 0
        mismatchList = ""
        for itr in range(0, len(compseq1)):
            ch1 = compseq1[itr:itr+1]
            ch2 = str2mod[itr:itr+1]
            if (ch1 != ch2):
                # event occurred - change flag
                mismatch = mismatch + 1
                mismatchList = mismatchList + ch1 + str(itr+1) + ch2 + "  "
        if (mismatch < mostMismatches):
            bestStr2 = str2mod
            mostMismatches = mismatch
            bestMismatchList = mismatchList
            
    matches = len(compseq1) - mostMismatches
    print "Comparing: "
    print "Wild Type: " + compseq1
    print "Mutant: " + bestStr2 
    print "Number of Mistmatches: " + str(mostMismatches) 
    print "Location of Mismatches: " + bestMismatchList
    
