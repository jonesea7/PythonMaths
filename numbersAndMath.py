conda deactivate
## Source: Python the Hardway by Zed A. Shaw
## Date: 09-13-2020

import math
import random
from statistics import mean
from decimal import *
from fractions import Fraction

############################# IMPORTED FROM DECIMAL ###########################################

print(f"The decimal version of 7: ", Decimal('7'))

w = 34e5
x = 3.3
y = 4
z = 5j

print(f"The number 34e5 is type: ", type(w))
print(f"The number 3.3 is type: ", type(x))
print(f"The number {4} is type: ", type(y))
print(f"The number 5j is type: ", type(5j))

print(type(complex(y)))
print(type(float(y)))
print(type(int(w)))

################################# SOME METHODS IMPORTED FROM THE MATH MODULE ############################

print(math.ceil(x))
print(math.gcd(math.ceil(x),y))


##################################### IMPORTED FROM RANDOM MODULE ############################

print(random.randrange(1,100))


######################################## IMPORTED FROM STATISTICS ###############################

practiceArray = [1,2,4,2,1]
print(f"The mean of {practiceArray} is: ", mean(practiceArray))



#This prints a string to the console
print("I will now count my chickens: ") 

#This prints the str and executes the expression with order of operations
print("Hens", 25.0 + 30.0 / 6.0)
#Same as above however the modulus is on left-associative with multiplication so that is performed first
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)

#the modulus gives us the remainder of 3/4 which in this case is 3
print("What is 3 % 4? " , 3.0 % 4.0)
#the modulus of 75 is also 3
print("What is (25 * 3) % 4? " , (25.0*3.0)%4.0)

#console str to inform the user
print("Now I will count the eggs: ")

#this does order of operations with left-association so 
# 4%2 goes first then 1/4 and then addition and subtraction left to right
print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

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


#calculate interest over ten years compounding monthly

print("Principle: 15000 Annual Compounding Frequency: 12 Years: 10 Interest: 5%", 15000 * 0.05 * (12 * 10) )
print("The above line is incorrect I did not compound correctly so let's try again.")
print("Using the compound interest formula the answer is: ", 15000*((1 + (0.05/12))**(12*10)))

#grab all of the parameters
principleAmount = 15000
annualCompoundingFrequency = 12
yearsInvested = 10
interestRate = 0.05

#multiple the compounding frequency by the number of years to get the total amount of compounding sessions
compoundingEvents = annualCompoundingFrequency * yearsInvested
print("Total compounding events (12 months x 10 years): ", compoundingEvents)

#set the total sessions to amount of iterations
#for number in compoundingEvents:

#multiply principal by interest
interestPaid = principleAmount*interestRate

print("Find the interest paid for the first month (5 percent of $15,000): ", interestPaid)

#add the product of the principal and interest to the principle
#save the new principle
principleAmount = principleAmount + interestPaid
print("The new principle after one month of interest: ", principleAmount)


#multiply new principle by interest again 
# add the product of the principle and interest to the new principle (repeat 120)

###################################STILL NEED TO LEARN HOW TO 'MANUALLY' DO THE ABOVE ##########################

#using the formula to compound interest with my variables
principleAmount = 15000
print("Using my variables the final principal after ten years is: ", principleAmount*((1 + (interestRate/annualCompoundingFrequency))**(annualCompoundingFrequency*yearsInvested)))


## GET INPUT FROM THE USER NOW AND GET THE INTEREST ###

principalAmount = eval(input("What is your principal investment: "))
interestRate = eval(input("What is your interest rate: "))
annualCompoundingFrequency = eval(input("What is your annual compounding frequency (Weekly = 52, Monthly = 12, Bi-Annually = 2, Annually = 1): "))
#all caps the user input to control the str
#if then to test the input
#assign number to the compoundfrequency variable based on the result 
yearsInvested = eval(input("How many years will you be investing?: "))

#establish the length of the decimal point displayed
getcontext().prec = 2

#this needs an f-string
print(f"You're expected return on {principalAmount} at {interestPaid} compounding {annualCompoundingFrequency} annually for {yearsInvested} is: ", principalAmount*((1 + (interestRate/annualCompoundingFrequency))**(annualCompoundingFrequency*yearsInvested)))

####### PIZZA CALCULATOR #########

# You are ordering one or more pizzas. The sales tax is 8%

#Set input containers
    #Number of pizzas
    #Price of pizza
    #sale tax
    #final order price

#ask for the number of pizzas
#assume the cost is the same for all pizzas $12
#multiply the number of pizzas by the cost
#multiply that number by 0.08
#return the new total cost with sales tax

#Ask the user if what size pizza (this will determine the cost)
#add the cost of the pizza to price
#Ask if they want another pizza (y/n)
#



#place the $15,000 inside a container called money_invested
money_invested = 15000

#place the 5 percent interest rate into a container called interest_rate
interest_rate = 0.05

#place the number of times the pricipal is compounding into 
    #container called annual_compounding_frequency
annual_compounding_frequency = 12

#place 10 inside a container marked years_invested
years_invested = 10

#dust off your algebra book 
    #this thing is heavier than I remember

#find the formula for compound interest
    # Total =  P(1+r/n)^(nt)  

#place all the pieces (money_invested, interest_rate, etc.) inside the compound interest formula 
    # and place the result of a container called investment_with_compounded_interest
investment_with_compounded_interest = (money_invested
                                        * ((1 + (interest_rate/annual_compounding_frequency))
                                        **(interest_rate * years_invested)))

#share the result