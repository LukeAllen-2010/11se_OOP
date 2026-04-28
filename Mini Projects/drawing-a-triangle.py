import math
from turtle import *
class Calculation:
    def __init__(self, Side1, Side2, Side3):
        self.a = Side1
        self.b = Side2
        self.c = Side3
        self.scale = 10
    def angle_from_sides(self, Side1, Side2, Side3):
        # Ensure valid triangle
        if Side1 <= 0 or Side2 <= 0 or Side3 <= 0:
            raise ValueError('Sides must be positive.')
        # Cosine Rule for angle opposite side self.c
        cos_C = (Side1**2 + Side2**2 - Side3**2) / (2 * Side1 * Side2)
        # Clamp cos_C to [-1, 1] to avoid math domain error due to rounding
        cos_C = max(-1, min(1, cos_C))
        angle_C_rad = math.acos(cos_C)
        angle_C_deg = math.degrees(angle_C_rad)
        return 180 - angle_C_deg

    def find_triangle_type(self):
        right_angled = False
        if not self.a + self.b > self.c or not self.b + self.c > self.a or not self.c + self.a > self.b:
            raise ValueError("Invalid triangle")
        else:
            if self.a == self.b == self.c:
                triangle_type = 'Equilateral'
            if self.a == self.b or self.b == self.c or self.c == self.a:
                triangle_type = 'Isosceles'
            else:
                triangle_type = 'Scalene'
            if self.c == math.sqrt((self.a)**2 + (self.b)**2) or self.b == math.sqrt((self.a)**2 + (self.c)**2) or self.a == math.sqrt((self.c)**2 + (self.b)**2):
                right_angled == True
            return triangle_type, right_angled

    def draw_triangle(self):
        forward(self.a * self.scale)
        print(f"forward({self.a})")
        left(self.angle_from_sides(self.a, self.b, self.c))
        forward(self.b * self.scale)
        print(f"forward({self.b})")
        left(self.angle_from_sides(self.b, self.c, self.a))
        forward(self.c * self.scale)
        print(f"forward({self.c})")
        done()

# side1 = int(input("Side 1: "))
# side2 = int(input("Side 2: "))
# side3 = int(input("Side 3: "))
# print(f"The triange is {find_triangle_type(side1, side2, side3)}")
# if not find_triangle_type(side1, side2, side3) == "Invalid triangle":
#     draw_triangle(side1, side2, side3)




# if a == input("Side 1: "), b == , c == , input("Side 2: "), input("Side 3: "):
#     try:
#         draw_triangle()
#     except "Invalid triangle":
#         print("Bruv lock in")



a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

calculation = Calculation(a, b, c)

try:
    calculation.draw_triangle()
except ValueError:
    print("Values less than 1:", ValueError)