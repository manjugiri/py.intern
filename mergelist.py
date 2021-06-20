def mergeList(listOne, listTwo):
    print("First List ", listOne)
    print("Second List ", listTwo)
    newList = []

    for num in listOne:
 #use if statement to select odd num from the list one
        if (num % 2 != 0):
 #list method:append attach all odd num of listone to newlist  
            newList.append(num)
    for num in listTwo:
        if (num % 2 == 0):
 #list method:append attach all even num of listTwo to newlist           
            newList.append(num)
    return newList 

listOne = [1, 4, 3, 7, 10]
listTwo = [9, 2, 12, 15, 18]

print("New List is", mergeList(listOne, listTwo))