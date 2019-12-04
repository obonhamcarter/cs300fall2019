print "counting"
import string


s_str = "AAAACCCGGT"


Acount = 0
Tcount = 0
Gcount = 0
Ccount = 0

print "  Your string is:",s_str
s_str = string.lower(s_str)
for i in s_str:
    if i == "a": 
        Acount = Acount + 1
    elif i == "t":
        Tcount = Tcount + 1
    elif i == "c":
        Ccount = Ccount + 1
    elif i == "g":
        Gcount = Gcount + 1
    else:
        print "  Error: unknown character :",i
print " Num of A's =",Acount
print " Num of C's =",Ccount
print " Num of G's =",Gcount
print " Num of T's =",Tcount




print " Or a more simple approach is..."
print " Nums of A's", s_str.count("a")
print " Nums of C's", s_str.count("c")
print " Nums of G's", s_str.count("g")
print " Nums of T's", s_str.count("t")



print "We now find the reverse compliment of a string."
s_str = "AAAACCCGGT"
s_str = string.lower(s_str)
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



# add the compliments by reading through bs_str
comp_str = "" #complimentary string
for i in bs_str:
    print "  bs_str :",i
    if i == "a":
        comp_str = comp_str + "t"
    if i == "t":
        comp_str = comp_str + "a"
    if i == "c":
        comp_str = comp_str + "g"
    if i == "g":
        comp_str = comp_str + "c"

print "  String is           :",s_str 
print "  Backward string     :",bs_str
print "  Compliment string   :",comp_str 


