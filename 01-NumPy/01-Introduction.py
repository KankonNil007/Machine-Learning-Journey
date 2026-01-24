import numpy as np 
import time

# We will two methods to perform data tasks

# Method 01: With Basic Python
temperatures = [34.6, 45.7, 37.9, 23.5, 47.8]

startTime = time.perf_counter()

total = 0
for i in temperatures:
    total += i

average = total/len(temperatures)

print(average)
endTime = time.perf_counter()


elapsedTime = endTime - startTime
print(f"Execution Time: {elapsedTime:.5f} Seconds")

# Method 02: Using NumPy

startTime2 = time.perf_counter()

array1 = np.array([34.6, 45.7, 37.9, 23.5, 47.8])
average2 = np.mean(array1)

print(average2)
endTime2 = time.perf_counter()

elapsedTime2 = endTime2 - startTime2
print(f"Execution Time: {elapsedTime2:.5f} Seconds")

# You can clearly See the Time Difference.
# That's why we should use Numpy