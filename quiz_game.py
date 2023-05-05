print("Welcome to Easiest Quiz Game Ever?")

playing = input("Do you want to play a game? Type Yes or No ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :P")
score = 0

answer = input("What comes after 1? ")
if answer == "2": 
    print('Awesome Sauce!')
    score += 1
else:
    print("Wow! Are You OK? ;P")

answer = input("What comes after a? ")
if answer.lower() == "b": 
    print('Awesome Sauce!')
    score += 1
else:
    print("Wow! Are You OK? ;P")

answer = input("What comes before 2? ")
if answer == "1": 
    print('Awesome Sauce!')
    score += 1
else:
    print("Wow! Are You OK? ;P")

answer = input("What comes before b? ")
if answer.lower() == "a": 
    print('Awesome Sauce!')
    score += 1
else:
    print("Wow! Are You OK? ;P")

answer = input("Are we having fun yet? yes / no ")
if answer.lower() == "no": 
    print('Awesome Sauce!')
    score += 1
else:
    print("Wow! Are You OK? ;P")

print("You got " + str(score) + " question correct!")
print("You got " + str((score /5)* 100) + "%.")
