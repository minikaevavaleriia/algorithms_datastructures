# мы решали эту задачу на лекции))) можно я не буду расписывать комментарии, а просто защищу, если она попадется ^^
# сложность O(N^2)

class Solution:
    @staticmethod
    def islandPerimeter(grid):
        peri = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i - 1 < 0 or grid[i - 1][j] != 1:
                        peri += 1
                    if i + 1 > len(grid) -1  or grid[i + 1][j] != 1:
                        peri += 1
                    if j - 1 < 0 or grid[i][j - 1] != 1:
                        peri += 1
                    if j + 1 > len(grid[0]) -1  or grid[i][j + 1] != 1:
                        peri += 1

        return peri


def main():
    a = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(Solution.islandPerimeter(a))

main()

