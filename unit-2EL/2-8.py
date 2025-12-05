#A geometry class uses a static method to compute triangle area.
# You must call it without creating objects and print the output.

class Geometry:
    @staticmethod
    def triangle_area(base, height):
        return 0.5 * base * height

print(Geometry.triangle_area(10, 5))
print(Geometry.triangle_area(6, 8))
print(Geometry.triangle_area(12, 7))