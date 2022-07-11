# Salary-Calculator-using-Python
Basic salary calculator using functions in python.
This basic calculator can be used in any retails, workshops, small-scale organizations to determine the total pay an employee's is entitled to including the varible of one working extra time.

The steps inloved in this python program are: -
1) Definig a function. Writng conditional statements and logic under the "computepay" function.
2) Taking user's input like; hours, rate per hour and time rate per hour for overtime work.
3) Calling the function.
4) Displaying the output.

Logic behind this program runs under two conditions: -
1st when the hours worked is less than or equal to 40 hours then the totalpay = rate*hours
2nd whne the hours worked exceed 40 hours then total pay includes two sub-pay: (1) pay1 = rate*hours
                                                                               (2) pay2 = (hours-40)*(rate)*(extrawork times constant)
                                                                               Thus, totalpay = pay1 + pay2
