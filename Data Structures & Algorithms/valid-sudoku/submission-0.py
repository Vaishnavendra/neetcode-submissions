class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        box=defaultdict(set)
        col=defaultdict(set)
        n=len(board)

        for i in range(n):
            for j in range(n):
                if board[i][j]==".":
                    continue
                if(board[i][j] in rows[i] or board[i][j] in col[j] or board[i][j] in box[i//3,j//3]):
                    return False
                rows[i].add(board[i][j])
                col[j].add(board[i][j])
                box[(i//3,j//3)].add(board[i][j])

        return True