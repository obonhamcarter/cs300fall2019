import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'SH_reads.txt')


with open(my_file, 'r') as reader:
# Read and print the entire file line by line
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        print(line, end='')
        # while line[0] != '>':
            x = line
        line = reader.readline()

print(x)

#strFrag = ['SGALWDV', 'GALWDVP', 'ALWDVPS', 'LWDVPSP', 'WDVPSPV']
strFrag = ['I al', 'always', 'ove ', 'love', 'ys lo', ' you.']

for repeat in range(0, len(strFrag)-1):
    bestMatch = [2, '', ''] #overlap score (minimum value 3), otherStr index, assembled str portion
    for otherStr in strFrag[1:]:
        for x in range(0,len(otherStr)):
            if otherStr[x:] == strFrag[0][:len(otherStr[x:])]:
                if len(otherStr)-x > bestMatch[0]:
                    bestMatch = [len(otherStr)-x, strFrag.index(otherStr), otherStr[:x]+strFrag[0]]
            if otherStr[:-x] == strFrag[0][-len(otherStr[x:]):]:
                if x > bestMatch[0]:
                    bestMatch = [x, strFrag.index(otherStr), strFrag[0]+otherStr[-x:]]
    if bestMatch[0] > 2:
        strFrag[0] = bestMatch[2]
        strFrag = strFrag[:bestMatch[1]]+strFrag[bestMatch[1]+1:]

print(strFrag)
print(strFrag[0])
