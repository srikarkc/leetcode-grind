candies = [2, 3, 5, 1, 3]
extraCandies = [3]

output = []
highestVal = max(candies)

for i in range(len(candies)):
    if (candies[i] + extraCandies > highestVal):
        output.append(True)
    else:
        output.append(False)
