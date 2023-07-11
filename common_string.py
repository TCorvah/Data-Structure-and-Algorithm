def sameSubstring(string1,string2):
    string1 = list(string1)
    string2 = list(string2)
    sets = set()
    found = False

    for i in string1:
        for j in string2:
            if i  >  j :
                sets.add(j)
            elif j > i:               
                sets.add(i)
            elif i == j:
                found = True
            for c in sets:
                if len(string1) > len(string2) and string2.index(c) >= 0 and string1.index(c):
                   found = True
                else:
                    found = False
            return found
    
    
                  
a = ["hello", "hi", "efkm", "gh"]
b = ["hello", "ok", "dc", "hi"]
comm = sameSubstring(a, b)
print(comm)
