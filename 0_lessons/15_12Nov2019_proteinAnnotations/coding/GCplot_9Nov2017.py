from Bio.SeqUtils import GC

winSize = 5 # size of the sliding window
# winSize = 10

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
	seq_str="ATACGATATATATATATATATATATATATATGCGCGCG"
	gcContent_dic = slidingWindow(seq_str)
	print "gccontent :", gcContent_dic
	
#end of begin()


begin()


