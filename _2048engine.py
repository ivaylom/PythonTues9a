class _2048:
    def __init__(self):
        self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    def addItem(self):
        from functools import reduce
        count = reduce(lambda x,y: x+y, 
            map(lambda l: len(list(filter(lambda x: x==0, l))), self.board))
        if count == 0:
            return None

        import random
        index = random.randint(0, count)
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    if index == 0:
                        self.board[i][j] = 2
                    index-=1

    def moveRow(row, d):
        """row = [0,2,0,4]"""
        """d = [0,1]"""

        for i in range(len(row)):
            for j in range(i+1, len(row)):
                if (d == 0 and row[i] == 0 and row[j] != 0 or
                    d == 1 and row[i] != 0 and row[j] == 0):
                    a = row[i]
                    row[i] = row[j]
                    row[j] = a
    
    def addNumbers(row, d):
        for i in range(3):
            if d == 0 and row[i] == row[i+1]:
                row[i] *= 2
                row[i+1] = 0
            if d == 1 and row[3-i] == row[2-i]:
                row[3-i] *= 2
                row[2-i] = 0

    def move(self, direction):
        """Mesti elementite v posoka i dobavya nov"""
        """direction = [up, down, left, right]"""
        if direction == "Left" or direction == "Right":
            for row in self.board:
                d = 0
                if (direction == "Right"):
                    d = 1
                _2048.moveRow(row, d)
                _2048.addNumbers(row, d)
                _2048.moveRow(row, d)
        elif direction == "Up" or direction == "Down":
            # Homework
            for i in range(4):
                col = list(map(lambda row: row[i], self.board))
                d = 0
                if (direction == "Down"):
                    d = 1
                _2048.moveRow(col, d)
                _2048.addNumbers(col, d)
                _2048.moveRow(col, d)
                list(map(_2048.assign, self.board, col, [i] * 4))
        else: raise "Error"
        self.addItem()
    def assign(row, e, i):
        row[i] = e

    def printBoard(self):
        for row in self.board:
            rowString = ""
            for i in row:
                rowString += "{:5d} ".format(i)
            print(rowString)



    