from playsound import playsound
from abc import ABC, abstractmethod
# Abstract class for DC machine
class DCMachine(ABC):
    def __init__(self, rated_voltage, rated_current, rated_speed):
        self.rated_voltage = rated_voltage
        self.rated_current = rated_current
        self.rated_speed = rated_speed

    @abstractmethod
    def calculate_efficiency(self, input_voltage, input_current, force , radius ):
        pass

    @abstractmethod
    def calculate_speed(self, input_voltage):
        pass

# Concrete class for DC motor
class DCmotor(DCMachine):
    def __init__(self, rated_voltage, rated_current, rated_speed, armature_resistance, field_resistance):
        super().__init__(rated_voltage, rated_current, rated_speed)
        self.armature_resistance = armature_resistance
        self.field_resistance = field_resistance

    def calculate_efficiency(self, input_voltage, input_current, force , radius ):
        input_power = input_voltage * input_current
        torque = force * radius * 9.81
        print(f"Torque on Motor: {torque:2f}")
        speed = (input_voltage - (self.armature_resistance * input_current)) / 0.23
        output_power = (input_voltage - (self.armature_resistance * input_current)) * input_current
        efficiency = (output_power / input_power) * 100
        return efficiency

    def calculate_speed(self, input_voltage):
        speed = (input_voltage - (self.armature_resistance * input_current)) / 0.23
        return speed
# Concrete class for DC generator
class DCgenerator(DCMachine):
    def __init__(self, rated_voltage, rated_current, rated_speed, armature_resistance, field_resistance):
        super().__init__(rated_voltage, rated_current, rated_speed)
        self.armature_resistance = armature_resistance
        self.field_resistance = field_resistance

    def calculate_efficiency(self, output_voltage, output_current, force , radius ):
        torque = force * radius * 9.81
        speed = (input_voltage - (self.armature_resistance * input_current)) / 0.23
        input_power = (input_voltage - (self.armature_resistance * input_current)) * input_current
        output_power = output_voltage * output_current
        efficiency = (output_power / input_power) * 100
        return efficiency

    def calculate_speed(self, input_voltage):
        speed = (input_voltage - (self.armature_resistance * input_current)) / 0.23
        return speed

# Example 
motor = DCmotor(220, 8.3, 1500, 0.5, 2)
generator = DCgenerator(220, 8.3, 1500, 0.2, 1.5)

#getting input_voltage

while True:
    try:
        input_voltage = float(input("Enter the input voltage: "))
        
        if abs(input_voltage) <= motor.rated_voltage:
            break
        else:
            print("Input voltage is within the acceptable range -",{motor.rated_voltage})

    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")

#for getting input current
while True:
    try:
        input_current= float(input("Enter the input current: "))
        
        if abs(input_current) <= motor.rated_current:
            break
        else:
            print("Input voltage is within the acceptable range -",{motor.rated_current})

    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")
        
        
#getting weight
while True:
    try:
        force = float(input("Enter weight acting on brake drum (in kgs) : "))
        
        if force < 0:
            print("Force should be positive. Try Again")
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")

#getting Radius
while True:
    try:
        radius = float(input("Enter radius of the brake drum in meters: "))
        
        if radius < 0:
            print("Radius should be positive. Try Again")
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")
        
        
#getting output_voltage
while True:
    try:
        output_voltage = float(input("Enter output voltage from Generartor: "))
        
        if output_voltage <= input_voltage:
            break
        else:
            print("Output voltage can't be generated greater than ",{input_voltage})

    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")
        
#getting output_current
while True:
    try:
        output_current = float(input("Enter output current from Generator: "))
        
        if output_current <= input_current:
            break
        else:
            print("output_current can't be generated greater than",{input_current})

    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")

# Calculate and print results for motor
motor_efficiency = motor.calculate_efficiency(input_voltage, input_current, force, radius)
motor_speed = motor.calculate_speed(input_voltage)

print(f"Motor efficiency: {motor_efficiency:.2f}%")
print(f"Motor speed: {motor_speed:.2f} RPM")


if motor_efficiency > 90:
        print("Motor is in good condition and It started perfectly\n")
        sound="C:\\Users\\kalya\\Downloads\\PYTHON PROJECT\\motorgood.mp3"
        playsound(sound)

elif motor_efficiency > 85:
        print("WARNING!!")
        print ("Motor is about to fail and It can be repaired, Started noisy and is about to fail\n")
        sound="C:\\Users\\kalya\\Downloads\\PYTHON PROJECT\\motorepair.mp3"
        playsound(sound)        
else:
    print("IF you use it, It will Blast, Motor is not fit using\n")
    sound="C:\\Users\\kalya\\Downloads\\PYTHON PROJECT\\blast.mp3"
    playsound(sound)   
# Calculate and print results for generator

generator_efficiency = generator.calculate_efficiency(output_voltage, output_current, force, radius)

print(f"Generator efficiency: {generator_efficiency:.2f}%")
print(f"Generator speed: {motor_speed:.2f} RPM")


if generator_efficiency > 90:
        print("Generator is in good condition and It started perfectly")
        sound="C:\\Users\\kalya\\Downloads\\PYTHON PROJECT\\motorgood.mp3"
        playsound(sound)        

elif generator_efficiency > 85: 
        print("WARNING!!")
        print ("Generator is about to fail and It can be repaired, Started noisy and is about to fail")
        sound="C:\\Users\\kalya\\Downloads\\PYTHON PROJECT\\motorepair.mp3"
        playsound(sound)   
        
else:
    print("Generator is not fit using")
    sound="C:\\Users\\kalya\\Downloads\\PYTHON PROJECT\\blast.mp3"
    playsound(sound)   

