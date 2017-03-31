#!/usr/bin/env python3
'''
Kenneth Adair

To run this program type:
python3 millionaire.py

What does this script do?
This program calculates how much money you'll have for retirement if you work for the federal government as a computer scientist in an area
with the lowest cost of living adjustment such as Utah or another low cost of living area.
This program assumes that if you are starting with the GS scale (GS-7, GS-9, GS-11, GS-12) that you'll stay at each of those
scales for one year each.  After becoming a GS-12 this program assumes you transition to a NH-3 with a salary equal to GS-12 and a raise.
For your pension it calculates it based on your highest three salaries divided by three multiplied by the number of years you worked
for the federal government multipled by the percentage you receive per year of service (1% or 1.1%).

The numbers for this program seem high but keep in mind that with inflation these numbers may not be that unreasonable.
'''

#This import is needed specificially to get e which is 2.718281828459045
import math as m

# Continuously compounded interest formula, A = pe^(rt)
# http://www.mathwarehouse.com/compound-interest/continuously-compounded-interest.php
def calculate_net_worth(principal, rate_of_interest, time_in_years):
    return (principal * (m.exp(rate_of_interest*time_in_years)))

# Since the first few years of a new computer scientist are spent on the GS scale rather
# than the NH scale this calculates how much savings will be accumulated during this early
# phase of the career before being promoted to the NH scale
def calculate_starting_savings_before_nh3(gs, savings_rate, investments_interest_rate):
    # 2017 Salaries grabbed from https://apps.opm.gov/specialrates/2017/table999b01012017.aspx
    gs7 = 47027.0 * savings_rate
    gs9 = 56226.0 * savings_rate
    gs11 = 61748.0 * savings_rate
    # GS 12 Step 1 salary taken from https://www.federalpay.org/gs/2017/utah
    gs12 = 72168.0 * savings_rate

    # Calculate savings generated during this phase of the career
    if gs >= 7:
        my_principal = calculate_net_worth(gs7, investments_interest_rate, 1)
    if gs >= 9:
        my_principal = calculate_net_worth(my_principal + gs9, investments_interest_rate, 1)
    if gs >= 11:
        my_principal = calculate_net_worth(my_principal + gs11, investments_interest_rate, 1)
    if gs >= 12:
        my_principal = calculate_net_worth(my_principal + gs12, investments_interest_rate, 1)

    # Because the FOR loop in calculate_total_retirement() requires to know how many years of remaining
    # federal work remain on the NH scale we calculate how many years to deduct based on how long
    # the federal employee is on the GS scale
    if gs == 7:
        years_deducted = 4
    elif gs == 9:
        years_deducted = 3
    elif gs == 11:
        years_deducted = 2
    else:
        years_deducted = 1

    return years_deducted, my_principal

# Using variables input by the federal employee this calculates the employee's final salary the year before retirement,
# their total TSP, and the amount of money they'll receive annually from their pension.
def calculate_total_retirement(my_principal, savings_rate, years_of_work, years_deducted, investments_interest_rate, raises):
    # GS 12 Step 1 salary taken from https://www.federalpay.org/gs/2017/utah
    salary = 72168.0

    # The my_principal variable is the amount of money accumulated during the GS phase of federal service
    total_tsp = my_principal

    # For the remaining years of federal service
    # increase the salary by their raise amount,
    # increase the total_tsp by their savings rate times their new salary
    # increase the total_tsp again from the interest gained by investments
    # Repeat this for all years of service on the NH-3 scale
    for i in range(years_of_work - years_deducted + 1):
        salary *= (1.0 + raises)
        total_tsp += salary * savings_rate
        total_tsp = calculate_net_worth(total_tsp, investments_interest_rate, 1)

    # The pension percentage per year of service is 1.1% if you worked over 20 years for the government
    # or 1% if you worked for less than 20 years
    # https://www.opm.gov/retirement-services/fers-information/computation/
    pension_percentage = 0.011 if years_of_work > 20 else 0.01
    # From thes same link above the salary they multiply your final pension percentage by is the average of your highest three salaries
    average_high_three_salary = (salary + (salary / (1.0 + raises)) + ((salary / (1.0 + raises)) / (1.0 + raises))) / 3.0
    # From the same link above your pension is calculated  by multiplying your average high three salaries by your years of work by your pension percentage
    annual_pension = average_high_three_salary * years_of_work * pension_percentage

    return salary, annual_pension, total_tsp

# Prompt the user for their information, perform the math, display how much money they'll have at retirement.
def main():
    print("Are you starting as a GS 7, 9, 11, or 12?")
    print("    For 7 enter '7', for 9 enter '9', for 11 enter '11', for 12 enter '12'")
    gs = int(input())
    print("What % of your paycheck is going into your TSP including government matching?")
    print("    The government provides 1% of your paycheck for free, matches the first 3% you contribute by 100%, and matches an additional 2% by 50%")
    print("    This means if you invest the default you contribute 3% and get 4% matching for a total of 7%")
    print("    If you invest 5% the government matches 4% and provides 1% for free for a total of 10%")
    print("    If you invest 15% the government still only provides a max of 5% so your total would only be 20%")
    print("    Due to the limit on TSP/401K of $18,000.00 per year you generally can't go over a total of 25%")
    print("    Enter your contribution as a number, for example 7% is 7, 10% is 10, 20% is 20, etc.")
    savings_rate = float(input()) / 100
    print("How many years until you retire?")
    print("    You must retire at age 62 or greater to not have decreased pension benefits")
    print("    If you retire at age 62 and you're currently 22 years old, enter '40'")
    years_of_work = int(input())
    print("What interest rate do you anticipate receiving on your investments?")
    print("   7% is a suggested default.  The S&P averaged 9.62% per year from 1957 to 2011.")
    print("   Enter your anticipated returns as a number, for example 7% is 7, 9.62% is 9.62, 10% is 10, etc")
    investments_interest_rate = float(input()) / 100
    print("What percentage of raises do you anticipate on your salary once you're a NH3?")
    print("    Note that you receive a 1% cost of living increase every year and the average raise for SMXG is 2% for a total of 3%")
    print("    As a recommended default we recommend 3%.")
    print("    Enter your raises as a number, for example 2% is 2, 3% is 3, 3.5% is 3.5, etc")
    raises = float(input()) / 100.0

    #Perform the math based on user input to see how much money they'll have at retirement.
    years_deducted, my_principal = calculate_starting_savings_before_nh3(gs, savings_rate, investments_interest_rate)
    last_year_salary, annual_pension, total_tsp = calculate_total_retirement(my_principal, savings_rate, years_of_work, years_deducted, investments_interest_rate, raises)

    # Formatted the output to make it easier to read
    print("Last year of work's salary is " + str('${:,.2f}'.format(last_year_salary)))
    print("Your total tsp is: " + str('${:,.2f}'.format(total_tsp)))
    print("Your annual pension is: " + str('${:,.2f}'.format(annual_pension)))

main()