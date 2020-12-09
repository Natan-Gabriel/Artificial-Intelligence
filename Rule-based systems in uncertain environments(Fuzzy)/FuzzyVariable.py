
class FuzzyVariable:
    #Encapsulate a description of a fuzzy variable
    def __init__(self):
        self.regions = {}#functions for each fuzzy region
        self.inverse = {}

    def addMembershipFunction(self, var_vame, membership_function, inverse=None):
        #Adds a  membership function and an inverse function for Sugeno

        self.regions[var_vame] = membership_function
        self.inverse[var_vame] = inverse

    def fuzzify(self, value):
        #Return the fuzzified values for each region
        return {name: membership_function(value)
                for name, membership_function in self.regions.items()
                }

    def defuzzify(self, var_name, value):
        print("before",value)
        print("after",self.inverse[var_name](value))
        return self.inverse[var_name](value)