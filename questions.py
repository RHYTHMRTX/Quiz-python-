#python quiz game
import os
print("Ladies and lads , welcome to KBC")
print("----------------questions on your screen----------------")
questions = ("Whats the name of the founder Nvidia? : ",
             "What the best pizza's cheese to ever exist? : ",
             "Name of the longest River? : ",
             "Which company has 2 GOTY awards continously in their 2 games created? : ",
             "Will Rhythm00A1 get a job? :  ")
options = (("A. Paramjeet laamba","B. Jessi Pinkman","C. Hamza ali mazari","D. Jensen Huang"),
           ("A. Random Cheese","B. Mozrilla","C. Bhlue cheese","D. Cheddar Cheese"),
           ("A. Ganga","B. Yamuna","C.Ravi","D. Nile"),
           ("A. Ubisoft","B. Bandai namco","C. Fromsoftware","D. NONE"),
           ("A. OFC","B. if he cant then no one ","C. i doubt","D. NOPE"))
answers = ("D","B","D","C","A")
guesses = []
score = 0
questions_num = 0
for question in questions:
    print("-----------------------")
    print(question)
    for option in options[questions_num]:
        print(option)
    print("-----------------------")
    guess = input("Enter the Option (A,B,C,D) : ").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[questions_num]} is the correct one")

    questions_num += 1

print("-----------------------")
print(f"You got {score} out of {len(questions)} correct")
if score == 5:
    os.startfile("7 crore.mp4")
    