n= int(input("Enter any number:"))
if(n ==0 or n == 1):
    print(n,"Number is neither prime nor composite")
elif n>1 :
    for i in range(2,n):
        if(n%i == 0):
            print(n,"is composite number")
            break
    else:
        print(n," is prime number")
else :
    print("Please enter positive number only ")