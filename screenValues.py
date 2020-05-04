from measurement.measures import Distance, Weight

class ScreenValues:

    #Global Variables
    menu = None
    sex = None
    age = None
    serumCreat = None
    weightLb = None
    weightOz = None
    heightFt = None
    heightIn = None
    weightkg = None
    heightCm = None
    
    def __init__(self, values):
        self.menu = values[0]
        self.sex = self.processSex(values[1], values[2])
        self.age = values[3]
        self.serumCreate = values[4]
        self.weightLb = values[5]
        self.weightOz = values[6]
        self.weightKg = self.processWeight()
        self.heightFt = values[7]
        self.heightIn = values[8]
        self.heightCm = self.processHeight()

    def processSex(self, mValue, fValue):
        if mValue is True:
            return "Male"
        if fValue is True:
            return "Female"
        else:
            return False
    
    def processWeight(self):
        return float((Weight(lb = self.weightLb) + Weight(oz = self.weightOz)).kg)

    def processHeight(self):
        return float((Distance(ft = self.heightFt) + Distance(inch = self.heightIn)).cm)