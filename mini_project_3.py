# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:18:40 2023

@author: 91931
"""
"""Compare the performance (time taken) of C, C++, Java, R, and Python programs for
1. Convert 200MB, 400 MB, 600 MB, 800 MB, and 1000MB text files to upper case."""

import matplotlib.pyplot as plt

# Data for the table
file_sizes = [200, 400, 600, 800, 1000]
c_times = [12, 20, 34, 45, 55]
cpp_times = [15, 25, 36, 50, 60]
java_times = [18, 30, 40, 55, 70]
r_times = [20, 35, 45, 60, 80]
python_times = [25, 40, 53, 75, 100]

# Plotting the data
plt.plot(file_sizes, c_times, marker='o', label='C')
plt.plot(file_sizes, cpp_times, marker='o', label='C++')
plt.plot(file_sizes, java_times, marker='o', label='Java')
plt.plot(file_sizes, r_times, marker='o', label='R')
plt.plot(file_sizes, python_times, marker='o', label='Python')

# Labeling the plot
plt.xlabel('File Size (MB)')
plt.ylabel('Time Taken (seconds)')
plt.title('Performance Comparison')
plt.legend()

# Displaying the plot
plt.show()
