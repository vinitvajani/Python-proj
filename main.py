from emoji import emojize

q1 = ["What is the pincode of Malad East?", "A. 400095", "B. 400096", "C. 400097", "D. 400098"]
q2 = ["Who is the current PM of India?", "A. Pappu", "B. Amit Shah", "C. Modi ", "D. Pashu    "]
q3 = ["What catergory of job will you get?", "A. Elite", "B. Super Dream", "C. Dream", "D. Normal"]
q4 = ["Who is Pashu's bestie?", "A. Rishona", "B. Samruddhi", "C. Sakshi", "D. Aastha"]

name = input("Enter your name: ")
print()
print("Welcome to KBC! ", name)
print()

print("Here is your first question: \n")
print(q1[0])
print()
print(f" {q1[1]}            {q1[2]}")
print(f" {q1[3]}            {q1[4]}")
print()

ans1 = input("Enter your answer: ")
print()
if ans1 == "C" or ans1 == "c":
  print(emojize("Congratulations! You've won Rs.1000:partying_face:"))
else:
  print("Sorry, that's the wrong answer. You've won Rs.0")
  exit()
print()

print("Here is your second question: \n")
print(q2[0])
print()
print(f" {q2[1]}             {q2[2]}")
print(f" {q2[3]}             {q2[4]}")
print()

ans2 = input("Enter your answer: ")
print()
if ans2 == "D" or ans2 == "d":
  print(emojize("Congratulations! You've won Rs.10,000:partying_face:"))
else:
  print("Sorry, that's the wrong answer. You've won Rs.1000")
  exit()
print()

print("Here is your Third question: \n")
print(q3[0])
print()
print(f" {q3[1]}             {q3[2]}")
print(f" {q3[3]}             {q3[4]}")
print()

ans3 = input("Enter your answer: ")
print()
if ans3 == "D" or ans3 == "d":
  print(emojize("Congratulations! You've won Rs.100,000:partying_face:"))
else:
  print("Sorry, that's the wrong answer. You've won Rs.10,000")
  exit()
print()

print("Here is your Final question: \n")
print(q4[0])
print()
print(f" {q4[1]}           {q4[2]}")
print(f" {q4[3]}            {q4[4]}")
print()

ans4 = input("Enter your answer: ")
print()
if ans4 == "A" or ans4 == "a":
  print(emojize("Congratulations! You've won GT650:motorcycle:"))
else:
  print("Sorry, that's the wrong answer. You've won Rs.100,000")
  exit()
print()