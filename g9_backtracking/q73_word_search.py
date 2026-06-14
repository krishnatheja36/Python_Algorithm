"""
Word Search — LeetCode 79 | Backtracking

Logic:
    Try starting a DFS from every cell in the grid. At each step, check bounds,
    character match, and that the cell hasn't been visited in this path (path set).
    Explore all 4 directions recursively. Add cell to path before recursing, remove
    after (backtrack). Return True as soon as i == len(word).

Time:  O(m * n * 4^L) — m*n starting cells, 4^L DFS branches per start (L = word length)
Space: O(L) — path set and recursion depth bounded by word length
"""

class Solution:
    def word_search(self, board: list[list[str]], word: str) -> bool:
        l = len(word)
        rows, cols = len(board), len(board[0])
        path = set()
        # path_list = []

        def dfs(r, c ,i):
            if i == l:
                # print("\n\tWord path =", path_list)
                return True
            if (r < 0 or c <0 or r >=rows or c >=cols or word[i] != board[r][c] or (r,c) in path):
                return False

            path.add((r, c))
            # path_list.append((r,c))
            res = (
                    dfs(r+1, c, i+1) or
                    dfs(r, c+1, i+1) or
                    dfs(r-1, c, i+1) or
                    dfs(r, c-1, i+1)
                   )
            path.remove((r,c))
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False


if __name__ == '__main__':
    S = Solution()
    input = [
             ([['E', 'D', 'X', 'I', 'W'],
              ['P', 'U', 'F', 'M', 'Q'],
              ['I', 'C', 'Q', 'R', 'F'],
              ['M', 'A', 'L', 'C', 'A'],
              ['J', 'T', 'I', 'V', 'E']], "EDUCATIVE"),
              
             ([['E', 'D', 'X', 'I', 'W'],
              ['P', 'A', 'F', 'M', 'Q'],
              ['I', 'C', 'A', 'S', 'F'],
              ['M', 'A', 'L', 'C', 'A'],
              ['J', 'T', 'I', 'V', 'E']], "PACANS"),

              ([['h', 'e', 'c', 'm', 'l'],
              ['w', 'l', 'i', 'e', 'u'],
              ['a', 'r', 'r', 's', 'n'],
              ['s', 'i', 'i', 'o', 'r']], "warrior"),

              ([['C', 'Q', 'N', 'A'],
              ['P', 'S', 'E', 'I'],
              ['Z', 'A', 'P', 'E'],
              ['J', 'V', 'T', 'K']], "SAVE"),

             ([['O', 'Y', 'O', 'I'],
              ['B', 'Y', 'N', 'M'],
              ['K', 'D', 'A', 'R'],
              ['C', 'I', 'M', 'I'],
              ['Z', 'I', 'T', 'O']], "DYNAMIC"),
            ]
    num = 1

    for i in input:
        print(num, ".\tGrid =", sep="")
        for j in range(len(i[0])):
            print("\t\t", i[0][j])
        if i[1] == "":
            print('\n\tWord = ""')
        else:
            print(f"\n\tWord =  {i[1]}")
        search_result = S.word_search(i[0], i[1])
        if search_result:
            print("\n\tSearch result = Word found")
        else:
            print("\n\tSearch result = Word could not be found")
        num += 1
        print("-"*100, "\n")


