#!/usr/bin/env python3
'''
Implementation of Needleman-Wunsch Algorithm
according to Chapter 3 pseudocode in
Exploring Bioinformatics: A Project-Based Approach by
Caroline St.Clair and Jonathan Visick
'''

# Step 0: Initialization and Read in Sequences

prmpt1_str = "\t Enter first file   :"
prmpt2_str = "\t Enter second file  :"

inFilename1_str = input(prmpt1_str)
inFilename2_str = input(prmpt2_str)

#infile1 = open('Shortsequence1.txt', 'r')
#infile2 = open('Shortsequence2.txt', 'r')

infile1 = open(inFilename1_str, 'r')
infile2 = open(inFilename2_str, 'r')



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
for i in range(1, N+1):  # up to but not including N+1
    matrix[i][0] = matrix[i-1][0] + gap
for i in range(1, M+1):  # up to but not including M+1
    matrix[0][i] = matrix[0][i-1] + gap
for i in range(1, N+1):
    for j in range(1, M+1):
        if seq1[i-1] == seq2[j-1]:
            score1 = matrix[i-1][j-1] + match
        else:
            score1 = matrix[i-1][j-1] + mismatch
        score2 = matrix[i][j-1] + gap
        score3 = matrix[i-1][j] + gap
        matrix[i][j] = max(score1, score2, score3)

# format matrix output
print("\t_____Matrix_____")
for row in matrix:
    for elem in row:
        print(" {:>3} ".format(elem), end=' ')
    print('')

# Step 2: Create Directional Strings

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
        elif ((matrix[currentRow][currentCol-1] + gap)
            == (matrix[currentRow][currentCol])):
            dstring = dstring + 'H'
            currentCol-=1
        elif ((matrix[currentRow-1][currentCol] + gap)
              ==(matrix[currentRow][currentCol])):
            dstring = dstring + 'V'
            currentRow-=1
        else:
            dstring = dstring + 'D'
            currentRow-=1
            currentCol-=1
    return dstring     #end function

dstring = getDirectionalString(matrix, N, M) # call the function getDirectionalString (lines 60-83)
print("\t Directional String : " + dstring)

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

print("\t_____Alignment_____")
perLine = 5
numLines = len(alignSeq1) / perLine  # 50 to a line
if len(alignSeq1) % perLine != 0:
    numLines+=1

for i in range(int(numLines)):
    print(str(i) + ' ', end=' ')
    print(alignSeq1[i*perLine:(i+1)*perLine])
    print(str(i) + ' ', end=' ')
    print(matchLine[i*perLine:(i+1)*perLine])
    print(str(i) + ' ', end=' ')
    print(alignSeq2[i*perLine:(i+1)*perLine])
print("\n\t Alignment Score : " + str(matrix[N][M]))

if (len(seq1) > len(seq2)):
    print("\n\t Match Percentage : " + str((matchCtr*1.0) / len(seq1)))
else:
    print("\n\t Match Percentage : " + str((matchCtr*1.0) / len(seq2)))
