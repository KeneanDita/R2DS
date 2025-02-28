class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1 = Point()
point1.draw()
point1.move()
point1.Name = "Joe"
print(point1.Name)