numbers = [1,2,3,4,5,6,7,8,9]

print(numbers[1])
print(numbers[0])
print(numbers[-1])

shapes = ["square", "circle", "triangle", 1]

shapes.append("hexagon")
shapes.remove(1)
print(shapes.pop())

empty = []
empty.append("Hello")
print(empty)
print(empty.index("Hello"))

print(max(numbers))
print(min(numbers))
print(sum(numbers))
numbers.sort()

newlist = numbers

print(newlist)
print(numbers)



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]


print(matrix[0][1])


#Challenge 1

# numbers = [1,2,3,4,5,6]
# numbers[2] = input("Enter a number: ")
# print(numbers)

#Challenge 2

shopping = []
items = ["milk", "bread", "eggs"]
shopping += items
shopping.insert(1)

print(shopping)
