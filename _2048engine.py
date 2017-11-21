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


    def move(self, direction):
        """Mesti elementite v posoka i dobavya nov"""
        """direction = [up, down, left, right]"""
        if direction == "left" or direction == "right":
            for row in self.board:
                d = 0
                if (direction == "right"):
                    d = 1
                _2048.moveRow(row, d)
        if direction == "up" or direction == "down":
            # Homework

    