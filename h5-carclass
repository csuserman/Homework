class Car:
    def __init__(self, yearModel: int, make: str):
        self.yearModel = yearModel
        self.make = make
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def __str__(self):
        result = f'Car model: {self.make}, yearmodel: {self.yearModel}\n'

        for i in range(5):
            self.accelerate()
            result += f'{self.speed}\n'

        for i in range(5):
            self.brake()
            result += f'{self.speed}\n'

        return result

car = Car(2000, 'Mercedes')
print(car)