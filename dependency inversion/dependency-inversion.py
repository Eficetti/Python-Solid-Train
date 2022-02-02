from abc import ABC, abstractmethod

class Switchable(ABC):

    @abstractmethod
    def switch_on(self):
        pass

    @abstractmethod
    def switch_off(self):
        pass

class Appliance(Switchable):

    def __init__(self, name):
        self.name = name
        self.is_on = False

    def switch_on(self):
        print(f"{self.name} is on")

    def switch_off(self):
        print(f"{self.name} is off")

class ElectricSwitch:

    def __init__(self, switchable):
        self.switchable = switchable
        self.is_on = False

    def switch(self):
        if self.is_on:
            self.switchable.switch_off()
            self.is_on = False
        else:
            self.switchable.switch_on()
            self.is_on = True

class Application:

    def create_appliance(self,name):
        appliance = Appliance(name)
        e = ElectricSwitch(appliance)
        e.switch()
        e.switch()

a = Application()
a.create_appliance('TV')
a.create_appliance('Stereo')
