import art
import game_data
import random
import sys

def get_Account():
    return random.choice(game_data.data)
def format_Account(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def compare(acc1,acc2,guess):
    a_followers=acc1['follower_count']
    b_followers=acc2['follower_count']
    if a_followers>b_followers:
        return guess=='A'
    else:
        return guess=='B'

score=0
game_on=True

print(art.logo)
a=get_Account()
b=get_Account()
while a==b:
    b=get_Account()

while game_on:
    print(f"Compare A: {format_Account(a)}")
    print(art.vs)
    print(f"Against B: {format_Account(b)}")
    guess=input("Who has more followers? Type 'A' or 'B': ")

    iscorrect=compare(a,b,guess)

    if(iscorrect):
        score+=1
        print(f"You're right!Current Score: {score}")
        a=b
        b=get_Account()
        while a==b:
            b=get_Account()
    else:
        print(f"Sorry,that's wrong. Final Score: {score}")
        game_on=False

