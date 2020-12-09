from FuzzySystem import FuzzySystem


class Controller:
    def __init__(self, temperature, humidity, time, rules):
        self.system = FuzzySystem(rules)
        self.system.addVariable('temperature', temperature)
        self.system.addVariable('humidity', humidity)
        self.system.addVariable('time', time, True)

    def compute(self, inputs):
        return "For humidity: " + str(inputs['humidity']) + \
               " and temperature: " + str(inputs['temperature']) + \
               " the operating time will be: " + str(self.system.defuzzify(inputs))

