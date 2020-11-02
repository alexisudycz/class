message1 = "Hello"
print(message1)
name = input("What company are you with?")
print("Hi " + name + "!!")
num = int(input("How many feet of fiber optic cable do you need?"))
if num < 100:
  total = num * 0.87
elif num < 500:
  total = num * 0.80
elif num > 499.9:
  total = num * 0.50
total_end = str(total)
print("The total for " + name + " is $" + total_end)
