from abc import ABC, abstractmethod

# Implementor Interface
class Device(ABC):
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass

    @abstractmethod
    def adjust_volume(self, level):
        pass

# Concrete Implementors
class Television(Device):
    def __init__(self):
        self.is_on = False
        self.volume = 10

    def power_on(self):
        self.is_on = True
        print("Television is now ON.")

    def power_off(self):
        self.is_on = False
        print("Television is now OFF.")

    def adjust_volume(self, level):
        self.volume = level
        print(f"Television volume set to {self.volume}.")

class Radio(Device):
    def __init__(self):
        self.is_on = False
        self.volume = 5

    def power_on(self):
        self.is_on = True
        print("Radio is now ON.")

    def power_off(self):
        self.is_on = False
        print("Radio is now OFF.")

    def adjust_volume(self, level):
        self.volume = level
        print(f"Radio volume set to {self.volume}.")

# Abstraction
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def turn_on(self):
        self.device.power_on()

    def turn_off(self):
        self.device.power_off()

    def set_volume(self, level):
        self.device.adjust_volume(level)

# Refined Abstraction
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self.device.adjust_volume(0)
        print("Device is muted.")

# Client Code
def main():
    tv = Television()
    radio = Radio()

    tv_remote = RemoteControl(tv)
    radio_remote = AdvancedRemoteControl(radio)

    print("-- Testing Television Remote --")
    tv_remote.turn_on()
    tv_remote.set_volume(15)
    tv_remote.turn_off()

    print("\n-- Testing Radio Remote --")
    radio_remote.turn_on()
    radio_remote.set_volume(8)
    radio_remote.mute()
    radio_remote.turn_off()

if __name__ == "__main__":
    main()
