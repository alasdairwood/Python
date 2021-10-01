#birthyear = input("Enter your birth year: ")
#age = 2021 - int(birthyear)
#print("Your age is:", age)

#first = input("First: ")
#second = input("Second: ")
#sum = float(first) + float(second)
#print("Total:" + str(sum))

#first = float(input("First: "))
#second = float(input("Second: "))
#sum = first + second
#print("Total:" + str(sum))

course = 'Python for Beginners'
print(course.replace('for', '4'))

course = 'Python for Beginners'
print('Python' in course)

x = 10 + 3 * 2
print(x)
y = (10 + 3) * 2
print (y)

price = 20
print (price > 10 and price < 30)


temperature = 1

if temperature > 30:
    print("It's a Hot Day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's Cold")
print("Done")


#weight = int(input("Weight: "))
#unit = input("(K)gs or (L)bs: ")
#if unit.upper() == "K":
#    converted = weight / 0.45
#    print("Weight in Lbs: " + str(converted))
#else:
#    converted = weight * 0.45
#    print("Weight in Kgs: " + str(converted))

#While Loop
i = 1

while i <= 10:
    print(i * '*')
    i = i + 1

#Lists
names = ["Alasdair", "Lynne", "Ava", "Kieran", "Freya"]
names[0] = "Al"
print(names[0:3])
print(names)

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)
print(len(numbers))
print(1 in numbers)
numbers.remove(3)
print(numbers)

#For and while Loops

numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

#Range Function

numbers = range(5, 10, 2)
print(numbers)
for number in numbers:
    print(number)

for number in range(5):
    print(number)

#tuples

numbers = (1, 2, 3)
numbers.count(3)
numbers.index
print(numbers)
