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
      
    return max
  def get_min(self):
    min = self.readings[0]
    for item in self.readings:
      if item < min:
        min = item
    return min

  def get_average(self):
    total_reading = 0
    count = 0
    for item in self.readings:
      count += 1
      total_reading = total_reading + item
    return total_reading/count

s = Sensor("Temperature")
s.add_reading(25)
s.add_reading(30)
s.add_reading(28)
print(s.readings)

print(s.get_max())
print(s.get_min())
print(s.get_average())