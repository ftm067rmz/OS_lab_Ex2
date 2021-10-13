time = input("Enter the time in 12 hours (hh:mm:ss) :  ")
strTime = time.split(":")

hour = int(strTime[0])
minutes = int(strTime[1])
second =int(strTime[2])

result = hour*3600 + minutes*60 + second
print("Time to seconds : " , result)