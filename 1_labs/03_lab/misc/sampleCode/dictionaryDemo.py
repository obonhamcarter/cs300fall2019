seq_str = "ATGCTCGCTAACC" # define your sequence
seq_dict = {} # define a dictionary

for i in seq_str:
   print " Serving char: ",i
   if i not in seq_dict:
     seq_dict[i] = 1
   else:
     seq_dict[i] = seq_dict[i] + 1

print " The contents of the dictionary are the following: ", seq_dict 

