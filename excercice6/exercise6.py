import random
secret_number= random.randint(1, 100000)
#print (secret_number)
guess =0
number_guesses = 0
while guess !=secret_number:
    guess=int(input("Guess the Number between 1 and 100000 : "))
    number_guesses +=1
    if guess==secret_number:
        print("congratulation!!!! you win!!!!")
        print("number of guesses :", number_guesses)
    elif guess<secret_number:
        print("Higher try again")
    else :
        print("Lower try again")

print("----Task2----")
print()

num1=1
num2=1
for _ in range(50):
    num3=num1+num2
    print(num3)
    num1,num2=num2,num3g
    