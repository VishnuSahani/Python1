def lcm(x,y):
    if x>y:
        grt = x
    else:
        grt = y
    while(True):
        if grt % x ==0 and grt % y == 0:
            lcm = grt
            break
        grt = grt+1
    return lcm
n = int(input("Enter the first number to find LCM of Number : "))
m = int(input("Enter the second number to find LCM of Number : "))
print("the L.C.M. of", n ,"amd", m,"is", lcm(n,m))
