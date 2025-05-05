class Vehicle:
    def move(self):
        print("This vehicle moves in its own way.")


class Car(Vehicle):
    def move(self):
        print("Driving on the road.")


class Plane(Vehicle):
    def move(self):
        print("Flying through the skies. ")


class Boat(Vehicle):
    def move(self):
        print("Sailing across the water. ")


class Bicycle(Vehicle):
    def move(self):
        print("Pedaling along the path. ")


vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()
