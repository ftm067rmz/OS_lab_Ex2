print("Please enter the time in seconds :  " )
second = int(input())

hour = int(second/3600)
second = second % 3600
minute = int(second/60)
second = second % 60

print ("Time in H,M,S is : " , hour , ":" , minute , ":" , second)