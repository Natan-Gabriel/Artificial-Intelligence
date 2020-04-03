from GameRepo import GameRepo1
from validator import Validator
from GameService import GameService
from Console import Console

gameRepo = GameRepo1()
gameValidator=Validator(gameRepo)
gameService=GameService(gameRepo,gameValidator)

console=Console(gameService)
console.run()
