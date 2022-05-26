import random  
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
 
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
        
print("Choose one option: \n 1.Rock. \n 2.Paper. \n 3.Scissors. ")
def main():
    try:
        user_input = int(input("Your choose:"))
        if user_input == 1:
            print("Rock")
            print(rock)
        elif user_input == 2:
            print("Paper!")
            print(paper)
        elif user_input == 3:
            print("Scissors!")
            print(scissors)
        computer_input = int(random.randint(1,3))
        print("______________________________________________")
        print(f'Computer choose')
        if computer_input == 1:
            print("Rock")
            print(rock)
        elif computer_input == 2:
            print("Paper!")
            print(paper)
        elif computer_input == 3:
            print("Scissors!")
            print(scissors)
    except:
        print("______________________________________________")
        print("You had 3 options, you are too dumb for this game...")
        user_input = "Idiot"



    if user_input == "Idiot":
        print("Idiot!")
    elif user_input == computer_input:
        print("Draw!")
    elif (computer_input == 1 and user_input == 3) or (computer_input == 2 and user_input == 1) or (computer_input == 3 and user_input == 2):
        print("Lose!")
    elif (computer_input == 1 and user_input == 2) or (computer_input == 2 and user_input == 3) or (computer_input == 3 and user_input == 1):
        print("Win!")
    else:
        print("You had 3 options, you are too dumb for this game...")
if __name__ == "__main__":
    main()
