def hashmap(string):
    hm = {}
    for char in string:
        if char in hm:
            hm[char] +=1 
        else:
            hm[char]=1
    chars=[]
    for char in hm:
        if hm[char]>1:
            chars.append(char)
    return chars

string = "abcdabokokok"
print(hashmap(string))
