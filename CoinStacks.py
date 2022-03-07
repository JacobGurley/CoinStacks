# Jacob Gurley
# coinstacks

def solve(grid):
    def firstSum(grid):  # gets sum of matrix
        a = list(map(sum, grid))
        b = sum(a)
        return b

    def zeros(r, c): #makes new matrix, helps with transpose
        grid = []
        while len(grid) < r:
            grid.append([])
            while len(grid[-1]) < c: #-1 is the last row of the grid
                grid[-1].append(0)
        return grid

    def transpose(grid): #turns col into rows
        grid1 = zeros(len(grid[0]), len(grid))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid1[j][i] = grid[i][j]
        return grid1
    a = firstSum(grid)
    bigCoins = 0
    bigDone = False
    while bigDone == False:
        for i in range(len(grid)):
            currentRow = grid[i]
            maxNum = max(currentRow)
            indexMax = currentRow.index(maxNum)
            isDone = False
            iterCoins = 0
            while isDone == False:
                if indexMax == 0:
                    for x in range(indexMax,len(currentRow)-1): #checking right
                        currentElement = grid[i][x]
                        afterElement = grid[i][x+1]
                        if currentElement < afterElement:
                            iterCoins = afterElement - currentElement
                            bigCoins = afterElement - currentElement
                            currentElement = currentElement + (afterElement - currentElement)
                            grid[i][x] = currentElement
                elif indexMax == len(currentRow)-1: #checking left
                    for y in range(indexMax,0 , -1):
                        currentElement = grid[i][y]
                        afterElement = grid[i][y - 1]
                        if currentElement < afterElement:
                            iterCoins = afterElement - currentElement
                            bigCoins = afterElement - currentElement
                            currentElement = currentElement + (afterElement - currentElement)
                            grid[i][y] = currentElement
                elif indexMax != 0 and indexMax != len(currentRow) - 1:
                    for x in range(indexMax,len(currentRow)-1): #checking right
                        currentElement = grid[i][x]
                        afterElement = grid[i][x+1]
                        if currentElement < afterElement:
                            iterCoins = afterElement - currentElement
                            bigCoins = afterElement - currentElement
                            currentElement = currentElement + (afterElement - currentElement)
                            grid[i][x] = currentElement
                    for y in range(indexMax, 0, -1): #checking left
                        currentElement = grid[i][y]
                        afterElement = grid[i][y - 1]
                        if currentElement < afterElement:
                            iterCoins = afterElement - currentElement
                            bigCoins = afterElement - currentElement
                            currentElement = currentElement + (afterElement - currentElement)
                            grid[i][y] = currentElement
                if iterCoins > 0:
                    isDone = False
                elif iterCoins == 0:
                    isDone = True
                iterCoins = 0
        g = transpose(grid)
        for i in range(len(g)):
            currentRow = g[i]
            maxNum = max(currentRow)
            indexMax = currentRow.index(maxNum)
            isDone = False
            iterCoins = 0
            while isDone == False:
                if indexMax == 0:
                    for x in range(indexMax,len(currentRow)-1): #checking right
                        currentElement = g[i][x]
                        afterElement = g[i][x+1]
                        if currentElement < afterElement:
                            iterCoins = afterElement - currentElement
                            bigCoins = afterElement - currentElement
                            currentElement = currentElement + (afterElement - currentElement)
                            g[i][x] = currentElement
                elif indexMax == len(currentRow)-1: #checking left
                    for y in range(indexMax,0 , -1):
                        currentElement = g[i][y]
                        afterElement = g[i][y - 1]
                        if currentElement < afterElement:
                            iterCoins = afterElement - currentElement
                            bigCoins = afterElement - currentElement
                            currentElement = currentElement + (afterElement - currentElement)
                            g[i][y] = currentElement
                elif indexMax != 0 and indexMax != len(currentRow) - 1:
                    for x in range(indexMax,len(currentRow)-1): #checking right
                        currentElement = g[i][x]
                        afterElement = g[i][x+1]
                        if currentElement < afterElement:
                            iterCoins = afterElement - currentElement
                            bigCoins = afterElement - currentElement
                            currentElement = currentElement + (afterElement - currentElement)
                            g[i][x] = currentElement
                    for y in range(indexMax, 0, -1): #checking left
                        currentElement = g[i][y]
                        afterElement = g[i][y - 1]
                        if currentElement < afterElement:
                            iterCoins = afterElement - currentElement
                            bigCoins = afterElement - currentElement
                            currentElement = currentElement + (afterElement - currentElement)
                            g[i][y] = currentElement

                if iterCoins > 0:
                    isDone = False
                elif iterCoins == 0:
                    isDone = True
                iterCoins = 0
        f = transpose(g)
        for i in range(len(grid)):
            grid[i] = f[i]

        if bigCoins > 0:
            bigDone = False
        elif bigCoins == 0:
            bigDone = True
        bigCoins = 0

    b = firstSum(grid)

    return b - a











gride = [[1, 2, 5, 3, 3], [2, 4, 1, 5, 1], [2, 1, 1, 5, 2], [1, 1, 5, 1, 3], [4, 3, 1, 5, 1]]




print(solve(gride))



