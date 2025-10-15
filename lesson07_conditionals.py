import random

# name = input("Enter your name: ").title()

# #b001ean

# if name == "Aarush": print("Welcome, Master")
# else: print("Access Denied")
    
# characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# password = ""
# length = 0

# while length < 8:
#     password = password + characters[random.randint(0, len(characters) - 1)] 
#     length += 1 

# inputpassword = input("Enter password: ")

# if inputpassword == password:
#     print("Correct! How did you know?")
# else:
#     print(f"Ha! Ha! The passsword was {password}") 

# first_name = "Aarush"
# last_name = "Singh"

# if first_name == "Aarush" and last_name == "Singh":
#     print("You are the best!")
# else:
#     print("Hello")

# day = "friday"
# if day == "friday" or day == "saturday": print("Yay!")
# else: print("Eh")





#Challenge 1


print("Even" if int(input("Enter a number: ")) % 2 == 0 else "Odd")

#Challenge 2

print("Access Granted" if input("Enter password: ") == "tree" else "Access Denied")

#Challenge 3

grade = input("Enter grade: ")

if grade >= 90:
    print("A")
elif grade < 90 and grade >= 80:
    print("B")
elif grade < 80 and grade >= 70:
    print("C")
elif grade < 70 and grade >= 60:
    print("D")
else:
    print("F")

