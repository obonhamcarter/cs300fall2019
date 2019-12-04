#!/usr/bin/env python

#*************************************
# CMPSC 300 Spring 2016
# Class Example
# Date: February 9, 2016

# Purpose: illustrating reading files
#*************************************

# Read an input from a fasta file and print out its name and sequence

my_file = open('diabetes.fasta')
firstLine = my_file.readline()
print "This is the first line in your file: ", firstLine
name = firstLine[1:len(firstLine)]# this removes the first char
print "The name is: %s"%name

secondLine = my_file.readline()
print "This is the second line in your file: ", secondLine
print "The sequence is: %s"%secondLine



