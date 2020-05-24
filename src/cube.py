import pyglet
from pyglet.gl import *
from face import Face
import numpy as np

class Cube:

    sideLen = 20

    def __init__(self, x, y, z):


        self.faces = 6 * [0]
        self.faces[0] = Face(0, 0, 1, (255,255,255))
        self.faces[1] = Face(1, 0, 0, (255,0,0))
        self.faces[2] = Face(0, 0, -1, (240,255,0))
        self.faces[3] = Face(-1, 0, 0, (255,165,0))
        self.faces[4] = Face(0, 1, 0, (0,0,255))
        self.faces[5] = Face(0, -1, 0, (0,255,0))

        self.phi = 0
        self.axis = [0,0,0]
        self.change = [x, y, z]
        self.pos = [x, y, z]

        self.goodToTurn = True

    def show(self):

        glPushMatrix()

        glScalef(self.sideLen, self.sideLen, self.sideLen)
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        for f in self.faces:
            f.show()

        glPopMatrix()


    def turn(self, d, axis):

        self.axis = axis # axis of rotation
        self.phi = 0 #initial angle
        self.change = [self.pos[0], self.pos[1], self.pos[2]] # intitial position

        if axis[0] == 0 and axis[1] == 0:
            pyglet.clock.schedule_interval(self.animate, .01, d, 0, 1)
        elif axis[0] == 0 and axis[2] == 0:
            pyglet.clock.schedule_interval(self.animate, .01, d, 2, 0)
        elif axis[1] == 0 and axis[2] == 0:
            pyglet.clock.schedule_interval(self.animate, .01, d, 1, 2)

        self.goodToTurn = False


    def animate(self, dt, d, i1, i2):

        self.pos[i1] = round(self.change[i1] * np.cos(self.phi)
                     - self.change[i2] * np.sin(self.phi), 10)
        self.pos[i2] = round(self.change[i1] * np.sin(self.phi)
                     + self.change[i2] * np.cos(self.phi), 10)


        self.phi += .05 * d

        for f in self.faces:
            f.turnFace(d, self.phi, self.axis)

        if abs(self.phi) >= np.pi/2:
            if self.phi > 0:
                self.phi = np.pi/2
            else:
                self.phi = -np.pi/2

            self.pos[i1] = round(self.change[i1] * np.cos(self.phi)
                         - self.change[i2] * np.sin(self.phi))
            self.pos[i2] = round(self.change[i1] * np.sin(self.phi)
                         + self.change[i2] * np.cos(self.phi))

            self.phi = 0
            pyglet.clock.unschedule(self.animate)
            for f in self.faces:
                f.reset(d, i1, i2)

            self.goodToTurn = True












