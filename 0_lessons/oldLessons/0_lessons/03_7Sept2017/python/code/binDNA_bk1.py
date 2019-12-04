#!/usr/bin/env python

def help():
    print """ 
        Date: 7 Sept 2017
        Program to convert binary into DNA and DNA into binary, depending on input options.

        (For text file of binary information to be converted into DNA)
            Usage: binDNA.py bin.txt dna 

        (For text file of DNA information to be converted into binary)
            Usage: binDNA.py dna.txt bin

"""

dnaCode_dic = {"a": "00", "c": "01", "t": "11", "g": "10"}
binCode_dic = {"00":"a", "01":"c", "11":"t", "10":"g"}


def openFile(inFile):

    try: 
        data_str = open(inFile,"r").readline()
        data_str = data_str.replace("\n","")
        return data_str
    except IOError:
        print " Bad file name. Quitting"
        exit()
#end of open()


def makeDNA(in_str):
# method to convert bin into dna
# input: 1010111
# output: atacga

    tmp_str = ""

    print "\n  Input string is the following :",in_str

    if len(in_str) % 2 != 0:
        in_str = in_str + "0"

    for i in range(0, len(in_str), 2): 
#        print i, in_str[i:i+2]
        tmp_str = tmp_str + binCode_dic[in_str[i:i+2]]
    return tmp_str

#end of makeDNA()


def makeBinary(in_str):
# method to convert dna into bin
# input: atagatac
# output: 1010101
    tmp_str = ""
#    print " _____ ",in_str

    print "\n  Input string is the following :",in_str

    for i in in_str:
        tmp_str = tmp_str + dnaCode_dic[i]
    return tmp_str

#end of makeBinary()



def begin(inFile_str,task_str):
# main method of the program. Called by the command-line arguments
    data_str = string.lower(openFile(inFile_str))
    task_str = string.lower(task_str)
    output_str = "none"
#    print "\n  Input string is the following :",data_str

    if task_str == "bin": #we are making a binary sequence from dna
        print "\t+ Preparing a binary sequence from DNA"
        output_str = makeBinary(data_str)

    if task_str == "dna" : # make a dna sequence from binary
        print "\t+ Preparing a DNA sequence from binary"
        output_str = makeDNA(data_str)

    print "\t\tYour sequence is the following:", output_str
    print " \n"

#end of begin()


import string,sys
if __name__ == '__main__':
#       if len(sys.argv) == 2: #one option added to command line
#       begin(sys.argv[1])

    if len(sys.argv) == 3:
         begin(sys.argv[1],sys.argv[2])
    else:
         help()
         sys.exit(0)


