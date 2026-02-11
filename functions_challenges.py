# Challenge 1
# 
# PROCEDURE add(a, b):
# {
#   DISPLAY(a + b)
# } 
# PROCEDURE subtract(a, b):
# {
#   DISPLAY(a - b)
# }
# PROCEDURE multiply(a, b):
# {
#   DISPLAY(a * b)
# }
# PROCEDURE divide(a, b):
# {
#   DISPLAY(a / b)
# }

def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def multiply(a, b):
    print(a * b)

def divide(a, b):
    print(a/b)

add(1, 4)
subtract(7, 3)
multiply(7, 6)
divide(15, 3)

# Challenge 2
# 
# PROCEDURE average(num1, num2, num3)
# {
#   sum <- num1 + num2 + num3
#   RETURN (sum/3)
# }
#
# DISPLAY(average(97, 5, 32))


def average(num1, num2, num3):
    sum = num1 + num2 + num3
    return sum / 3

print(average(32, 5, 68))

# Challenge 3
#
# PROCEDURE is_Even(a)
# {
#   IF (a % 2 = 0)
#   {
#       RETURN("Even")
#   }
#   ELSE
#   {
#       RETURN("Odd")
#   }
# }
# 
# DISPLAY(is_Even(5))

def is_Even(a):
    even_or_odd =  "Even" if a % 2 == 0 else "Odd"
    return even_or_odd

print(is_Even(7))


# Challenge 4
#

# PROCEDURE analyzeWord(word)
# {
#     vowelCount <- 0
#     consonantCount <- 0
#     vowels <- ['a', 'e', 'i', 'o', 'u']
#     FOR EACH i in word
#     {
#         IF i in vowels
#         {
#             vowelCount <- vowelCount + 1
#         }
#         ELSE
#         {
#             consonantCount <- consonantCount + 1
#         }
#     }
#     RETURN("Number of vowels: " + vowelCount + ", Number of consonants: " + consonantCount)
# }
# DISPLAY(analyzeWord("hello"))






def analayzeWord(word):
    word = word.lower()
    vowelCount = 0
    consonantCount = 0
    alphabet = "abcdefghijklmnop"
    try:
        for i in word:
            if i in alphabet:
                if i in ('a', 'e', 'i', 'o', 'u'): 
                    vowelCount += 1
                else:
                    consonantCount += 1
        return f"Number of vowels: {vowelCount}, Number of consonants: {consonantCount}"
    except: 
        return "Error! Not a string"
        
print(analayzeWord("helloc123"))