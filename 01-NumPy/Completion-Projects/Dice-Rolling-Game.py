import numpy as np

while True:
    rollNum = int(input("Enter Number of Rolls: "))

    if (rollNum > 0):
        break

diceVals = np.random.randint(1, 7, size=(rollNum))
counts = np.bincount(diceVals, minlength=7)
prob = (counts / rollNum) * 100

print("Dice Face - Frequency - Probability\n")

for i in range(1, 7):
    print(f"{i} - {counts[i]} - {prob[i]:.2f}%\n")