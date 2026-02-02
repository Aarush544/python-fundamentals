#1

word = str(input("Enter a number: "))
isPalindrome = True if word[0] == word[-1] else False
print(isPalindrome)

#2

email = input("Enter an email: ")         
print(email[email.find("@") + 1:])

#3

match = True if (["apples", "bannanas", "oranges", "mangoes"])[-1] == input("Enter word: ") else False
print(match)

#4 

string = (input("Enter a word: "))
new = (string + "ly" if string[-3:] == "ing" else string + "ing") if len(string) >= 3 else string
print(new)
    