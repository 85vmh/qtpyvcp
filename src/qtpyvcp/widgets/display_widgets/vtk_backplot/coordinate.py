class Coordinate:
    def __init__(self, x, y, z, a, b, c, u, v, w, r):
        self.x = x
        self.y = y
        self.z = z
        self.a = a
        self.b = b
        self.c = c
        self.u = u
        self.v = v
        self.w = w
        self.r = r

    @classmethod
    def fromTuple(cls, coords):
        if len(coords) != 10:
            raise ValueError("Tuple must have exactly 10 elements.")
        return cls(*coords)

    def __repr__(self):
        return (f"Coordinate(x={self.x}, y={self.y}, z={self.z}, a={self.a}, " 
                f"b={self.b}, c={self.c}, u={self.u}, v={self.v}, w={self.w}, r={self.r})")