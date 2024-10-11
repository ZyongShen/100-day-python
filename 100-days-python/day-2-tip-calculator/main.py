#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

def calculate_tip(bill, num_people, tip_percent):
    tip_percent = tip_percent/100
    tip = (bill/num_people) * (1 + tip_percent)
    tip = round(tip, 2)
    return tip

if __name__ == "__main__":
    bill = float(input('How much is the bill?\n'))
    num_people = float(input('How many people are there?\n'))
    tip_percent = float(input('What percent tip?\n'))
    split = calculate_tip(bill, num_people, tip_percent)
    print("The split is {:0.2f}".format(split))