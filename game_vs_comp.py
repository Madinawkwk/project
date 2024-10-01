##game vs comp
##1--100%
##2--90%
##3--80%
##...
##9--20%
import random


def success(f):
    pr = 1 - (f - 1) / 10
    return random.random() < pr


def is_valid(f):
    return 1 <= f <= 9


def play():
    hp1, hp2 = 50, 50
    print("Great! Let's get started!") 
    while hp1 >= 0 and hp2 >= 0:
        print('Enter your f strength, 1<=f<=9')
        f = int(input())
        while not is_valid(f):
            print("You can't fool me. Enter your f strength, 1<=f<=9")
            f = int(input())
        
        if success(f):
            hp2 -= f
            print("Congratulations! You've hit the target!")
            print(hp1, '- Your health;', hp2, "- Computer's Health")
            print()
        else:
            print("Alas, you couldn't hit the target!")
            print(hp1, '- Your health;', hp2, "- Computer's Health")
            print()
        if hp2 <= 0:
            print('Congratulations you have won')
            break

        f = random.randint(1, 9)
        print('The power of the computer f is equal to', f)
        if success(f):
            hp1 -= f
            print('The computer hit the target')
            print(hp1, '- Your health;', hp2, "- Computer's Health")
            print()
        else:
            print('The computer missed its target')
            print()
        if hp1 <= 0:
            print('Alas, you have lost')
            break

ans = input('Do you want to play a game? (y=yes, n=no)')
print(ans)
if ans.lower() =='y' or ans.lower() =='н':
    play()
else:
    print('Okay, come back later!')




        
