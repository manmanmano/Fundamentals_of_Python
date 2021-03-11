#Pell's formula: Pn = 2 * Pn-1 + Pn-2

def pellnums(n):
    if n <= 1:
        return n
    else:
        return(2 * pellnums(n - 1) + pellnums(n - 2))

nterms = int(input("Number of terms to be printed: "))
while nterms < 0:
    print("INVALID INPUT - input must be positive!")
    nterms = int(input("Numbers of terms to be printed: "))
print("Pell sequence:")
for i in range(nterms + 1):
    print(pellnums(i))
