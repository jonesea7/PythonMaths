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
                                      *((1 + (interest_rate/annual_compounding_frequency))
                                      **(annual_compounding_frequency * years_invested)))

#share the result
print(f"Your final amount is {investment_with_compounded_interest}!")

