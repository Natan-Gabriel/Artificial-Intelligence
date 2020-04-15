#Gradient descent algorithm for linear regression


from numpy import *

from Controller import Controller
from Repository import Repository

class UI:
	def run(self):
		repo=Repository("data.txt")
		ctrl=Controller()
		points = repo.getPoints()

		learning_rate = 0.001
		initial_b0 = 0
		initial_b1 = 0
		initial_b2 = 0
		initial_b3 = 0
		initial_b4 = 0
		initial_b5 = 0

		num_iterations = 2000
		print("Error at start",ctrl.computeError(initial_b0, initial_b1, initial_b2, initial_b3, initial_b4, initial_b5,points))
		[b0,b1,b2,b3,b4,b5] = ctrl.gradientDescent(points, initial_b0,initial_b1,initial_b2,initial_b3,initial_b4,initial_b5, learning_rate, num_iterations)
		print("After",num_iterations,"iterations,the error is: ", ctrl.computeError(b0, b1, b2,b3, b4, b5,points))
		print("The obtained function is:",b0,"+",b1,"*x1 +",b2,"*x2 +",b3,"*x3 +",b4,"*x4 +",b5,"*x5")

ui=UI()
ui.run()