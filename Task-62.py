class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self, time):
        print(f"{self.name} пройдет путь в {self.speed * time} м за {time} час(ов)")


class СrawlerRobot(Robot):
    def __init__(self, name, speed, territory):
        super().__init__(name, speed)
        self.territory = territory


class WheelsRobot(Robot):
    def __init__(self, name, speed, car_brand):
        super().__init__(name, speed)
        self.car_brand = car_brand


robot1 = Robot("Робот 1", 10)
robot2 = СrawlerRobot("Гусеничный робот", 5, "Тайга")
robot3 = WheelsRobot("Робот на колесах", 15, "BMW")

robot1.move(1)
robot2.move(2)
robot3.move(3)
