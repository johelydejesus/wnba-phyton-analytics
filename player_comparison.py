caitlin_points = [18, 10, 12, 14, 14]
sabrina_points = [17, 16, 11, 6, 11]

total_caitlin = sum(caitlin_points)
total_sabrina = sum(sabrina_points)

caitlin_average = total_caitlin/len(caitlin_points)
print("Caitlin average:", caitlin_average)

sabrina_average = total_sabrina/len(sabrina_points)
print("Sabrina average:" , sabrina_average)

if caitlin_average > sabrina_average:
    print("Caitlin averaged more points!")
elif sabrina_average > caitlin_average:
    print("Sabrina averaged more points :(((")
else: 
        print("Both players averaged the same amount of points!")
