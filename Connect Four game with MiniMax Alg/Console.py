class Console:

    def __UIadd(self, board, parts, player):

        x = int(parts[0])
        self.__gameService.add(board, x, player)

    def AIturn(self, board, player):
        self.__gameService.AIturn(board, player)

    def __init__(self, gameService):
        self.__gameService = gameService
        self.__commands = {"add": self.__UIadd}

    def run(self):
        board = [[0 for x in range(7)] for y in range(6)]  # here we create the board
        while True:
            user = input(">>")
            user = user.strip()
            parts = user.split(" ")  # here we split the parts
            # !!!! for adding a circle on a board on column i use command:add i
            # you are number 1,AI is number 2
            # it will take a while for AI to compute the best move
            if user == "Exit":
                return
            elif parts[0] in self.__commands:
                try:
                    self.__commands[parts[0]](board, parts[1:], 1)  # human being make its move
                    self.AIturn(board, 2)  # AI make its move
                    i = 5
                    while i >= 0:  # print the board in an inverse mode relative to rows
                        print('\n')
                        for j in range(7):
                            print(board[i][j], end=' ')
                        i -= 1
                    print('\n')

                except ValueError:
                    print("Invalid numberical format")
                if self.__gameService.gameOver(board) == True:
                    print("Game over")
                    break
            else:
                print("Invalid command")

