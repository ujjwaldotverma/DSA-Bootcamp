def fibrecursion(n):
   if n <= 1:
       return n
   else:
       return fibrecursion(n-1) + fibrecursion (n-2)

nterms = 10

print("Fibonacci sequence:")
for i in range(nterms):
    print(fibrecursion(i))
