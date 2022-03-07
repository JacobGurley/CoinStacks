# CoinStacks
This algorithm problem was coded using Python.

The algorithm can hold a matrix of any size. 

The way this algorithm works is it takes a matrix, and finds the index of the largest number of each row. Once the index is found, it checks left and right to see if the numbers in the same row are smaller, bigger, or the same.

If the number that is being checked is the same number, then the algorithm keeps checking left/right of that number.

If the number being checked is a smaller number, then we keep checking.

If the number being checked is a bigger number, then the numbers we checked up to this checked number get replaced with the checked number, but not the largest index number we discovered earlier. 

After the algorithm checks the rows, then it checks the columns, using the transpose method, and repeats the steps mentioned above.

The program will loop the steps above until every number to the left/right of the largest number of the row are either the same or are in descending order.

Once the looping is done, then the algorithm takes the newly created matrix and adds up the sum. 

Here is an example problem for this type of algorithm:

Two people are playing King of the Hill with coins in a grid formation. They have labeled the piles with coordinates (i, j) where 0 ≤ i, j < N. Each pile has a height
h(i, j), a nonnegative integer that represents the number of coins in the pile. Aside from the coins in the piles, the two people have an infinite number of spare
coins that they can add to any pile.

The way the game is played is as follows: One person arranges the piles in the shape of a grid with a nonnegative number of coins in each pile as described. The tallest of the piles is going to hold the King of the Hill; that pile will have at least as many coins as any other coin stack in the grid. It is now the other persons' responsibility to add the minimum number of coins to the various piles in the grid so that the following restrictions are respected:

1. For any given row x, assume that the maximum height of a pile in that row occurs in column y. Then the heights of the piles must be decreasing outward from column y in row x. Mathematically, ∀i < j ≤ y, h(x, i) ≤ h(x, j) and ∀i > j ≥ y, h(x, i) ≤ h(x, j).

2. For any given column x, assume that the maximum height of a pile in that column occurs in row y. Then the heights of the piles must be decreasing outward from row y in column x. Mathematically, ∀i < j ≤ y, h(i, x) ≤ h(j, x) and ∀i > j ≥ y, h(i, x) ≤ h(j, x).

The goal of this problem is to determine the minimum number of coins is needed to satisfy the grid restrictions, given a grid of coin heights.

The following is an example of the results for a 5 by 5 grid. The total number
of coins in this case should be 26.

Original matrix: 1 2 5 3 3
2 4 1 5 1
2 1 1 5 2
1 1 5 1 3
4 3 1 5 1


After algorithm runs: 1 2 5 3 3
2 4 5 5 3
2 4 5 5 3
2 4 5 5 3
4 4 4 5 1
