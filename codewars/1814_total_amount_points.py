def points(games):

    points = 0

    for match in games:
        score = match.split(":")
        x = int(score[0])
        y = int(score[1])

        if x > y:
            points += 3
        elif x == y:
            points += 1
        
    return points


print(points(["1:0", "2:0", "3:0", "4:0", "2:1", "3:1", "4:1", "3:2", "4:2", "4:3"]))
