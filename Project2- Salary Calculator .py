#!/usr/bin/env python
# coding: utf-8

# In[4]:


# To determine the total pay of an employee based on worked hours and rate per hour.
# This calculator will be programmed through assignment of a function.

# Definning the function. h: number of hours, r: rate per hour & x: Times rate for extra work.
def computepay(h, r, x): 
    if h > 40:          # Let us assume that work done beyond 40Hrs lead to extra pay of 0.5 times of the rate per hour.
        pay1 = (h-40)*x*r
        pay2 = h*r
        totalpay = pay1 + pay2
        return totalpay
    
# User's Input.
hrs = input("Enter the total number of hours worked by an employee: ")
rph = input("Enter the rate per hour applicable under your organization: ")
xph = input("Enter the times rate per hour applicable for overtime hours ")
fhrs = float(hrs)
frph = float(rph)
fxph = float(xph)

# Calling the function.
P = computepay(fhrs, frph, fxph)
print("Employee's Basic Pay:", P,"Units")


# In[ ]:




