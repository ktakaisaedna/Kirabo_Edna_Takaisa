class Vehicle:
    def start(self):
        print("Vehicle starting...")

class Electric:
    def start(self):
        print("Electric motor starting...")
    
    def charge(self):
        print("Charging battery...")

class Autonomous:
    def start(self):
        print("Autonomous systems initializing...")
    
    def self_drive(self):
        print("Self-driving mode activated")

class TeslaModel3(Vehicle, Electric, Autonomous):
    def start(self):
        print("Tesla Model 3 starting sequence:")
        super().start()  

tesla = TeslaModel3()
print(f"Tesla MRO: {TeslaModel3.__mro__}")
print("Calling start():")
tesla.start()
