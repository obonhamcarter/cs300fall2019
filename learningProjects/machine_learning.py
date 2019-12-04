#!/usr/bin/env python



def help():
#print some help on the screen when the program is entered without a parameter
        print """
  Date: 22 October 2013: learning.py
  -------------------------------------------

	A learning program to determine if the user is 
	more likely to enter an even number or an odd one.

	Usage: <programFile> (any paramrter)

	note: The parameter is necessary to start the program 
        and to not display the help screen

"""
	#
	return " " 
#end of help()

def printer(in_thing):
# function to print out contents of the dic or list.
        a = type(in_thing)
        if 'dict' in str(a):
                print "  type: dict"
                for i in in_thing: print "key = ",i,", value = ",in_thing[i]
        if 'list' in str(a):
                print "  type: list"
                for i in range(len(in_thing)): print "i = ", i, "[i] = ",in_thing[i]
#end of printer()

def smartGuesser(in_dic): 
# program to determine which of in_dic's odds and evens has more counts.

	if in_dic["odd"] > in_dic["even"]: return "odd"
	elif in_dic["odd"] == in_dic["even"]: return "tied score"
	else: return "even"

#end of smartGuesser()

def begin(inThing):
	prmpt = "  Enter a number or zero to exit :"
	rsp = 1
	learn_dic = {"odd":0,"even":-1} #the even <- -1 removes the zero entered by the user.
	polarity_flag = 1 # print the polarity report line
        userTries = 0 #total number of inputs
	while (rsp != 0 ):
		try:
			rsp = input(prmpt) #inputs an int
		#	print "  You Entered :",rsp

		except Exception:#IOError:
			try:
				rsp = input("  Your entry is not a number :")
				polarity_flag = 1
			except Exception: #IOError
				rsp = 1
				polarity_flag = 0 # do not print the polarity report now
				learn_dic["even"] = learn_dic["even"] - 1
#record odd or even
		polarity = rsp % 2 # 0 = even value, 1 = odd value

		if polarity_flag == 1: print "  Polarity :",
                if polarity == 0 : print "Even"
                else: print "Odd"

		if polarity == 1: #odd value entered
			learn_dic["odd"] = learn_dic["odd"] + 1
                        userTries = userTries + 1
		elif polarity == 0: #even value entered
			learn_dic["even"] = learn_dic["even"] + 1
                        userTries = userTries + 1
	#printer(learn_dic)
		
	print "\n  Results: \n"
	# printer(learn_dic)
        print "   Total values entered: ",userTries
	print "   The general preference for numbers is:", smartGuesser(learn_dic)
        oddFreq = 1.0 * learn_dic["odd"] / (userTries-1) #remove one for '0' entry
        evenFreq = 1.0 * learn_dic["even"] / (userTries-1) #remove one for '0' entry
        print "   Frequency of picking an Odd number  :", oddFreq 
        print "   Frequency of picking an Even number :", evenFreq
        if oddFreq > evenFreq: print"\n   The user is likely to enter an odd number"
        else: print"\n   The user is likely to enter an even number"
	return " "
#end of begin()

#launch the program
import sys, os, string, random  

if __name__ == '__main__':
#	if len(sys.argv) == 2: #one option added to command line
#	begin(sys.argv[1])

    if len(sys.argv) == 2:
         begin(sys.argv[1])#,sys.argv[2])
    else:
         print help()
         sys.exit(0)
