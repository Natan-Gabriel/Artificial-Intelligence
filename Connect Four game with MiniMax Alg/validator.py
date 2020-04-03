class Validator:
    def __init__(self, gameRepo):
        self.__gameRepo = gameRepo

    def validateLocation(self, board, col):
        '''
        validate a move

        '''
        return board[5][col] == 0 and col >= 0 and col <= 6