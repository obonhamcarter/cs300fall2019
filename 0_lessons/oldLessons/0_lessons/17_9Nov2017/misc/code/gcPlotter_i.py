#!/usr/bin/env python
# CS300 Bioinformatics
# Date: 9 Nov 2017
# Oliver Bonham-Carter
# ref: http://biopython.org/

# for plotting
import pylab
import matplotlib.pyplot as plt 
import numpy as np 

# for bioinformatics tasks
#from Bio import SeqIO # for opening and reading the fasta files
from Bio.SeqUtils import GC # for measuring the gc content


#winSize = 5 # the size of the sliding window
winSize = 10 # larger values give us a result of lower granularity


def getGcContent(in_str):
	""" inputs a sequence fragment and outputs a score of gc content."""

#	print "GC Content Checker."
	return GC(in_str)
#end of getGcContent()



def slidingWindow(in_str):
	""" method to create a window of length 3 of the sequence. The gc content in the window is stored in a list and returned to the caller method."""

	print "  Sliding window of length :",winSize
        print "\n  Chunks and GC content"
	gcContent_dic = {}
	for i in range(0,len(in_str),winSize):
		seqChunk_str = in_str[i:i+winSize]
		print "   ",i, "| ",seqChunk_str, getGcContent(seqChunk_str)#,type(seqChunk_str)
		gcContent_dic[i] = getGcContent(seqChunk_str)
	return gcContent_dic

#end of slidingWindow 


def scatter(l_list):
    """ create a scatter plot """

    x = np.asarray([i for i in range(len(l_list))])
    y = np.asarray(l_list)
    #plt.scatter(x, y, s=80, facecolors='none', edgecolors='r')
    plt.scatter(x, y, s=40, facecolors='b', edgecolors='b')
    plt.show()
#end of scatter()


def begin():
	"""host method to control the whole program"""

	seq_str = "atatatatatattatatatatagcgcgcgcatatatatatattatatatatagcgcgcgcatatatatatattatatatatagcgcgcgc"
	gcContent_dic = slidingWindow(seq_str) # gather the gc content scores using a window
	#print "begin() :",gcContent_dic # report those scores
	#convert the dictionary to a list
	l_list = [gcContent_dic[i] for i in gcContent_dic ]
	print "  Results of GC content for each chunk:", l_list	
        scatter(l_list)
# end of begin()

begin()
	



