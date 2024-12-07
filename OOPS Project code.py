from abc import ABC, abstractmethod
import math

class Transformer(ABC):
    def __init__(self):
        self.Vo = float(input("Enter open circuit test input voltage (Vo in volts): "))
        self.IO = float(input("Enter open circuit test input current (IO in amperes): "))
        self.Po = float(input("Enter open circuit test input power (Po in watts): "))
        self.Vsc = float(input("Enter short circuit test input voltage (Vsc in volts): "))
        self.Isc = float(input("Enter short circuit test input current (Isc in amperes): "))
        self.Psc = float(input("Enter short circuit test input power (Psc in watts): "))
        self.irated = float(input("Enter rated current (irated in amperes): "))
        self.vrated = float(input("Enter rated voltage (vrated in volts): "))
        while True:
            self.load_fraction = float(input("Enter fraction of full load (less than 1.25): "))
            if self.load_fraction < 1.25:
                break
            else:
                print("Please enter a value less than 1.25.")
        while True:
            self.power_factor = float(input("Enter load power factor (less than 1): "))
            if self.power_factor < 1:
                break
            else:
                print("Please enter a value less than 1.")
        self.Qrated = float(input("Enter rated load (Qrated in kVA): "))

    @abstractmethod
    def calculate_total_losses(self):
        pass

    def calculate_efficiency(self):
        Pc = self.load_fraction ** 2 * self.Psc
        PL = self.Po + Pc
        Pout = self.load_fraction * self.Qrated * self.power_factor * 1000
        Pin = Pout + PL
        efficiency = (Pout / Pin) * 100
        return Pc, PL, Pout, Pin, efficiency

    def calculate_regulation(self):
        Req = self.Psc / (self.Isc ** 2)
        Zeq = self.Vsc / self.Isc
        Xeq = (Zeq ** 2 - Req ** 2) ** 0.5

        cos_theta = self.power_factor
        sin_theta = (1 - cos_theta ** 2) ** 0.5

        regulation_lagging =  (self.load_fraction)*(self.irated/self.vrated) *(Req * cos_theta + Xeq*sin_theta)*100
        regulation_leading =  (self.load_fraction)*(self.irated/self.vrated) *(Req * cos_theta - Xeq*sin_theta)*100

        return regulation_lagging, regulation_leading

    def calculate(self):
        Pc, PL, Pout, Pin, efficiency = self.calculate_efficiency()
        regulation_lagging, regulation_leading = self.calculate_regulation()

        print(f"Copper Loss at any load (Pc): {Pc:.2f} W")
        print(f"Total Loss (PL): {PL:.2f} W")
        print(f"Output Power (Pout): {Pout:.2f} W")
        print(f"Input Power (Pin): {Pin:.2f} W")
        print(f"Efficiency: {efficiency:.2f}%")
        print(f"Lagging Regulation: +{regulation_lagging:.2f}%")
        print(f"Leading Regulation: -{regulation_leading:.2f}%")

class SpecificTransformer(Transformer):
    def calculate_total_losses(self):
        # Implement this method with your specific calculation logic
        pass

# Calculate and display transformer characteristics
transformer = SpecificTransformer()
transformer.calculate()
