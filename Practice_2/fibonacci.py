nn = int(input("Type in a number: "))
na = 0 
nb = 1 
print("The Fibonacci sequence in the given range is:")
print(na)
print(nb)
for i in range(2, nn):
    fib = na + nb
    na = nb
    nb = fib
    print(fib)
    
    
