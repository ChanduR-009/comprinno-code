for _ in range(int(input())):	#To read the inputs from user
    s=input()		#This stores the input in new variable S	
    d={}		#Creating a set
    for i in s: 		#Traverse through S
        if(i in d):	#if i is present in d then add +1 value to d set
            d[i]+=1 
        else:		#else make the d set value as 1
            d[i]=1 
    l=[] 		#create a new list l 
    for i in d.values():  	#search for i in the set D
        l.append(i) 
    l.sort()		#sort the l list
    if(len(l)<3):  	#if length of l is equal to 3 print dynamic
        print("Dynamic")
    else:		#else check wether the length of l is equal to -1,-2,-3 then print dynamic else print not
        if(l[-1]==l[-2]+l[-3]):
            print("Dynamic")
        else:
            print("Not")
            