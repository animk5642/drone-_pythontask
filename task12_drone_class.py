class Drone:
  def __init__(self,name):
     self.name = name
     self.battery = 100
     self.status = "grounded"

  def takeoff(self):
    if self.battery>20:
        self.status = "flying"
        print(f"{self.name} is flying")
    else:
       print(f"{self.name} cannot take of low battery")
  def land(self):
     self.status = "grounded"
     print(f"{self.name} has landed")
  def check_battery(self):
     print(f"the battery staus is {self.battery}%")

d1 = Drone("Alpha")
d2 = Drone("Bravo")

d1.check_battery()
d2.check_battery() 

d1.takeoff()
d2.takeoff()
d1.land()

d2.land() 

class Sensor:
  def __init__(self, name):
    self.name = name
    self.readings = []
  def add_reading(self,value):
    self.readings.append(value)

  def get_max(self):
    max = self.readings[0]
    for item in self.readings:
      if item > max:
        max = item
      
   
