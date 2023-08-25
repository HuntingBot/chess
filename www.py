import random

EMPTY = 0
WROOK, WKNIGHT, WBISHOP, WQUEEN, WKING, WPAWN =    1, 2, 3, 4, 5, 6
BROOK, BKNIGHT, BBISHOP, BQUEEN, BKING, BPAWN =    9,10,11,12,13,14
ROOK, KNIGHT, BISHOP, QUEEN, KING, PAWN = 1, 2, 3, 4, 5, 6
WHITE, BLACK = 0, 8

class Position:
    def __init__(self, board, color=WHITE, ep_square=None, halfmove_clock=0):
        self.board = board
        self.color = color
        self.ep_square = ep_square
        self.halfmove_clock = halfmove_clock
    
    def __str__(self):
        return '\n'.join(map(lambda x: ' '.join(map(lambda y: ".RNBQKP  rnbqkp"[y], x)), self.board))
    
    def to_FEN(self):
        s, cnt, aa = '/'.join(map(lambda x: ''.join(map(lambda y: ".RNBQKP  rnbqkp"[y], x)), self.board)), 0, ""
        for i in s:
            if i != '.':
                aa += str(cnt) if cnt else ""
                cnt = 0
                aa += i
            else:
                cnt += 1
        aa += str(cnt) if cnt else ""
        return aa

    @classmethod
    def from_FEN():
        pass

    def get_all_moves(self):
        color = self.color
        board = self.board
        movelist = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] & 8 != color:
                    continue
                x = board[i][j] & 7
                if x == ROOK or x == QUEEN:
                    for k in range(1, len(board[i])):
                        if 0 <= j + k <= len(board[i]) - 1:
                            if board[i][j+k] != EMPTY and board[i][j+k] & 8 == color:
                                break
                            movelist.append((i, j, i, j+k))
                            if board[i][j+k] != EMPTY:
                                break

                    for k in range(1, len(board[i])):
                        if 0 <= j - k <= len(board[i]) - 1:
                            if board[i][j-k] != EMPTY and board[i][j-k] & 8 == color:
                                break
                            movelist.append((i, j, i, j-k))
                            if board[i][j-k] != EMPTY:
                                break

                    for k in range(1, len(board)):
                        if 0 <= i + k <= len(board) - 1:
                            if board[i+k][j] != EMPTY and board[i+k][j] & 8 == color:
                                break
                            movelist.append((i, j, i+k, j))
                            if board[i+k][j] != EMPTY:
                                break

                    for k in range(1, len(board)):
                        if 0 <= i - k <= len(board) - 1:
                            if board[i-k][j] != EMPTY and board[i-k][j] & 8 == color:
                                break
                            movelist.append((i, j, i-k, j))
                            if board[i-k][j] != EMPTY:
                                break

                if x == BISHOP or x == QUEEN:
                    for k in range(1, len(board[i])):
                        if 0 <= i + k <= len(board) - 1 and 0 <= j + k <= len(board[i]) - 1:
                            if board[i+k][j+k] != EMPTY and board[i+k][j+k] & 8 == color:
                                break
                            movelist.append((i, j, i + k, j + k))
                            if board[i+k][j+k] != EMPTY:
                                break

                    for k in range(1, len(board[i])):
                        if 0 <= i - k <= len(board) - 1 and 0 <= j - k <= len(board[i]) - 1:
                            if board[i-k][j-k] != EMPTY and board[i-k][j-k] & 8 == color:
                                break
                            movelist.append((i, j, i - k, j - k))
                            if board[i-k][j-k] != EMPTY:
                                break

                    for k in range(1, len(board[i])):
                        if 0 <= i + k <= len(board) - 1 and 0 <= j - k <= len(board[i]) - 1:
                            if board[i+k][j-k] != EMPTY and board[i+k][j-k] & 8 == color:
                                break
                            movelist.append((i, j, i + k, j - k))
                            if board[i+k][j-k] != EMPTY:
                                break

                    for k in range(1, len(board[i])):
                        if 0 <= i - k <= len(board) - 1 and 0 <= j + k <= len(board[i]) - 1:
                            if board[i-k][j+k] != EMPTY and board[i-k][j+k] & 8 == color:
                                break
                            movelist.append((i, j, i - k, j + k))
                            if board[i-k][j+k] != EMPTY:
                                break

                if x == KNIGHT:
                    d = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
                    for k in d:
                        if 0 <= i + k[0] <= len(board) - 1 and 0 <= j + k[1] <= len(board[i]) - 1 and (board[i+k[0]][j+k[1]] & 8 != color or board[i+k[0]][j+k[1]] == EMPTY):
                            movelist.append((i, j, i + k[0], j + k[1]))

                if x == KING:
                    d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                    for k in d:
                        if 0 <= i + k[0] <= len(board) - 1 and 0 <= j + k[1] <= len(board[i]) - 1 and (board[i+k[0]][j+k[1]] & 8 != color or board[i+k[0]][j+k[1]] == EMPTY):
                            movelist.append((i, j, i + k[0], j + k[1]))

                if x == PAWN:
                    if color == WHITE:
                        if board[i-1][j] == EMPTY:
                            movelist.append((i, j, i-1, j))
                        if i == 6 and board[i-1][j] == EMPTY and 0 <= i-2 and board[i-2][j] == EMPTY:
                            movelist.append((i, j, i-2, j))
                        if 0 <= j-1 and board[i-1][j-1] != EMPTY and board[i-1][j-1] != EMPTY and board[i-1][j-1] & 8 != color:
                            movelist.append((i, j, i-1, j-1))
                        if j+1 <= len(board[i]) - 1 and board[i-1][j+1] != EMPTY and board[i-1][j+1] != EMPTY and board[i-1][j+1] & 8 != color:
                            movelist.append((i, j, i-1, j+1))
                    if color == BLACK:
                        if board[i+1][j] == EMPTY:
                            movelist.append((i, j, i+1, j))
                        if i == 1 and board[i+1][j] == EMPTY and i+2 <= len(board) - 1 and board[i+2][j] == EMPTY:
                            movelist.append((i, j, i+2, j))
                        if 0 <= j-1 and board[i+1][j-1] != EMPTY and board[i+1][j-1] != EMPTY and board[i+1][j-1] & 8 != color:
                            movelist.append((i, j, i+1, j-1))
                        if j+1 <= len(board[i]) - 1 and board[i+1][j+1] != EMPTY and board[i+1][j+1] != EMPTY and board[i+1][j+1] & 8 != color:
                            movelist.append((i, j, i+1, j+1))
        flag = False
        for i in movelist:
            if board[i[2]][i[3]] != EMPTY:
                flag = True
                break
        if flag:
            aa = []
            for i in movelist:
                if board[i[2]][i[3]] != EMPTY:
                    aa.append(i)
            movelist = aa
        return movelist

    def evaluate(self):
        board = self.board
        color = self.color
        cnt = 0
        for i in board:
            for j in i:
                cnt += (j & 8 != color) * 2 - 1 if j != EMPTY else 0
        return cnt + 0.01 * len(self.get_all_moves())

    def make_move(self, move):
        board = []
        for i in self.board:
            board.append(i[:])
        color = self.color
        x1, y1, x2, y2 = move
        board[x2][y2] = board[x1][y1]
        board[x1][y1] = EMPTY
        return Position(board, 8 - color)

    def search(self, depth):
        if not depth: return self.evaluate()
        maxx = -99
        for i in self.get_all_moves():
            score = -(self.make_move(i).search(depth-1))
            maxx = max(maxx, score)
        return maxx

    def random_move(self):
        return random.choice(self.get_all_moves())
    
    def good_move(self):
        maxx, maxxmove = -999, ()
        for i in self.get_all_moves():
            w = -self.make_move(i).search(3)
            if w > maxx:
                maxx, maxxmove = w, i
        print(w, toNotation(maxxmove))
        return maxxmove

def fromNotation(n, bs=8):
    return (bs - 1 - (ord(n[1]) - ord('1')), ord(n[0]) - ord('a'), bs - 1 - (ord(n[3]) - ord('1')), ord(n[2]) - ord('a'))

def toNotation(n, bs=8):
    return chr(n[1] + ord('a')) + chr(bs - 1 - n[0] + ord('1')) + chr(n[3] + ord('a')) + chr(bs - 1 - n[2] + ord('1')) # 还没写完

initial_position = Position([[BROOK, BKNIGHT, BBISHOP, BQUEEN, BKING, BBISHOP, BKNIGHT, BROOK],
                             [BPAWN, BPAWN, BPAWN, BPAWN, BPAWN, BPAWN, BPAWN, BPAWN],
                             [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                             [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                             [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                             [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                             [WPAWN, WPAWN, WPAWN, WPAWN, WPAWN, WPAWN, WPAWN, WPAWN],
                             [WROOK, WKNIGHT, WBISHOP, WQUEEN, WKING, WBISHOP, WKNIGHT, WROOK]], WHITE)

position = initial_position

while 1:
    print(position)
    position = position.make_move(position.good_move())
    print(position)
    print(list(map(toNotation, position.get_all_moves())))
    position = position.make_move(fromNotation(input()))

"""print(initial_position)

print(initial_position.to_FEN())

print(initial_position.get_all_moves())

print(initial_position.evaluate())

print(fromNotation("e4e5", 8))

print(toNotation((4, 4, 3, 4), 8))

print(list(map(toNotation, initial_position.get_all_moves())))

e3b5 = initial_position.make_move(fromNotation("b7b5"))

print(e3b5)

print(list(map(toNotation, e3b5.get_all_moves())))"""
