class GameService:
    def __init__(self,gameRepo,validator):
        self.__gameRepo=gameRepo
        self.__validator=validator
    def add(self,board,x,player):
        self.__gameRepo.add(board,x,player)
    def gameOver(self,board):
        return self.__gameRepo.gameOver(board)
    def AIturn(self,board,player):
        self.__gameRepo.AIturn(board,player)