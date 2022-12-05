def checkRotation(string1,string2):
    if len(string1)!=len(string2):
        return False
    string3=string1+string1
    if string2 in string3:
        return True
    else:
        return False

string1="AACD"
string2="ACDA"
print(checkRotation(string1,string2))
