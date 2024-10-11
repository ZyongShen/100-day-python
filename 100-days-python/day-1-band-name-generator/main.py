#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end

if __name__=="__main__":
    print('Hello users')

    city = input('What city did you grow up in?\n')
    pet = input('Give a pet name. \n')

    band = (f'{city} {pet}')

    print(f'Band name: {band}')