from Point import Point


class Repository:
	def __init__(self,fileName):
		self.fileName=fileName
		self.points=[]
		self.readFile()
	def readFile(self):
		file = open(self.fileName, 'r')
		lines = file.readlines()
		index=0
		for line in lines:
			if index%2==0:
				f_list = [float(i) for i in line.split(" ")]
				self.points.append(Point(float(f_list[0]), float(f_list[1]), float(f_list[2]), float(f_list[3]), float(f_list[4]), float(f_list[5])))
			index+=1
	def getPoints(self):
		return self.points

