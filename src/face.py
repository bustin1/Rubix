import pyglet
import numpy as np
from pyglet.gl import *

class Face:

    sideLen = 20
    half_pi = np.pi/2

    def __init__(self, x, y, z, c):
        self.normal = [x, y, z]
        self.pos = [x, y, z]
        self.change = [i for i in self.normal]
        self.color = c
        self.t = 0
        self.d = 0
        self.phi = 0
        self.axis = [0,0,0]


    def square(self):
        coor = [-.5,-.5, -.5,.5, .5,.5, .5,-.5]
        pyglet.graphics.draw(4, GL_QUADS, ('v2f', coor))


    def show(self):
        glColor3ub(*self.color)

        glPushMatrix()

        glRotatef(np.degrees(self.phi), self.axis[0], self.axis[1], self.axis[2])

        glTranslatef(.5 * self.normal[0], .5 * self.normal[1], .5 * self.normal[2])
        glRotatef(90, self.normal[1], self.normal[0], 0)

        self.square()

        glPopMatrix()


    def turnFace(self, d, phi, axis):

        self.axis = axis
        if sum(axis) > 0:
            self.phi = phi
        else:
            self.phi = -phi

    def reset(self, d, i1, i2):

        x = self.pos[i1]
        y = self.pos[i2]
        half_pi = Face.half_pi * d

        self.normal[i1] = round(x*np.cos(half_pi) - y*np.sin(half_pi))
        self.normal[i2] = round(x*np.sin(half_pi) + y*np.cos(half_pi))

        self.phi = 0

        self.pos[i1] = self.normal[i1]
        self.pos[i2] = self.normal[i2]




