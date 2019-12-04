'''
Exploring Bioinformatics: A Project-Based Approach
Caroline St.Clair and Jonathan Visick

Chapter 3 - Skills 5 Solution - Non-recursive Semi Global Alignment
'''
import sys

# function to determine directional string
def getDirectionalString(matrix, N, M):
    dstring = ''
    currentRow = N;
    currentCol = M;
    while (currentRow != 0 or currentCol != 0):
        if currentRow == 0:
            dstring = dstring + 'H'
            currentCol-=1
        elif currentCol == 0:
            dstring = dstring + 'V'
            currentRow-=1
        elif (((matrix[currentRow][currentCol-1] + gap) == (matrix[currentRow][currentCol]))
            or ((currentRow == N) and ((matrix[currentRow][currentCol]) == matrix[currentRow][currentCol-1]))):
            dstring = dstring + 'H'
            currentCol-=1
        elif (((matrix[currentRow-1][currentCol] + gap) == (matrix[currentRow][currentCol]))
            or ((currentCol == M) and ((matrix[currentRow][currentCol]) == matrix[currentRow-1][currentCol]))):
            dstring = dstring + 'V'
            currentRow-=1
        else:
            dstring = dstring + 'D'
            currentRow-=1
            currentCol-=1
    return dstring     

# Step 1: Initialization and Read in Sequences

infile1 = open('Shortsequence1.txt', 'r')
infile2 = open('Shortsequence2.txt', 'r')

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

# Step 1: Build Scoring Matrix

N = len(seq1)
M = len(seq2)
gap = -1
mismatch = 0
match = 1
matrix = [[0 for i in range(M+1)] for j in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if seq1[i-1] == seq2[j-1]:
            score1 = matrix[i-1][j-1] + match
        else:
            score1 = matrix[i-1][j-1] + mismatch
        if i == N:
            score2 = matrix[i][j-1]
        else:
            score2 = matrix[i][j-1] + gap
        if j == M:
            score3 = matrix[i-1][j]
        else:
            score3 = matrix[i-1][j] + gap
        matrix[i][j] = max(score1, score2, score3) 
        
# format matrix output   
print "Matrix"    
for row in matrix:
    for elem in row:
        print " {:>3} ".format(elem),
    print ''
    
# Step 2: Create Directional Strings
dstring = getDirectionalString(matrix, N, M)
print "Directional String: " + dstring

# Step 3: Build Alignments Using Directional Strings
seq1pos = N - 1
seq2pos = M - 1
dirpos = 0;
alignSeq1 = ''
alignSeq2 = ''
matchLine = ''
matchCtr = 0
while (dirpos < len(dstring)):
    if (dstring[dirpos] == 'D'):
        alignSeq1 = seq1[seq1pos] + alignSeq1
        alignSeq2 = seq2[seq2pos] + alignSeq2
        if seq1[seq1pos] == seq2[seq2pos]:
            matchLine = '|' + matchLine
            matchCtr+=1
        else:
            matchLine = '.' + matchLine
        seq1pos-=1
        seq2pos-=1
    elif (dstring[dirpos] == 'V'):
        alignSeq1 = seq1[seq1pos] + alignSeq1
        alignSeq2 = '_' + alignSeq2
        seq1pos-=1
        matchLine = ' ' + matchLine
    else:
        alignSeq1 = '_' + alignSeq1
        alignSeq2 = seq2[seq2pos] + alignSeq2
        seq2pos-=1
        matchLine = ' ' + matchLine
    dirpos+=1

print "Alignment:"
perLine = 50
numLines = len(alignSeq1) / perLine  # 50 to a line
if len(alignSeq1) % perLine != 0:
    numLines+=1

for i in range(int(numLines)):
    print str(i) + ' ',
    print alignSeq1[i*perLine:(i+1)*perLine]
    print str(i) + ' ',
    print matchLine[i*perLine:(i+1)*perLine]
    print str(i) + ' ',
    print alignSeq2[i*perLine:(i+1)*perLine]
print "\nAlignment Score: " + str(matrix[N][M])
if (len(seq1) > len(seq2)):
    print "\nMatch Percentage: " + str((matchCtr*1.0) / len(seq1))
else:
    print "\nMatch Percentage: " + str((matchCtr*1.0) / len(seq2))
