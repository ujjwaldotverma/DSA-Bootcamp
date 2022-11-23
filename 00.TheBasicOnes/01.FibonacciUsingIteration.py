n=5
one,two = 1, 1
print(0)
print(1)
for i in range(n):
    tmp = one
    one = one + two
    two = tmp
    print(one)
print()
