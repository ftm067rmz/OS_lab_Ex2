import random

count = 1
userScore = comp1Score = comp2Score =0
print("--- Welcome Game ---\n")

while( 0 < count < 6):
    comp1 = random.randint(1,2)
    comp2 = random.randint(1,2)

    print('Choose : 1-PALAM(✋)  2-PILISH(🤚)')
    user = int(input())

    if user == 1 :
        user_choice = 'PALAM'
    else :
        user_choice = 'PILISH'

#---------------------------------------
    if comp1 == 1:
        comp1_choice = 'PALAM'
    else :
        comp1_choice = 'PILISH'
#---------------------------------------
    if comp2 == 1:
        comp2_choice = 'PALAM'
    else :
        comp2_choice = 'PILISH'
#---------------------------------------

    if comp1_choice == user_choice == comp1_choice:
        print("Similar choice '" , comp1_choice, "'\nPlay again")

    elif (comp1==1 and comp2==1 and user==2) or (comp1==2 and comp2==2 and user==1):
        print("Computers : " , comp1_choice)
        print("User Win")
        userScore += 1
    
    elif (comp1==2 and comp2==1 and user==1) or (comp1==1 and comp2==2 and user==2):
        print( "Computer1 : " , comp1_choice ," Computer2 : " , comp2_choice)
        print("Computer1 Win")
        comp1Score += 1

    elif (comp1==2 and comp2==1 and user==2) or (comp1==1 and comp2==2 and user==1):
        print( "Computer1 : " , comp1_choice ," Computer2 : " , comp2_choice)
        print("Computer2 Win")
        comp2Score += 1

    
    
    count +=1

print("User score : " , userScore)
print("Computer1 score : " , comp1Score)
print("Computer2 score : " , comp2Score)

if userScore == comp1Score == comp2Score:
    print(" No one wins ")

elif userScore>comp1Score and userScore>comp2Score:
    print("User is winner")

elif comp1Score>userScore and comp1Score>comp2Score:
    print("Computer1 is winner")

elif comp2Score>userScore and comp2Score>comp1Score:
    print("Computer2 is winner")