##game vs comp
##1--100%
##2--90%
##3--80%
##...
##9--20%
import random

def uspex(pr1):
    return random.random() < pr1

def uspex(pr2):
    return random.random() < pr2

def is_valid(f1):
    return str(f1).isdigit() and 1<=f1<=9

def play():
    hp1, hp2 = 50, 50
    print ('Отлично! Давайте начнем!') 
    while hp1>=0 and hp2>=0:
        print ('Введите Вашу силу f, 1<=f<=9')
        f1 = int(input())
        while is_valid(f1)!= True:
            print ('Меня не обманешь. Введите Вашу силу f, 1<=f<=9')
            f1 = int(input())
        
        pr1 = (100-10*(f1-1))/100
        if uspex(pr1)==True:
            hp2-=f1
            print ('Поздравляю! Вы попали в цель!')
            print (hp1, '- Ваше здоровье;', hp2, '- Здоровье Вашего противника')
            print ()
        else:
            print ('Увы, Вы не смогли попасть в цель!')
            print (hp1, '- Ваше здоровье;', hp2, '- Здоровье Вашего противника')
            print ()
        if hp2<=0:
            print ('Поздравляю Вы выиграли')
            break

        f2 = random.randint(1, 9)
        print ('Сила компьтера f равна', f2)
        pr2 = (100-10*(f2-1))/100
        if uspex(pr2)==True:
            hp1-=f2
            print ('Компьютер попал в цель')
            print (hp1, '- Ваше здоровье;', hp2, '- Здоровье компьютера')
            print ()
        else:
            print ('Компьютер не попал в цель')
            print ()
        if hp1<=0:
            print ('Увы, Вы проиграли')
            break

ans = input('Хотите сыграть в игру? (д=да, н=нет)')
print (ans)
if ans.lower()=='д' or ans.lower()=='l':
    play()
else:
    print ('Хорошо, приходите позже!')




        
