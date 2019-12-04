from Bio.SeqUtils import GC
import pylab
import matplotlib.pyplot as plt
import numpy as np

winSize = 5 # size of the sliding window
# winSize = 10

def plotter(in_list):
	""" Create a plot from the inputted data"""
	x = np.asarray([i for i in range(len(in_list))])
	y = np.asarray(in_list) 
	plt.scatter(x, y, s=80, facecolors = 'none', edgecolors = 'r')
	plt.plot(x,y)
	plt.show()

#end of plotter()

def getGcContent(in_str):
#	print "  Getting GC content in getGcContent()."
	return GC(in_str) 
#end of getGcContent()

def slidingWindow(in_str):
#	print "  This is a slidingWindow() method."
	gcContent_dic = {} # define the dictionary
	for i in range(0,len(in_str), winSize): 
		chunk_str = in_str[i:i+winSize]
		#print i, in_str[i:i+winSize]
		gcContent_dic[i] = getGcContent(chunk_str)
	return gcContent_dic	
#end of slidingWindow()


def begin():
# driver method of the program
	seq_str="ATATATTTTTTGCGCGCGGCGCGT"
	gcContent_dic = slidingWindow(seq_str)
	print "gccontent :", gcContent_dic
	l_list = [gcContent_dic[i] for i in gcContent_dic]
	plotter(l_list)	
#end of begin()


begin()


