n = int(input())
inputs=[]

for i in range(n):
    number = int(input())
    prime = True
    for i in range(2, number):
        if number%i==0:
            prime = False
    if prime:
        print("Prime")
    else:
        print("Not prime")
