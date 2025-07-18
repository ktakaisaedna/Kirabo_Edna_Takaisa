class Device:
    def power_on(self):
        print("Device powered on")

class NetworkCapable:
    def connect(self):
        print("Network connected")
    
    def power_on(self):
        print("Network interface powered on")

class AudioCapable:
    def play_sound(self):
        print("Playing sound")
    
    def power_on(self):
        print("Audio system powered on")

class SmartPhone(Device, NetworkCapable, AudioCapable):
    def power_on(self):
        print("SmartPhone booting up...")
        super().power_on() 

phone = SmartPhone()
print("\n=== Method Resolution Order Example 1 ===")
print(f"SmartPhone MRO: {SmartPhone.__mro__}")
print("Calling power_on():")
phone.power_on()