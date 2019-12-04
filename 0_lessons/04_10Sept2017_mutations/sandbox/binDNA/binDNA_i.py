#!/usr/bin/env python3

def help():

        print("\tDate: 10 Sept 2019")
        print("\tProgram to convert binary into DNA and DNA into binary, depending on input options.")

        print("\n\tFor text file of binary information to be converted into DNA")
        print("\tUsage: binDNA.py bin.txt dna")

        print("\n\tFor text file of DNA information to be converted into binary")
        print("\tUsage: binDNA.py dna.txt bin")

dnaCode_dic = {"a": "00", "c": "01", "t": "11", "g": "10"}
binCode_dic = {"00":"a", "01":"c", "11":"t", "10":"g"}


def openFile(inFile):
    try:
        data_str = open(inFile,"r").readline()
        data_str = data_str.replace("\n","")
        return data_str
    except IOError:
        print("\tBad file name. Quitting")
        exit()
#end of openFile()


def makeDNA(in_str):
# method to convert bin into dna
# input: 1010111
# output: atacga

    tmp_str = ""
    if len(in_str) % 2 != 0:
        in_str = in_str + "0"

    for i in range(0, len(in_str), 2):
        tmp_str = tmp_str + binCode_dic[in_str[i:i+2]]
    return tmp_str
#end of makeDNA()


def makeBinary(in_str):
# method to convert dna into bin
# input: atagatac
# output: 1010101
    tmp_str = ""

    for i in in_str:
        tmp_str = tmp_str + dnaCode_dic[i]
    return tmp_str
#end of makeBinary()



def begin(inFile_str,task_str):
# main method of the program. Called by the command-line arguments
    data_str = openFile(inFile_str).lower()
    task_str = task_str.lower()
    output_str = "none"

    if task_str == "bin": #we are making a binary sequence from dna
        print("\t+Preparing a binary sequence from DNA\n")
        print("\n\tInput sequence  :",data_str)
        output_str = makeBinary(data_str)

    if task_str == "dna" : # make a dna sequence from binary
        print("\t+ Preparing a DNA sequence from binary\n")
        print("\n\tInput sequence  :",data_str)

        output_str = makeDNA(data_str)

    print("\tOutput sequence :", output_str)
    print("\n")
#end of begin()


import string,sys
if __name__ == '__main__':
    if len(sys.argv) == 3:
         begin(sys.argv[1],sys.argv[2])
    else:
         help()
         sys.exit(0)
