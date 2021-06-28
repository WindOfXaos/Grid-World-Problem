
def getLocation(grid, v):
    index = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == v:
                index.append([i, j])

    if v == 0 or v == 2:
        if len(index) == 0:
            return True
        return index[0]
    else:
        return index


def isEmpty(car, blocks, move):
    if move == "up":
        for block in blocks:
            if (car[0] - 1 == block[0] and
                    car[1] == block[1]):
                return False
        return True

    if move == "down":
        for block in blocks:
            if (car[0] + 1 == block[0] and
                    car[1] == block[1]):
                return False
        return True

    if move == "right":
        for block in blocks:
            if (car[0] == block[0] and
                    car[1] + 1 == block[1]):
                return False
        return True

    if move == "left":
        for block in blocks:
            if (car[0] == block[0] and
                    car[1] - 1 == block[1]):
                return False
        return True
