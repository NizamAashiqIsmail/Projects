import random
No_of_Rounds=int(input("Enter no of round:"))
value=['STONE','PAPER','SCISSOR']
user_score=0;com_score=0
while No_of_Rounds>0:
    user=input("enter your choice:")
    comp=random.choice(value)
    if user in value:
        if user==comp:
            print("Computer = "+user+" So-> DRAW")
        elif user=='STONE' and comp=='PAPER':
            print('Computer = PAPER')
            com_score+=1
        elif user=='STONE' and comp=='SCISSOR':
            print("Computer = SCISSOR")
            user_score+=1
        elif user=='PAPER' and comp=='STONE':
            print("Computer = STONE")
            user_score+=1
        elif user=='PAPER' and comp=='SCISSOR':
            print('Computer = SCISSOR')
            com_score+=1
        elif user=='SCISSOR' and comp=='STONE':
            print('Computer = STONE')
            com_score+=1
        else:
            print('Computer = PAPER')
            user_score+=1
        No_of_Rounds-=1

    else:
        print('\nEnter valid value')
print("\nUser Score = ",user_score)
print("Computer Score = ",com_score)
if user_score>com_score:
    print("\n*** USER WON ***")
else:
    print("\n*** COMPUTER WON ***")
    
            
        
    
    
