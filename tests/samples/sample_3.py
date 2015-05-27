class Shape:
    def radius(self, r):
        return r * r * 3.1415;
		
    def area(self, x, y):
        return x * y

    def __str__(self):
        return "x&Y"