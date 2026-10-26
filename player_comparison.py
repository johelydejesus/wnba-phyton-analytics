player1_points = [18, 10, 12, 14, 14]
player2_points = [17, 16, 11, 6, 11]

total_player1 = sum(player1_points)
total_player2 = sum(player2_points)

player1_average = total_player1/len(player1_points)
print("Player 1 average:", player1_average)

player2_average = total_player2/len(player2_points)
print("Player 2 average:" , player2_average)

if player1_average > player2_average:
    print("Player 1 averaged more points!")
elif player2_average > player1_average:
    print("Player 2 averaged more points!")
else: 
        print("Both players averaged the same amount of points!")
