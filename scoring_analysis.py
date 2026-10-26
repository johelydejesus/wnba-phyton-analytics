points = [24, 31, 18, 27, 35]
total = sum(points)

average = total/len(points)
print("Average:", average)

if average >= 25:
    print("Elite scorer")
else:
    print("mid")

highest_score = max(points)
print("Highest score:", highest_score)
