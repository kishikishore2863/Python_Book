#A travel class uses a static method to compute distance between coordinates.
# You must test it with three coordinate pairs.

import math

class Travel:
    @staticmethod
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

pairs = [
    (0, 0, 3, 4),
    (1, 2, 4, 6),
    (-2, -1, 3, 3)
]

for x1, y1, x2, y2 in pairs:
    print(Travel.distance(x1, y1, x2, y2))