def anagram_checker(x,y):
    x=x.replace('','').lower()
    y=y.replace('','').lower()
#the above removes spaces and converts to lowercases
    if len(x)!=len(y):
        print(False)
#the above checks if the length of both strings are the same
    if sorted(x) == sorted (y):
        print("Both strings are anagrams of each other")
    else:
        print("not anagrams")

p='cargo andb'
r='gocar nda'
print(anagram_checker(p,r))

l='cargo'
h='gocar'
print(anagram_checker(l,h))

