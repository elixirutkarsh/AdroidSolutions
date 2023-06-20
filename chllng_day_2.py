# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 18:41:27 2023

@author: 91931
"""

# When sorting a list of heterogeneous data types, Python will raise a TypeError because the elements in the list are not directly comparable. To sort such a list, you can use a custom sorting key.

# Here's the corrected code:


L = ["Ram", 1, "Shyam", 2, "Aman", 3]
print(L)
L.sort(key=lambda x: str(x))
print(L)