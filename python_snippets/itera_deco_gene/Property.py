class Temp1():

    def __init__(self, temperature):
        if temperature <60:
            self.temperature = temperature
        else: raise Exception("Tu mar jayega")

    def fan_control(self):
        if self.temperature < 20:
            print("Switched off fan")
        else:
            print("Switched ON")
'''
t1 = Temp1(30)
t1.temperature = 300
t1.fan_control()
'''
class Temp2:

    def __init__(self, temperature):
        self.temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value<60:
            self._temperature = value
        else:
            raise Exception("Too high temperature")

    #temperature = property(get_temperature, set_temperature)

    def fan_control(self):
        if self._temperature < 20:
            print("Switched off fan")
        else:
            print("Switched ON")

t2 = Temp2(15)
t2.temperature = 155
t2.fan_control()