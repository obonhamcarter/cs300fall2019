#!/usr/bin/env python

import pylab
from Bio import SeqIO
from Bio.SeqUtils import GC

winSize = 10 # the size of the sliding window
#binSize = 30 # used in the plotter method to control the granularity in the histogram


def getGcContent(in_str):
	""" inputs a sequence fragment and outputs a score of gc content."""
#	print "GC Content Checker."
	return GC(in_str)
#end of getGcContent()



def slidingWindow(in_str):
	""" method to create a window of length 3 of the sequence. The gc content in the window is stored in a list and returned to the caller method."""
	print "Slideing window of length 3"
	gcContent_dic = {}
	for i in range(0,len(in_str),winSize):
		seqChunk_str = in_str[i:i+winSize]
		print "   ",i, "| ",seqChunk_str, getGcContent(seqChunk_str),type(seqChunk_str)
		gcContent_dic[i] = getGcContent(seqChunk_str)
	return gcContent_dic

#end of slideingWindow 


def makePlot(in_list, binSize):
	"""method to plot the contents of a list of numerical values"""

	pylab.hist(in_list, bins=binSize)
#	pylab.title("GC content")
#	pylab.xlabel(" Position in Sequence, bin = %i", binSize)
#	pylab.ylabel("GC Score")
	pylab.show()
# end of makePlot()


def newMakePlot(in_list, bins):
# https://matplotlib.org/1.2.1/examples/api/histogram_demo.html
	import numpy as np
	import matplotlib.pyplot as plt
	import matplotlib.mlab as mlab

#	mu, sigma = 100, 15
##	x = mu + sigma * np.random.randn(10000)
	x = in_list

	fig = plt.figure()
	ax = fig.add_subplot(111)

#	# the histogram of the data
	n, bins, patches = ax.hist(x, 50, normed=1, facecolor='green', alpha=0.75)
	plt.show()


#	# hist uses np.histogram under the hood to create 'n' and 'bins'.
#	# np.histogram returns the bin edges, so there will be 50 probability
#	# density values in n, 51 bin edges in bins and 50 patches.  To get
#	# everything lined up, we'll compute the bin centers
#	bincenters = 0.5*(bins[1:]+bins[:-1])
#	# add a 'best fit' line for the normal PDF
#	y = mlab.normpdf( bincenters, mu, sigma)
#	l = ax.plot(bincenters, y, 'r--', linewidth=1)

	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	#ax.set_title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
	ax.set_xlim(40, 160)
	ax.set_ylim(0, 0.03)
	ax.grid(True)

	plt.show()

# end of newMakePlot()

def scatter(l_list):
    """ create a scatter plot """
    import matplotlib.pyplot as plt 
    import numpy as np 

#    x = np.random.randn(60) 
#    y = np.random.randn(60)

    x = np.asarray([i for i in range(len(l_list))])
    y = np.asarray(l_list)

    plt.scatter(x, y, s=80, facecolors='none', edgecolors='r')
    plt.show()

#end of scatter()


def begin():
	"""host method to control the whole program"""

	seq_str = "atatatatatattatatatatagcgcgcgcatatatatatattatatatatagcgcgcgcatatatatatattatatatatagcgcgcgc"
	gcContent_dic = slidingWindow(seq_str) # gather the gc content scores using a window
	print "begin() :",gcContent_dic # report those scores
	#convert the dictionary to a list
	l_list = [gcContent_dic[i] for i in gcContent_dic ]

	print " List :", l_list	
#	makePlot(l_list,len(seq_str))
#	newMakePlot(l_list,len(seq_str))
        scatter(l_list)
# end of begin()

begin()
	



