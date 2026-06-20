class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        hashMap = defaultdict(list)
        cols = defaultdict(list)
        rows = defaultdict(list)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                currentBoard = (i // 3) * 3 + (j // 3)
                if board[i][j] != ".":
                    if board[i][j] in hashMap[currentBoard] or board[i][j] in cols[j] or board[i][j] in rows[i]:
                        return False

                    cols[j].append(board[i][j])
                    rows[i].append(board[i][j])
                    hashMap[currentBoard].append(board[i][j])

        return True