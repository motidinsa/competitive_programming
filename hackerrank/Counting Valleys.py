def countingValleys(steps, path):
    count = 0
    sum = 0
    global initial
    for i in range(steps):
        if i == 0 or sum == 0:
            if path[i] == 'U':
                initial = 'U'
                sum += 1
            else:
                initial = 'D'
                sum -= 1
        elif path[i] == 'U':
            sum += 1
            if sum == 0 and initial == 'D':
                count += 1
        else:
            sum -= 1
    return count


print(countingValleys(14, 'UDDDUDUUDUDUUD'))
