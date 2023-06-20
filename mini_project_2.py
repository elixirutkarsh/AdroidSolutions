# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:12:24 2023

@author: 91931
"""
"""Find all the list of products whose sum-of-price is between 290 and 310.

ProductList = {p1:10, p2:15, p3:20, p4:25, p5:30, p6:35, p7:50}"""
#-------------------------------------------------------------
# Step 1: Library inclusion                             
#-------------------------------------------------------------
import random


#-------------------------------------------------------------
# Step 2: Parameter Setting
#-------------------------------------------------------------
ProductList = {'p1':10, 'p2':15, 'p3':20, 'p4':25, 'p5':30, 'p6':35, 'p7':50,
               'p8':40, 'p9':55, 'p10':60, 'p11':65, 'p12':75, 'p13':70,
               'p14':45}
LB          = 290
UB          = 310
ResultList  = set()   # Store Result List i.e. list of sets whose sum is between 90 and 210.
Iterations  = 1000    # Number of Iterations


#-------------------------------------------------------------
# Step3: Start Program
#-------------------------------------------------------------
for _ in range(Iterations):
    # Select number of elements from Set
    ComboList = random.sample(list(ProductList.keys()), 5)
    ComboSum = sum(ProductList[i] for i in ComboList)

    # Check the Sum Between LB and UB
    if LB <= ComboSum <= UB:
        ResultList.add(tuple(ComboList))


# Print all the sets whose sum is between LB and UB
for r in ResultList:
    print(r)

# Print total sets
print("\nTotal Sets:", len(ResultList), "\n")
