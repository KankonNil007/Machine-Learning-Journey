import numpy as np
import sys

numStud = int(input("Enter number of students: "))

markStud = np.empty(numStud, dtype=int)

for i in range(0, numStud):
    mark = int(input(f"Enter Marks {i + 1}: "))
    if (mark < 0 or mark > 100):
        print("Invalid Marks!!")
        sys.exit()

    markStud[i] = mark

print(f"\nAverage Marks: {round(np.average(markStud))}")
print(f"Minimum Marks: {np.min(markStud)}")
print(f"Maximum Marks: {np.max(markStud)}")
print(f"Passed Students: {len(markStud[markStud >= 40])} - {markStud[markStud >= 40]}")
print(f"Failed Students: {len(markStud[markStud < 40])} - {markStud[markStud < 40]}")