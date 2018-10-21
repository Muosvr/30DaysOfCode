n = int(input())
inputs=[]

for i in range(n):
    number = int(input())
    prime = True
    if number == 1:
        print("Not prime")
    else:
        for i in range(2, int(number**0.5)+1):
            if number%i==0:
                prime = False
        if prime:
            print("Prime")
        else:
            print("Not prime")
