from playsound import playsound
from abc import ABC, abstractmethod
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

class TransformerBase(ABC):
    def __init__(self):
        self.irated = 4.35  # Updated rated current to 4.35A
        self.vrated = 230   # Default rated voltage set to 230V

    @abstractmethod
    def get_test_values(self):
        pass

class OpenCircuitTransformer(TransformerBase):
    def __init__(self):
        super().__init__()

    def get_test_values(self):
        print("SEE THE OPEN CIRCUIT TEST DIAGRAM GIVE APPROPRIATE VALUES")
        while True:
            try:
                self.Vo = float(input(f"Enter open circuit test input voltage (Vo in volts, <= {self.vrated}): "))
                if 0 <= self.Vo <= self.vrated:
                    break
                else:
                    print(f"Please enter a value between 0 and {self.vrated} for voltage.")
            except ValueError:
                print("Please enter a valid number for voltage.")

        while True:
            try:
                self.IO = float(input(f"Enter open circuit test input current (IO in amperes, <= {self.irated}): "))
                if 0 <= self.IO <= self.irated:
                    break
                else:
                    print(f"Please enter a value between 0 and {self.irated} for current.")
            except ValueError:
                print("Please enter a valid number for current.")

        while True:
            try:
                self.Po = float(input("Enter open circuit test input power (Po in watts): "))
                break
            except ValueError:
                print("Please enter a valid number for power.")
   
        # Input values for load characteristics
        while True:
            try:
                self.load_fraction = float(input("Enter fraction of full load (less than or equal to 1.25): "))
                if 0 <= self.load_fraction <= 1.25:
                    break
                else:
                    print("Please enter a value between 0 and 1.25 for load factor.")
            except ValueError:
                print("Please enter a valid number for load factor.")

        while True:
            try:
                self.power_factor = float(input("Enter load power factor (less than or equal to 1): "))
                if 0 <= self.power_factor <= 1:
                    break
                else:
                    print("Please enter a value between 0 and 1 for power factor.")
            except ValueError:
                print("Please enter a valid number for power factor.")

        self.Qrated = 1  # Default rated load set to 1 kVA             

class ShortCircuitTransformer(TransformerBase):
    def get_test_values(self):
        print("SEE THE SHORT CIRCUIT TEST DIAGRAM GIVE APPROPRIATE VALUES")
        image = mpimg.imread("Screenshot 2023-12-18 221940.png")
        plt.imshow(image)
        plt.show()
        
        while True:
            try:
                self.Vsc = float(input(f"Enter short circuit test input voltage (Vsc in volts, <= {self.vrated}): "))
                if 0 <= self.Vsc <= self.vrated:
                    break
                else:
                    print(f"Please enter a value between 0 and {self.vrated} for voltage.")
            except ValueError:
                print("Please enter a valid number for voltage.")

        while True:
            try:
                self.Isc = float(input(f"Enter short circuit test input current (Isc in amperes, <= {self.irated}): "))
                if 0 <= self.Isc <= self.irated:
                    break
                else:
                    print(f"Please enter a value between 0 and {self.irated} for current.")
            except ValueError:
                print("Please enter a valid number for current.")

        while True:
            try:
                self.Psc = float(input("Enter short circuit test input power (Psc in watts): "))
                break
            except ValueError:
                print("Please enter a valid number for power.")


class SpecificTransformer(OpenCircuitTransformer, ShortCircuitTransformer):
    def _init_(self):
        super()._init_()

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

        regulation_lagging = (self.load_fraction) * (self.irated / self.vrated) * (Req * cos_theta + Xeq * sin_theta) * 100
        regulation_leading = (self.load_fraction) * (self.irated / self.vrated) * (Req * cos_theta - Xeq * sin_theta) * 100

        return regulation_lagging, regulation_leading

    def calculate(self):
        Pc, PL, Pout, Pin, efficiency = self.calculate_efficiency()
        regulation_lagging, regulation_leading = self.calculate_regulation()

        # Display computed values with line spaces for better readability
        print(f"\nCopper Loss at any load (Pc): {Pc:.2f} W")
        print(f"Total Loss (PL): {PL:.2f} W")
        print(f"Output Power (Pout): {Pout:.2f} W")
        print(f"Input Power (Pin): {Pin:.2f} W")
        print(f"Lagging Regulation: +{regulation_lagging:.2f}%")
        print(f"Leading Regulation: -{regulation_leading:.2f}%")

        # Check transformer efficiency and regulation for quality assessment
        if efficiency >= 90:
            print(f"Efficiency: {efficiency:.2f}%")
            print("This efficiency level indicates the transformer is operating well, converting input power effectively into output power.")
        else:
            print(f"Efficiency: {efficiency:.2f}%. This efficiency level suggests inefficiencies within the transformer's operation.")
            sound = "C:\\Users\\kalya\\OneDrive\\Desktop\\trans.mp3"
            playsound(sound)

        if abs(regulation_lagging) <= 3 and abs(regulation_leading) <= 3:
            print("This is a good transformer due to low regulation.")
            print("Regulation within ±3% indicates stable performance and voltage regulation within acceptable limits.")
        else:
            print("Regulation is not low enough for this to be considered a good transformer.")
            print("High regulation values might lead to undesirable voltage fluctuations and affect performance.")
            sound = "C:\\Users\\kalya\\OneDrive\\Desktop\\trans.mp3"
            playsound(sound)

# Calculate and display transformer characteristics
transformer = SpecificTransformer()
transformer.get_test_values()
transformer.calculate()