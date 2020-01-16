class VehicleClass:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print("vroooooom")

mycar = VehicleClass("porsche","911")
mycar.start_engine()