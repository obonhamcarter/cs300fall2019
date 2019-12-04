#!/usr/bin/env python3

# Written by:
# email:
# Date:

# Library installation notes:
#
#


DATE = "31 July 2019"
VERSION = "i"
AUTHOR = " myName"
AUTHORMAIL = "@allegheny.edu"

# directories
OUTPUT_DIR = "/tmp/0out/" # all results are saved in this local directory
#OUTPUT_DIR = "0out/" # all results are saved in this local directory
INPUT_DIR = "data/"


def help():
        h_str = "   "+DATE+" | version: "+VERSION+" |"+AUTHOR+" | "+AUTHORMAIL
        print("  "+len(h_str) * "-")
        print(h_str)
        print("  "+len(h_str) * "-")

        print("\n\tThe blank-blank program to do something cool.")

        #print("""\n\tLibrary installation notes:""")
        print("\t+ \U0001f600  USAGE: programName <any key to launch>")
        print("\t+ INPUT directory (your data files are here)     : ",INPUT_DIR)
        print("\t+ OUTPUT directory (your output is placed here)  : ",OUTPUT_DIR)

#end of help()


def saveFile(in_str):
# not currently used in this version...
    """Save the string as a text file. Filename is in_str variable."""
    if len(in_str) > 0:
        try:
            tmp_dir = checkDataDir(OUTPUT_DIR)
            fname = "out.md"
            filename = OUTPUT_DIR + fname
            f = open(filename, "w")
            f.write(in_str)
            f.close()
            print(" + Saved file of results in <",filename,"> ")
        except IOError:
            print("  Problem saving file... incorrect permissions?!")
	# end of saveFile()

def printer(inThing):
    """ prints things cleanly. inThing is list or directory"""
    if "list" in str(type(inThing)):
        for i in range( len(inThing) ):
            print("\t",i,":", inThing[i])
    if "dict" in str(type(inThing)):
        counter = 0
        for i in inThing:
            print("\t",counter," |  ",i,":",inThing[i])
            counter += 1
#end of printer()


def checkDataDir(dir_str):
#function to determine whether a data output directory exists.
#if the directory doesnt exist, then it is created

    try:
        os.makedirs(dir_str)
        #print("  PROBLEM: output_dir doesn't exist")
        print("  * Creating :",dir_str)
        return 1

    except OSError:
        return 0
#end of checkDataDir()




def begin(task_str):
    """Driver function of program"""
    print("\n\t Welcome to geneExPy!\n\t A heatmap generator of expression data.")
    #print(" Task :",task_str)

# check the output dir
    tmp_dir = checkDataDir(OUTPUT_DIR)

# check the input dir
    tmp_dir = checkDataDir(INPUT_DIR)


######################################################
#end of begin()



import os, sys
import math
# list other libraries here

#from sklearn.metrics import r2_score
#from sklearn.metrics import mean_squared_error
#import plotly.plotly as py
#import plotly.graph_objs as go
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#import matplotlib.pyplot as plt
#from scipy import stats
#import numpy as np



if __name__ == '__main__':

        if len(sys.argv) == 2: # one parameter at command line
        # note: the number of command line parameters is n + 1
                begin(sys.argv[1])#,sys.argv[2])#,sys.argv[3], sys.argv[4]),sys.argv[5])
        else:
                help()
                sys.exit()
