
print("Welcome to My Quiz Game!\nAn Interesting Game to Play")

player = input("Do you want to play the game? (yes/no): ")

if player.lower().strip() != "yes":
    print("Goodbye!")
    quit()

name_player = input("Enter your name: ")
print(f"Let's start the game, {name_player}! 😊")

score = 0
total_questions = 5

answer = input("What does CPU stand for? ").lower().strip()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Central Processing Unit.")

answer = input("What does GPU stand for? ").lower().strip()
if answer == "graphics processing unit" or answer == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Graphics Processing Unit.")

answer = input("What does RAM stand for? ").lower().strip()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Random Access Memory.")

answer = input("What does ROM stand for? ").lower().strip()
if answer == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Read Only Memory.")

answer = input("Is a mouse an input device or an output device? ").lower().strip()
if answer == "input device":
    print("Correct!")
    score += 1
else:
    print("Wrong! A mouse is an input device.")

percentage = (score / total_questions) * 100

print("\n--- Quiz Results ---")
print(f"Player: {name_player}")
print(f"Correct answers: {score}/{total_questions}")
print(f"Your score: {percentage:.0f}%")

print("Excellent work!" if percentage >= 80 else "Keep practicing!")

