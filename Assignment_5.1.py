initial_amount = input("Please enter the initial amount")
initial_amount = int(initial_amount)
initial_amount0 = initial_amount
interest = input("Please enter interest amount in decimal format")
interest = float(interest)
count = 0
while initial_amount < 2*initial_amount0:
	count +=1 
	initial_amount = (initial_amount*interest) + initial_amount
print("it will take %s years"%count)