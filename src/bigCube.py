


class BigCube:
    def __init__(self, cubes):
        self.cubes = cubes

    def turn(self, d, x, y, z):
        axis = [x,y,z]
        if x != 0:
            for c in self.cubes:
                if not c.goodToTurn:
                    return
            for c in self.cubes:
                if c.pos[0] == x:
                    c.turn(d, axis)
        if y != 0:
            for c in self.cubes:
                if not c.goodToTurn:
                    return
            for c in self.cubes:
                if c.pos[1] == y and c.goodToTurn:
                    c.turn(d, axis)
        if z != 0:
            for c in self.cubes:
                if not c.goodToTurn:
                    return
            for c in self.cubes:
                if c.pos[2] == z and c.goodToTurn:
                    c.turn(d, axis)

    def show(self):
        for c in self.cubes:
            c.show()


