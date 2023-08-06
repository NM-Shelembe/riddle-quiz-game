print("****** Welcome to the quiz game ******")
print("         ****** Riddles ****** \n ")

playing = input("Do you want to play?(type yes or no) ")

if playing.lower() != "yes":
    quit()

print("\nLet's begin \n")
score = 0

answer = input("1. What has to be broken before you can use it? ")
if answer.lower() == "egg":
    print("\nWell done, that's correct \n")
    score += 1
else:
    print("Tough luck, that's incorrect \n")

answer = input("2. I am tall when I'm young and short when I'm old, What am I? ")
if answer.lower() == "candle":
    print("\nWell done, that's correct \n")
    score += 1
else:
    print("Tough luck, that's incorrect \n")

answer = input("3. What is full of holes but still hold water? ")
if answer.lower() == "sponge":
    print("\nWell done, that's correct \n")
    score += 1
else:
    print("Tough luck, that's incorrect \n")

answer = input("4. what month of the year has 28 days? ")
if answer.lower() == "all of them":
    print("\nWell done, that's correct \n")
    score += 1
else:
    print("Tough luck, that's incorrect \n")

answer = input("5. What question can you never anser yes to? ")
if answer.lower() == "are you asleep yet":
    print("\nWell done, that's correct \n")
    score += 1
else:
    print("Tough luck, that's incorrect \n")

print("Here is your score: You got " + str(score) + " out of 5")
print("Percentage: " + str((score/4) * 100) + "%" "\n")
