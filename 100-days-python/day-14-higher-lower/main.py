from art import logo, vs
from game_data import data
import random

if __name__ == "__main__":
    print(logo)
    num_people = len(data)
    idx1 = random.randint(1,num_people)
    person1 = data[idx1]
    modified_data = data[:idx1] + data[idx1+1:]

    num_people -= 1
    idx2 = random.randint(1, num_people)
    person2 = modified_data[idx2]

    print(f"{person1['name']}, a {person1['description']}, from {person1['country']}")
    print(vs)
    print(f"{person2['name']}, a {person2['description']}, from {person2['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ")
    if (guess == 'A'):
        result = person1['follower_count'] > person2['follower_count']
    elif (guess == 'B'):
        result = person2['follower_count'] > person1['follower_count']
    
    if (result):
        print('You win!')
    else:
        print('You lose.')




    
