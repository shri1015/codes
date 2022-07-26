import random 

def guess_num(x):
    random_num = random.randint(1,x)
    guess=0
    while guess!= random_num:
        guess= int(input (f'guess a number between 1 and {x}'))
        if guess < random_num:
            print("num is too low")
        elif guess > random_num:
            print("num is too high")
    else:
        print(f"you guess the correct number {random_num}")
guess_num(10)