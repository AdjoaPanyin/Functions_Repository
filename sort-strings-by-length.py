def sort_strings_by_length(list):
    return sorted(list, key=len)
# This sorts the strings based on their lengths
#This function will sort the strings by their lengths in ascending order. 
#If multiple strings have the same length, their order relative to each other will be preserved.

o= ["abc", "", "aaa", "a", "zz"]
print(sort_strings_by_length(o))
