import random

print("--- Welcome Game ✊ ✋ 🤞 ---\n")

userScore = compScore = 0
counter = 1    

while( 0 < counter < 6):
    computer = random.randint(1,3)

    print('Choose : 1-sang✊ , 2-kaghaz✋ , 3-gheychi🤞')
    user = int(input())

    if user == 1 :
        user_choice = 'sang'

    elif user == 2 :
        user_choice = 'kaghaz'

    else :
        user_choice = 'gheychi'

#---------------------------------------
    if computer == 1:
        comp_choice = 'sang'

    elif computer == 2 :
        comp_choice = 'kaghaz'

    else :
        comp_choice = 'gheychi'
#---------------------------------------

    if comp_choice == user_choice:
        print("Similar choice" , comp_choice, "\nPlay again")

    elif (computer == 1 and user == 2) or (computer ==2  and user == 3) or (computer == 3 and user == 1) :
        print("computer choice : " , comp_choice)
        print("User Win")
        userScore += 1
    
    elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1) :
        print("computer choice : " , comp_choice)
        print("Computer Win")
        compScore += 1
    
    counter +=1

print ( "User score is : " , userScore , "&  Computer score is : " , compScore)

if userScore == compScore:
    print(" -- Equal score, No winner --")

elif userScore > compScore:
    print(" -- User is winner --")

else :
    print(" -- Computer is winner --")
