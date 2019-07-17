n = int(input("Enter the number : "))
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
a = fact(n)
print("Factorial of",n,"is", a)
