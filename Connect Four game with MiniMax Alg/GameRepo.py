from copy import deepcopy


class GameRepo1:
    def __init__(self):
        data = []

    def add(self, board, col, player):
        '''
        this function add a player move at a given column from a given board
        '''
        row = self.nextOpenRow(board, col)
        board[row][col] = player

    def AIturn(self, board, curr_player):
        '''
        this function make the best move for the computer after calculating
        the best move,the next open row in that board
        '''
        col = int(self.bestMove(board, curr_player))
        row = self.nextOpenRow(board, col)
        board[row][col] = 2

    def nextOpenRow(self, board, col):
        '''
        this function calculates the next open row for a given board and a given column
        and return it
        '''
        for i in range(6):
            if board[i][col] == 0:
                return i

    def bestMove(self, board, curr_player):
        '''
        this function calculates the best move
        for a given curr_player and a given board
        '''
        if curr_player == 1:
            opp_player = 2
        else:
            opp_player = 1
        boards = {}
        for i in range(7):
            boards[i] = board
        values = {}
        for column in range(7):
            if self.moveIsPossible(boards[i], column):
                table = self.makeMove(boards[i], column, curr_player)
                values[column] = self.search(4, table, opp_player)
        bestMove = 3
        bestAlpha = -10000000

        options = values.items()
        for column, alpha in options:
            if alpha > bestAlpha:
                bestAlpha = alpha
                bestMove = column
        return bestMove

    def search(self, depth, table, curr_player):
        '''
        this function search the value of a given table,
        at a given depth,
        and for a given curr_playe

        '''
        if curr_player == 1:
            opp_player = 2
        else:
            opp_player = 1

        board = {}
        for i in range(7):
            board[i] = table

        possibleMoves = []  # here we will put al the possible moves of curr_player,maximum 7
        for column in range(7):
            if self.moveIsPossible(board[column], column):
                '''
                if a move is possible,we make it,
                and after add it to the possibleMoves lis
                '''
                option = self.makeMove(board[column], column, curr_player)
                possibleMoves.append(option)
        if depth == 0 or len(possibleMoves) == 0 or self.gameOver(table):
            '''
            we call the value function if a cond is satisfied

            '''
            return self.value(table, 2)
        if curr_player % 2 == 1:
            alpha = 100
        else:
            alpha = -100
        for move in possibleMoves:
            # print(alpha)
            if curr_player % 2 == 1:
                alpha = min(alpha, self.search(depth - 1, move, opp_player))
                '''
                if the human is the curr_player the we will calculate the minimum
                between alpha and new search function call because we have to consider
                that the human player makes the best move possible
                '''
            else:
                '''
                if AI is the curr_player the we will calculate the max
                between alpha and new search function call,because we have
                make the best move possible
                '''
                alpha = max(alpha, self.search(depth - 1, move, opp_player))
        # print(alpha)
        return alpha

    def moveIsPossible(self, board, column):
        '''
        if the umost upper element on a given column  is 0,
        then the move is possible
        '''
        if board[5][column] == 0:
            return True
        return False

    def makeMove(self, board, column, curr_player):
        '''
        if a move is possible we will call the makeMove function
        this put the curr_player's element on a given column from a
        given board and returns the new board
        '''
        table = deepcopy(board)
        for i in range(6):
            if table[i][column] == 0:
                table[i][column] = curr_player
                return table

    def gameOver(self, table):
        '''
        if a player has more than 4 element on a column
        or the table is full,then the game is over
        '''
        FullColumn = 0
        if self.streak(table, 1, 4) >= 1 or self.streak(table, 2, 4) >= 1:
            return True
        for column in range(7):
            if table[5][column] != 0:
                FullColumn += 1
        if FullColumn == 7:
            return True
        return False

    def value(self, table, curr_player):
        '''
        this function calculates the value for
        curr_player of a given table
        the most points are won if curr_player wins the game
        the least points are given when curr_player lose the game

        '''
        if curr_player == 1:
            opp_player = 2
        else:
            opp_player = 1
        myTwo = self.streak(table, curr_player, 2)
        myThree = self.streak(table, curr_player, 3)
        myFour = self.streak(table, curr_player, 4)
        myCenter = self.center(table, curr_player)
        myMargins = self.margins(table, curr_player)
        oppTwo = self.streak(table, opp_player, 2)
        oppThree = self.streak(table, opp_player, 3)
        oppFour = self.streak(table, opp_player, 4)
        oppCenter = self.center(table, opp_player)
        return myCenter + myTwo * 10 + myThree * 1000 + myFour * 10000 - -myMargins - oppCenter - oppTwo * 10 - oppThree * 1000 - oppFour * 1000000

    def center(self, table, curr_player):
        '''
        this function help the AI to make central moves
        if two moves have the same value
        '''
        count = 0
        for i in range(6):
            if table[i][3] == curr_player:
                count += 1
        return count

    def margins(self, table, curr_player):
        '''
        this function help the AI not to make marginal
        moves if two moves have the same value
        '''

        count = 0
        for i in range(6):
            if table[i][0] == curr_player:
                count += 1
            if table[i][6] == curr_player:
                count += 1
        return count

    def streak(self, table, player, number):
        '''
        this function check of streaks for a given number
        the final number is the sum between the horizontalStreaks
        verticalStreaks and diagonalStreaks
        '''
        count = 0
        for i in range(6):
            for j in range(7):
                if table[i][j] == player:
                    count += self.horizontalStreak(i, j, table, number)
                    count += self.verticalStreak(i, j, table, number)
                    count += self.diagonalStreak(i, j, table, number)
        return count

    def verticalStreak(self, row, col, table, number):
        '''
        this function return 1 if we have a vertical streak
        of a given number of points and 0 if we don't
        have it
        '''
        count = 0
        for i in range(row, 6):
            if table[i][col] == table[row][col]:
                count += 1
            else:
                break
        if count >= number:
            return 1
        else:
            return 0

    def horizontalStreak(self, row, col, table, number):
        '''
        this function return 1 if we have a horizontalStreak
        of a given number of points and 0 if we don't
        have it
        '''
        count = 0
        for i in range(col, 7):
            if table[row][i] == table[row][col]:
                count += 1
            else:
                break
        if count >= number:
            return 1
        return 0

    def diagonalStreak(self, row, col, table, number):
        '''
        this function return 1 if we have a diagonal streak
        of a given number of points and 0 if we don't
        have it
        we have to check 2 cases of diagonal streaks:
        first from north-west to south-east
        second from south-west to north-east
        '''
        streaks = 0
        count = 0
        a = row
        for i in range(a, 6):
            if row < 1:
                break
            elif table[row][i] == table[row - 1][i + 1]:
                count += 1
            else:
                break
            row -= 1
        if count >= number:
            streaks += 1

        count = 0

        a = row

        for i in range(a, 6):
            if row < 1:
                break
            elif table[row][i] == table[row - 1][i + 1]:
                count += 1
            else:
                break
        if count >= number:
            streaks += 1

        return streaks


def testBoard():
    '''
    a test function for implemented functionalities
    '''
    board = [[0 for x in range(7)] for y in range(6)]
    a = GameRepo1()
    a.add(board, 0, 1)
    a.add(board, 0, 2)
    a.add(board, 1, 1)
    a.add(board, 0, 2)
    a.add(board, 2, 1)
    a.add(board, 1, 2)
    a.add(board, 3, 1)
    a.add(board, 0, 2)
    a.makeMove(board, 4, 1)
    assert a.moveIsPossible(board, 0) == True
    assert a.moveIsPossible(board, 1) == True
    assert a.moveIsPossible(board, 2) == True
    assert a.moveIsPossible(board, 3) == True
    assert a.moveIsPossible(board, 4) == True
    assert a.moveIsPossible(board, 5) == True
    assert a.gameOver(board) == True


testBoard()
