def add (a,b):
    c = a + b
    print('addition=', c)
def sub ( a , b ):
    c = a - b
    print('Subtration=', c)
def mult (a,b):
    c = a * b
    print('Multiply=', c)
def div (a,b):
    c = a / b
    print('Division=', c)


while True:
    print("option")
    print("Enter A for Addition: ")
    print("Enter S for Subtraction: ")
    print("Enter M for Multipication: ")
    print("Enter D for Division: ")
    print("Enter X for Quit the Program: ")
    user = input( ' :')

    if user == 'x' or user == 'X' :
        break
    elif user =='a' or user == "A":
        x = int(input('Enter the Ist number: '))
        y = int(input('Enter the IInd number: '))
        add(x,y)
    elif user == 's' or user == 'S':
        x = int(input('Enter the Ist number: '))
        y = int(input('Enter the IInd number: '))
        sub(x, y)
    elif user == 'm' or user == 'M':
        x = int(input('Enter the Ist number: '))
        y = int(input('Enter the IInd number: '))
        mult(x, y)
    elif user == 'd' or user == 'D':
        x = int(input('Enter the Ist number: '))
        y = int(input('Enter the IInd number: '))
        div(x, y)




