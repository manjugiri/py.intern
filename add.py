#element in list using recursion 
def sum(list):
    if len(list)==0:
        return 0
    return list[0]+sum(list[1:])
#creating list
list=[1,2,3,4,5,6,7,8,9,34,56,]
print(sum(list))