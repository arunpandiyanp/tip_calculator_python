#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total_bill_amount = float(input("Total amount of bill amount? "))
no_of_persons = int(input("No of persons will sprint the bill? "))
tip_give = int(input("Amount of Tip? "))
tip_as_percentage = tip_give / 100
total_tip_amount = total_bill_amount * tip_as_percentage
total_bill = total_bill_amount + total_tip_amount
bill_per_person = total_bill / no_of_persons
final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(final_amount)
print(f"Each person should pay: ${final_amount}")
