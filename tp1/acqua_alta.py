def max_interval(mesures):
    x = 0
    sum = 0
    start = 0
    for i in range(7):
        sum = sum + mesures[i]

    mean = sum / 6

    while x + 6 < len(mesures)-1:
        sum = sum - mesures[x]
        x = x + 1
        sum = sum + mesures[x+6]
        if mean < sum / 6:
            mean = sum / 6
            start = x

    return start