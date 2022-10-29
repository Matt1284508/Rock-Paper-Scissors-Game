import ascii_icons
import logic
computer_choice = logic.computer_choice

def user_print():
        if user_choice == 0:
            return(ascii_icons.rock)
        elif user_choice == 1:
            return(ascii_icons.paper)
        elif user_choice == 2:
             return(ascii_icons.scissors)
        else: 
            return('INVALID ENTRY') 
def computer_print():   
        if computer_choice == 0:
            return(ascii_icons.rock)
        elif computer_choice == 1:
            return(ascii_icons.paper)
        elif computer_choice == 2:
            return(ascii_icons.scissors)
        else:
            return('INVALID ENTRY')    
            
 #Prompt User for Play          
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())

#Display user selection as ASCII
print(user_print())

#Display computer selection as ASCII
print('Computer Chose:')
print(computer_print())

if user_choice == 0 and computer_choice == 2:
    print('Rock beats Scissors! You Win!')
elif user_choice == 1 and computer_choice == 0:
    print('Paper beats Rock! You Win!')
elif user_choice == 2 and computer_choice == 1:
    print('Scissors beats Paper! You Win!')
elif user_choice == computer_choice:
    print('Draw')
else: 
    print('You Lose!')
