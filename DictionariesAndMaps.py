numEntry = int(input())
phoneBook = {}

for i in range(numEntry):
    inputStr = input()
    pair = inputStr.split(" ")
    phoneBook.update({pair[0]:pair[1]})
    
for j in range(numEntry):
    inputStr = input()
    if inputStr in phoneBook:
        print(inputStr + "=" + phoneBook[inputStr])
    else:
        print("Not found")
