'''Given a binary string str of length N, the task is to find the maximum count of consecutive substrings str can be divided into such that all the substrings are balanced i.e. they have equal number of 0s and 1s. If it is not possible to split str satisfying the conditions then print -1.
'''
def function(string):
    count0=0
    count1=0 
    result=0 
    for i in range(len(string)):
        if string[i]=="0":
            count0 += 1 
        else:
            count1 += 1 
        if count0 == count1:
            result += 1
    if count0 != count1:
        return -1
    return result
    
string = "0100110101"
print(function(string))
