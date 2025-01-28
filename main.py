def bubble_short(mylist):
    for i in range(len(mylist)-1):            
        for j in range(len(mylist)-i-1): 
            if mylist[j]>mylist[j+1]:
                a=mylist[j]
                mylist[j]=mylist[j+1]
                mylist[j+1]=a
mylist=[30,20,55,67,12,54,56,68,78,10]
bubble_short(mylist)
print(mylist)



