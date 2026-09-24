careers = ["Software Engineer", "Cybersecurity", "Game Developer"]

number = 1

for career in careers:
    
    print(f"{number}. {career}")
    number += 1

addcareer = input("what career do you want to add?")

careers.append(addcareer)
number = 1

for career in careers:
    
    print(f"{number}. {career}")
    number += 1

print(f"You have {len(careers)} careers on your list.")

careersearch = input("What career are you looking for?")

if careersearch in careers:
    print("That career is on your list!")
else:
    print("That career is not on your list.")