n = int(input("Enter the first number to find HCF of Number : "))
m = int(input("Enter the second number to find HCF of Number : "))
def find_hcf(x,y):
    if x>y:
        s = y
    else:
        s = x
    for i in range(1 , s+1):
        if x % i== 0 and y % i == 0:
            hcf = i
    return hcf
print("the H.C.F. of", n ,"amd", m,"is", find_hcf(n,m))


