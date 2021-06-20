#def creates function 
def findDivisible(numberList):
    print("Given list is ", numberList)
    print("Divisible of 5 in a list")
    for num in numberList:
        #use if statement. 'num % 5 == 0' selects the number only divisible by 5 from the list.
        if (num % 5 == 0): 
            print(num)
#given list
numList = [10,12, 15,17, 20, 24, 25, 33,35] 
# call function
findDivisible(numList) 
