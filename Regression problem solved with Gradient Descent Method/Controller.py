class Controller:
	def computeError(self,b0,b1,b2,b3,b4,b5,points):
		totalError = 0
		for i in range (0, len(points)):
			x1 = points[i].x1
			x2 = points[i].x2
			x3 = points[i].x3
			x4 = points[i].x4
			x5 = points[i].x5

			y = points[i].y
			totalError += (y-self.f(b0,b1,x1,b2,x2,b3,x3,b4,x4,b5,x5))**2
		return totalError/ float(len(points))

	def f(self,b0,b1,x1,b2,x2,b3,x3,b4,x4,b5,x5):
		return b0 + b1*x1 + b2*x2 + b3*x3 + b4*x4 + b5*x5

	def iteration(self,b0_current, b1_current,b2_current,b3_current,b4_current,b5_current, points, learning_rate):
		b0_gradient = 0
		b1_gradient = 0
		b2_gradient = 0
		b3_gradient = 0
		b4_gradient = 0
		b5_gradient = 0
		N = float(len(points))
		for i in range(0, len(points)):
			x1 = points[i].x1
			x2 = points[i].x2
			x3 = points[i].x3
			x4 = points[i].x4
			x5 = points[i].x5
			y = points[i].y
			'''
			b0_gradient += -(2/N) * (y - self.f(b0_current,b1_current,x1,b2_current,x2,b3_current,x3,b4_current,x4,b5_current,x5))
			b1_gradient += -(2/N) * x1 *(y - self.f(b0_current,b1_current,x1,b2_current,x2,b3_current,x3,b4_current,x4,b5_current,x5))
			b2_gradient += -(2/N) * x2 * (y - self.f(b0_current, b1_current, x1, b2_current, x2, b3_current, x3, b4_current, x4, b5_current, x5))
			b3_gradient += -(2 / N) * x3 * (y - self.f(b0_current, b1_current, x1, b2_current, x2, b3_current, x3, b4_current, x4, b5_current, x5))
			b4_gradient += -(2 / N) * x4 * (y - self.f(b0_current, b1_current, x1, b2_current, x2, b3_current, x3, b4_current, x4, b5_current, x5))
			b5_gradient += -(2 / N) * x5 * (y - self.f(b0_current, b1_current, x1, b2_current, x2, b3_current, x3, b4_current, x4, b5_current, x5))
			'''
			b0_gradient += -(2 / N) * (y - self.f(b0_current, b1_current, x1, b2_current, x2, b3_current, x3, b4_current, x4, b5_current, x5))
			b1_gradient += -(2 / N) * x1 * (y - self.f(b0_current, b1_current, x1, b2_current, x2, b3_current, x3, b4_current, x4, b5_current, x5))
			b2_gradient += -(2 / N) * x2 * (y - self.f(b0_current, b1_current, x1, b2_current, x2, b3_current, x3, b4_current, x4, b5_current, x5))
			b3_gradient += -(2 / N) * x3 * (y - self.f(b0_current, b1_current, x1, b2_current, x2, b3_current, x3, b4_current, x4,b5_current, x5))
			b4_gradient += -(2 / N) * x4 * (y - self.f(b0_current, b1_current, x1, b2_current, x2, b3_current, x3, b4_current, x4, b5_current, x5))
			b5_gradient += -(2 / N) * x5 * (y - self.f(b0_current, b1_current, x1, b2_current, x2, b3_current, x3, b4_current, x4,b5_current, x5))

		new_b0 = b0_current - (learning_rate * b0_gradient)
		new_b1 = b1_current - (learning_rate * b1_gradient)
		new_b2 = b2_current - (learning_rate * b2_gradient)
		new_b3 = b3_current - (learning_rate * b3_gradient)
		new_b4 = b4_current - (learning_rate * b4_gradient)
		new_b5 = b5_current - (learning_rate * b5_gradient)
		return [new_b0,new_b1,new_b2,new_b3,new_b4,new_b5]

	def gradientDescent(self,points, starting_b0, starting_b1,starting_b2,starting_b3,starting_b4,starting_b5, learning_rate, num_iteartions):
		b0 = starting_b0
		b1 = starting_b1
		b2 = starting_b2
		b3 = starting_b3
		b4 = starting_b4
		b5 = starting_b5

		for i in range(num_iteartions):
			b0,b1, b2, b3, b4, b5 = self.iteration(b0,b1, b2,b3,b4,b5, points, learning_rate)
		return [b0,b1, b2,b3,b4,b5]

