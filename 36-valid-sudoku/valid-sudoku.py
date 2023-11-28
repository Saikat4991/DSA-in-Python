class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Steps:
        1. initialize rows, cols and subMatrix as dictionary
        2. Check for repetation in the same rows
        3. Check for repetation in the same cols
        4. Check for repetation in the same subMatrix


        '''
        rows = {}
        cols = {}
        subMatrix = {}

        for r in range(9):
            for c in range(9):

                if board[r][c] == '.':
                    continue

                if r not in rows:
                    rows[r] = set()
                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])

                if c not in cols:
                    cols[c] = set()
                if board[r][c] in cols[c]:
                    return False
                cols[c].add(board[r][c])

                subMatrix_key = (r//3, c//3)
                if subMatrix_key not in subMatrix:
                    subMatrix[subMatrix_key]= set()
                if board[r][c] in subMatrix[subMatrix_key]:
                    return False
                subMatrix[subMatrix_key].add(board[r][c])

        return True
        