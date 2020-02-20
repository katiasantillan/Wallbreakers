class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for i in board:
            tmp = [x for x in i if x != "."]
            if len(set(tmp)) != len(tmp):
                return False

        for i in range(len(board)):
            tmpSet = set()
            for j in range(len(board)):
                if(board[j][i] != "." and board[j][i]in tmpSet):
                    return False
                else:
                    tmpSet.add(board[j][i])
                    
        for d in range(0, 9, 3):
            for a in range(0, 9, 3):
                tmpA = set()
                for b in range(0+d, 3+d):
                    for c in range(0+a, 3+a):
                        if(board[b][c] != "."):
                            if(board[b][c] in tmpA):
                                return False
                            else:
                                tmpA.add(board[b][c])

        return True
        