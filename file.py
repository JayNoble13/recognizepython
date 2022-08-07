#declare variables num2, num2, boolean true, and the string "hello world"
num1 = 42
num2 = 2.3
boolean = True
string = 'Hello World'
#variable arrays that include the toppings, the name of the person ordering, and fruit options
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
#using print to output the type of topping and how many 1
print(type(fruit))
print(pizza_toppings[1])
#change pizza toppings variable to mushrooms from the fruit type
pizza_toppings.append('Mushrooms')
#using print to output the variable person, george, his eye color, and to print strawberry
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])
#this is a for loop that will print it's "It's greater" if num1 is less than 45, which it is at 42, else it will print "It's Lower"
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#if the length of the string is less than 5 characters it will print "It's a short word!" else if length is greather than 15 "it's a long word!"
#if the string is between 5 and 15 characters it will print "Just right!"
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#this will print 5, 3, 5, 3, 5, 4 because it will print up to 0, 1, 2, 3, 4 since x=0 to start and adds 1 up to 4 which is < 5 before the next iteration
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1
#the pop will remove the last element and the second element in the array
pizza_toppings.pop()
pizza_toppings.pop(1)
#this will print the name of the person, remove the blue eye color listed previously, and the print the person variable again without the eyecolor
print(person)
person.pop('eye_color')
print(person)
#if the topping is peperoni it will print the item, then list the next with the continue until it hits olives, and it will end the loop witht he break statement
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#defines the function print_hello_ten_times, and for any number between 0-10, print the word hello
def print_hello_ten_times():
    for num in range(10):
        print('Hello')
#this prints hello 10 times
print_hello_ten_times()
#this is telling the function to print x times
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
#this is setting x to be 4 times and will print hello 4 times 0, 1, 2, 3 and break at 4 and not print the 5th number
print_hello_x_times(4)
#this is defnining x as 10, for number in range of 10 print hello
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
#this will print it 10 times and 4 times
print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)