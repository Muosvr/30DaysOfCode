def oddvsEven(input):
    inputArr = list(input)
    oddArr = []
    evenArr = []

    for i in range(len(inputArr)):
        if i % 2 == 0:
            evenArr.append(inputArr[i])
        else:
            oddArr.append(inputArr[i])

    return "".join(evenArr) + " " + "".join(oddArr)

NumCase = input()
wordList = []
for i in range(int(NumCase)):
    word = input()
    wordList.append(word)

for w in wordList:
    print(oddvsEven(w))
