## Source: Python the Hardway by Zed A. Shaw
## Date: 09-13-2020

#This prints a string to the console
print("I will now count my chickens: ") 

#This prints the str and executes the expression with order of operations
print("Hens", 25 + 30 / 6)
#Same as above however the modulus is on left-associative with multiplication so that is performed first
print("Roosters", 100 - 25 * 3 % 4)

#the modulus gives us the remainder of 3/4 which in this case is 3
print("What is 3 % 4? " , 3 % 4)
#the modulus of 75 is also 3
print("What is (25 * 3) % 4? " , (25*3)%4)

#console str to inform the user
print("Now I will count the eggs: ")

#this does order of operations with left-association so 
# 4%2 goes first then 1/4 and then addition and subtraction left to right
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

#print str to inform the user
print("Is it true that 3+2 < 5-7?")

#perform the operation proposed in the str above
print(3 + 2 < 5 - 7)

#str with operation present to user as complete thought
print("What is 3 + 2? ", 3 + 2)
#Same as above
print("What is 5 - 7?", 5 - 7)
#str to inform user
print("Oh, that's why it's False.")
#str to inform user
print("How about some more. Let's look at 5 compared to 2!")

#str with expression to compare 5 to 2 with greater than sign
print("Is it greater? ", 5 > 2)
#str says it all here
print("Is it greater or equal? ", 5 >= 2)
#str says it the result is false because 5 is neither less than or equal to 2
print("Is it less or equal? ", 5<=2)