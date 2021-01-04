class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year
        self.odometers_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def read_odometers(self):
        """打印一条指出汽车里程的消息"""
        print("this car has "+ str(self.odometers_reading)+" miles on it.")

    def update_odometers(self,mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometers_reading:
            self.odometers_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometers(self,miles):
        """将里程表读数增加指定的量"""
        self.odometers_reading += miles

class Battery():
     """一次模拟电动汽车电瓶的简单尝试"""
     def __init__(self,battery_size = 70):
         """初始化电瓶的属性"""
         self.battery_size = battery_size

     def describe_battery(self):
         """打印一条描述电瓶容量的信息"""
         print("This car has a " + str(self.battery_size) + "-kWh battery.")


     def get_range(self):
         """打印一条消息，指出电瓶的续航里程"""
         if self.battery_size == 70:
            range = 240
         elif self.battery_size == 85:
            range = 270
         message = "This car can go approximately " + str(range)
         message += " miles on a full charge."
         print(message)

class ElectricCar(Car):
    """电动汽车的独到之处"""
    def __init__(self,make,model,year):
        """初始化父类的信息"""
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla','models', "2016")
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()