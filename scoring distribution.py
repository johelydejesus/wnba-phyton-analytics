player_points = [18, 50, 64, 14, 14]
thirty_point_games = 0
twenty_point_games = 0
under_twenty_point_games = 0

for score in player_points:
    if score >= 30:
        thirty_point_games += 1
    elif score >= 20:
        twenty_point_games += 1
    else:
        under_twenty_point_games += 1

print("30+ point games:", thirty_point_games)
print("20-29 point games:", twenty_point_games)
print("Under 20 point games:", under_twenty_point_games)
