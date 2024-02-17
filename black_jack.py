import random
import time
import os
from black_jack_art import logo
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player_cards = []
player_cards.append(cards[random.randint(0,12)])
computer_cards = []
computer_cards.append(cards[random.randint(0,12)])
computer_score = 0
for i in computer_cards:
    computer_score+=i

def choosing_cards(subject_card):
    subject_score = 0
    while(subject_score<17):
        subject_score = 0
        value =cards[random.randint(0,12)]
        subject_card.append(value)
        if value == 11:
            score =0
            for i in subject_card:
                score+=i
            if(score>21):
                subject_card.remove(11)
                subject_card.append(1)
                score-=10
        for i in subject_card:
                subject_score+=i
    return subject_score

def when_bust(sub_card):
    sub_score =0 
    value =cards[random.randint(0,12)]
    sub_card.append(value)
    for i in sub_card:
        sub_score+=i
    return sub_score
choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n' :") 
time.sleep(0.1)
os.system('clear')
if(choice=="y"):
    print(logo)
    while(choice=="y"):
        print('\n')
        point = cards[random.randint(0,12)]
        if(point == 11):
            player_points = 0
            for i in player_cards:
                player_points+=i
            if(player_points>21):
                player_cards.remove(11)
                player_cards.append(1)
            else:
                player_cards.append(point)
        else:       
            player_cards.append(point)
        player_score =0
        for i in player_cards:
            player_score+=i
        print(f"Your cards :{player_cards}, Current Score {player_score}")
        print(f"Computer's cards :{computer_cards}, Current Score {computer_score}")
        if(player_score==21):
            choice = "n"
            computer_score =when_bust(computer_cards)
            print(f"Your Final Hand : {player_cards}, Final Score = {player_score}")
            print(f"Computer's Final Hand : {computer_cards}, Final Score = {computer_score}")
            print("<<***BLACK JACK***>>\nYou Won.")
        elif(player_score>21):
            choice = "n"
            computer_score =when_bust(computer_cards)
            print(f"Your Final Hand : {player_cards}, Final Score = {player_score}")
            print(f"Computer's Final Hand : {computer_cards}, Final Score = {computer_score}")
            print("You Went Over .You Lose.")
        elif(player_score<=21 and computer_score>21):
            choice = "n"
            print(f"Your Final Hand : {player_cards}, Final Score = {player_score}")
            print(f"Computer's Final Hand : {computer_cards}, Final Score = {computer_score}")
            print("You Won.")
        elif(player_score==computer_score):
            point = cards[random.randint(0,12)]
            if(point == 11):
                player_points = 0
                for i in player_cards:
                    player_points+=i
                if(player_points>21):
                    player_cards.remove(11)
                    player_cards.append(1)
                else:
                    player_cards.append(point)
            else:       
                player_cards.append(point)
        else:
            choice = input("If you want another card type 'y' otherwise type 'n' :")
            if(choice=="n"):
                computer_score =choosing_cards(computer_cards)
                if(computer_score>21):
                    print(f"Your Final Hand : {player_cards}, Final Score = {player_score}")
                    print(f"Computer's Final Hand : {computer_cards}, Final Score = {computer_score}")
                    print("BUST. You Won.")
                elif(computer_score>player_score):
                    print(f"Your Final Hand : {player_cards}, Final Score = {player_score}")
                    print(f"Computer's Final Hand : {computer_cards}, Final Score = {computer_score}")
                    print("You Lose .")
                elif(computer_score==player_score):
                    print(f"Your Final Hand : {player_cards}, Final Score = {player_score}")
                    print(f"Computer's Final Hand : {computer_cards}, Final Score = {computer_score}")
                    print("Draw")
                else:
                    print(f"Your Final Hand : {player_cards}, Final Score = {player_score}")
                    print(f"Computer's Final Hand : {computer_cards}, Final Score = {computer_score}")
                    print("You Won .")
else:
    print("Thank You")



                    
                

            
