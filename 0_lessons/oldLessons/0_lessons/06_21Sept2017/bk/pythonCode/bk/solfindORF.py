import re

def findORF(seq, start):
    '''takes: sequence and the start point for ORF search'''
    '''returns: a message if no ORF found and a list with 
                (0)the gene and its absoulte
                (1)start and
                (2)end point'''
    #maximally length
    #genePatt = re.compile('ATG(...)+(TAG|TAA|TGA)')
    genePatt = re.compile('ATG(...){2,}?(TAG|TAA|TGA)')
    mo = genePatt.search( seq[start:] )
    #print mo.span()
    #print seq[mo.start():mo.end()] 
    startGene = mo.start()+start
    endGene = mo.end()+start
    
    if mo:
        return [seq[startGene:endGene], startGene, endGene]
    else:
        return 'No gene'

def main():
    fh = open('SREBF1.fasta')
    
    #read al data in one string and remove \n
    seq = fh.read().upper()
    seq = seq.replace('\n',"")

    seqLen = len(seq)
    newSearchStart = 0#keep track of where to start searching
    allGenesList = []#keep a list of ORFs
    
    while(seqLen - newSearchStart > 0):
        rez = findORF(seq, newSearchStart)
        
        if len(rez)>1:#if ORF returned
            allGenesList.append(rez)
            # find pos after the gene
            newSearchStart = rez[2]
            print rez
        else:#if no ORF
            newSearchStart = newSearchStart+1
            
    #print allGenesList
    print 'RESULTS ',17*'#'
    print 'The sequence length is: ', len(seq) 
    print 'I found ', len(allGenesList), ' gene'
    print  25*'#'
    #for x in allGenesList:
    #    print len(x[0])
    #fh.close()

main()






#try outs
#startPatt = re.compile('ATG')
#endPatt = re.compile('TAG|TAA|TGA')
##seq = fh.read()
##mo = startPatt.findall(seq)
##if(mo):
##    print 'Start:',mo
##mo = endPatt.findall(seq)
##if(mo):
##    print 'Stop',mo      

##for line in fh:
##     mo = startPatt.findall(line)
##     if(mo):
##         print 'Start:',mo
##     mo = endPatt.findall(line)
##     if(mo):
##         print 'Stop',mo         
    

