# valid = True
# while valid:
#     userInput = input("input a number")
#     if userInput[0] == '-':
#         print("negative number")
#     elif userInput == "Quit":
#         valid = False
#     else:
#         print("positive number")

# myList = [1, 2, 3.5, 7, 8.876]


# def myListLoop(mylist):
#     for i in mylist:
#         print(i)


# def myListLoop2(mylist):
#     newList = myList[2:6]
#     for i in newList:
#         print(i)


# def myLooper(myList: list, target: int):
#     for i in range(len(myList)):
#         for j in range(i+1, len(myList)):
#             if myList[i] + myList[j] == target:
#                 print(i, j, myList[i], myList[j])


def getMaxValue(myList):
    maxSum = 0
    bigNum = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] > maxSum:
                maxSum = myList[i] + myList[j]
                bigNum.append(i)
                bigNum.append(j)
    bigNum.reverse()
    return bigNum[0], bigNum[1]


def getThreeSum(myList, target):
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            for k in range(j+1, len(myList)):
                if myList[i] + myList[j] + myList[k] == target:
                    print(myList[i], myList[j], myList[k])
                    return i, j, k
    return "Not Found"


def getMaxValue(myList):
    maxSum = 0

    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] > maxSum:
                maxSum = myList[i] + myList[j]
                pairs = str(i) + " " + str(j)
    return pairs


def containsDuplicate(arr: list) -> bool:
    """
    Checks if A List Contains Duplicate
    """
    ar = []
    for a in arr:
        if a in ar:
            return True
        else:
            ar.append(a)
    return False