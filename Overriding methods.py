class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (x, y)
    
    def move(self, x, y):
        self.x += x
        self.y += y
        return (self.x, self.y)

    def __add__(self, p):
        return self.x + p.x, self.y + p.y

    def __sub__(self, p):
        return self.x - p.x, self.y - p.y

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def mag(self):
        return (self.x**2 + self.y**2)**(1/2)

    def __gt__(self, p):
        return self.mag() > p.mag()
    def __ge__(self, p):
        return self.mag() >= p.mag()
    def __lt__(self, p):
        return self.mag() < p.mag()
    def __le__(self, p):
        return self.mag() <= p.mag()
    def __eq__(self, p):
        return self.mag() == p.mag()


p1 = Point(1, 4)
p2 = Point(5, 4)
p3 = Point(-5, -4)
p4 = Point(-10, 10)
p5 = p2 <= p3
print(p5)