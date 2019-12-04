#!/usr/bin/env python


def help():
	print " This is the help() method!"
	print " Sequence Comparison tool:"
	print " Usage: ./sequenceCompare.py"
# end of help()


def compareSequences(seqA_str,seqB_str):
# note: a method to compare two entered sequences
	print " This is the compareSequences() method"
	print " seqA_str :",seqA_str
 	print " seqB_str :",seqB_str

	for i in range(len(seqA_str)):
		#print " checking: seqA_str, current char: ",i, seqA_str[i]
		if seqA_str[i] != seqB_str[i]:
			print "\n Sequences are difference at position :", i
			print "   seqA_str[i] = ",seqA_str[i]
			print "   seqB_str[i] = ",seqB_str[i]

# end of compareSequences()


def begin():
	print " This is the the begin() method!"
	print " Note: The entered sequences must be the same length!!"
	prompt_str = "Enter sequence :"
	seqA_str = raw_input(prompt_str)
	seqB_str = raw_input(prompt_str)
	compareSequences(seqA_str,seqB_str)


#end of being()



help()
begin()
