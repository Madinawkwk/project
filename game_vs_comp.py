import random


def success(f):
    pr = 1 - (f - 1) / 10
    return random.random() < pr


def is_valid(f):
    return 1 <= f <= 9


def opp(hp1, hp2, f):
    if success(f):
        hp1 -= f
        print('The Opponent hit the target')
        print(f"{hp1} - Your health; {hp2} - Opponent's Health")
        print()
    else:
        print('The Opponent missed its target')
        print()
    return hp1

    
def game():
    hp1, hp2 = 50, 50
    print("Great! Let's get started!") 
    while hp1 >= 0 and hp2 >= 0:  
        print('Enter your f strength, 1<=f<=9')
        f = int(input())
        if not is_valid(f):
            print("You can't fool me. Enter your f strength, 1<=f<=9")
            f = int(input())

        if success(f):
            hp2 -= f
            print("Congratulations! You've hit the target!")
            print(f"{hp1} - Your health; {hp2} - Opponent's Health")
            print()
        else:
            print("Alas, you couldn't hit the target!")
            print(f"{hp1} - Your health; {hp2} - Opponent's Health")
            print()
        if hp2 <= 0:
            print('Congratulations you have won')
            break

        if ans.lower() == 'h':
            print('Enter your opp f strength, 1<=f<=9')
            f = int(input())
            if not is_valid(f):
                print("You can't fool me. Enter your opp f strength, 1<=f<=9")
                f = int(input())
            hp1 = opp(hp1, hp2, f)
            if hp1 <= 0:
                print('Alas, you have lost')
                break
            
        elif ans.lower() == 'c':
            f = random.randint(1, 9)
            print('The power of the opp f is equal to', f)
            hp1 = opp(hp1, hp2, f)
            if hp1 <= 0:
                print('Alas, you have lost')
                break            


play = input('Do you want to play a game? (y=yes, n=no)')
if play.lower() =='y' or play.lower() =='н':
    ans = input('Do you want to play against a human or against the computer? (h=vs humam, c=vs comp)')
    game()
else:
    print('Okay, come back later!')





        
