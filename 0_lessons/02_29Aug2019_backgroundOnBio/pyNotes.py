print "counting"
import string


s_str = "Mississippi"


Mcount = 0
Icount = 0
Scount = 0
Pcount = 0

print "  Your string is:",s_str
s_str = string.lower(s_str)
for i in s_str:
    if i == "i": 
        Icount = Icount + 1
    elif i == "s":
        Scount = Scount + 1
    elif i == "p":
        Pcount = Pcount + 1
    elif i == "m":
        Mcount = Mcount + 1
    else:
        print "  Error: unknown character :",i
print " Num of M's =",Mcount
print " Num of I's =",Icount
print " Num of S's =",Scount
print " Num of P's =",Pcount




print " Or a more simple approach is..."
print " Nums of m's", s_str.count("a")
print " Nums of i's", s_str.count("i")
print " Nums of s's", s_str.count("s")
print " Nums of p's", s_str.count("p")



print "We now find the reverse compliment of a string."
print " Our string is: ",s_str



print " Forward printing"
#print the string char by char
for i in range(len(s_str)):
    print " F: ", i, s_str[i]


# make a new string that is a backward copy of another
bs_str = "" # backward string
print " Reverse printing"
for i in range(len(s_str)):
    print "B: ", len(s_str) - i -1, s_str[len(s_str)-i-1]
    bs_str = bs_str + s_str[len(s_str)-i-1]


# rules
print "\n\nRules:  switch: m <-> i, p <-> s"

# add the compliments by reading through bs_str
comp_str = "" #complimentary string
for i in bs_str:
    print "  bs_str :",i
    if i == "m":
        comp_str = comp_str + "i"
    if i == "i":
        comp_str = comp_str + "m"
    if i == "p":
        comp_str = comp_str + "s"
    if i == "s":
        comp_str = comp_str + "p"

print "  String is           :",s_str 
print "  Backward string     :",bs_str
print "  Compliment string   :",comp_str 

