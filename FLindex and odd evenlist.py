def splitevenodd(list): 
   evenlist = [] 
   oddlist = [] 
   for i in list: 
       
      if (i % 2 == 0): 
         evenlist.append(i) 
      else: 
         oddlist.append(i) 
   print("Even lists:", evenlist) 
   print("Odd lists:", oddlist) 
  
list=[1,2,3,4,6,7,8,9,12,34,43,41]
if(list[0] == list[-1]):
    print("Truee")
else:
    print("Flase")
splitevenodd(list) 