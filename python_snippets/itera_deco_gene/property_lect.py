class Temp1():

    def __init__(self, temperature):
        self._temperature = temperature

    def get_temperature(self):
        self.temperature = self._temperature

    def set_temperature(self):
        if self._temperature < 50:
            self.temperature = self._temperature
        else:
            raise Exception("To high temperature")



    def fan_control(self):
        if self.temperature < 20:
            print("Switched off fan")
        else:
            print("Switched ON")

temp1 = Temp1(20)
temp1.temperature = 200
temp1.fan_control()
