import pyglet
from pyglet.gl import *
from pyglet.window import key
import numpy as np
#from ctypes import pointer, sizeof
from bigCube import BigCube
from cube import Cube
from face import Face
#from OpenGL.GLUT import *

WIDTH = 600
HEIGHT = 600
INCREMENT = 5

faceLen = 60
sideLen = 20

class Window(pyglet.window.Window):

   # Cube 3D start rotation
    xRotation = yRotation = 0
    dim = 3
    dim3 = dim ** 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        glClearColor(.5, .5, .5, 1)
        glEnable(GL_DEPTH_TEST)

        self.smallCubes = []
        for i in range(-1, self.dim-1):
            for j in range(-1, self.dim-1):
                for k in range(-1, self.dim-1):
                    self.smallCubes.append(Cube(i, j, k))

        self.bigCube = BigCube(self.smallCubes)



    def on_draw(self):
        # Clear the current GL Window
        self.clear()

        # Push Matrix onto stack
        glPushMatrix()

        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.yRotation, 0, 1, 0)

        self.bigCube.show()

        # Pop Matrix off stack
        glPopMatrix()



    def on_resize(self, width, height):

        # set the Viewport
        glViewport(0, 0, width, height)

        # using Projection mode,
        # to reset aspect and clipping
        # plane
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspectRatio = width / height
        gluPerspective(45, aspectRatio, 1, 1000)

        # the camera doesn't move,
        # the object does
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -200)

        print("resizing to %d,%d"%(width,height))


    def on_text_motion(self, motion):
        if motion == key.UP:
            self.xRotation -= INCREMENT
        elif motion == key.DOWN:
            self.xRotation += INCREMENT
        elif motion == key.LEFT:
            self.yRotation -= INCREMENT
        elif motion == key.RIGHT:
            self.yRotation += INCREMENT

#    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):



    def on_key_press(self, symbol, modifier):
        print(f"{self.xRotation}, {self.yRotation}")
        glPushMatrix()
        if keys[key.W] and keys[key.LSHIFT]:
            xang = np.radians(90 * ((-self.xRotation + 45) // 90))
            y = round(np.cos(xang), 2)
            z = round(np.sin(xang), 2)
            self.bigCube.turn(y+z, 0,y,z)
        elif keys[key.W]:
            xang = np.radians(90 * ((self.xRotation + 45) // 90))
            y = round(np.cos(xang), 2)
            z = -round(np.sin(xang), 2)
            self.bigCube.turn(-y-z, 0,y,z)
        elif keys[key.S] and keys[key.LSHIFT]:
            self.bigCube.turn(-1, 0,-1,0)
        elif keys[key.S]:
            self.bigCube.turn(1, 0,-1,0)
        elif keys[key.D] and keys[key.LSHIFT]:
            yang = np.radians(90 * ((-self.yRotation + 45) // 90))
            x = round(np.cos(yang), 2)
            z = -round(np.sin(yang), 2)
            self.bigCube.turn(x+z, x,0,z)
        elif keys[key.D]:
            yang = np.radians(90 * ((-self.yRotation + 45) // 90))
            x = round(np.cos(yang), 2)
            z = -round(np.sin(yang), 2)
            self.bigCube.turn(-x-z, x,0,z)
        elif keys[key.A] and keys[key.LSHIFT]:
            yang = np.radians(90 * ((self.yRotation + 45) // 90))
            x = -round(np.cos(yang), 2)
            z = -round(np.sin(yang), 2)
            self.bigCube.turn(x+z, x,0,z)
        elif keys[key.A]:
            yang = np.radians(90 * ((self.yRotation + 45) // 90))
            x = -round(np.cos(yang), 2)
            z = -round(np.sin(yang), 2)
            self.bigCube.turn(-x-z, x,0,z)
        elif keys[key.Q] and keys[key.LSHIFT]:
            yang = np.radians(90 * ((self.yRotation + 135) // 90))
            x = round(np.cos(yang), 2)
            z = round(np.sin(yang), 2)
            self.bigCube.turn(x+z, x,0,z)
        elif keys[key.Q]:
            yang = np.radians(90 * ((self.yRotation + 135) // 90))
            x = round(np.cos(yang), 2)
            z = round(np.sin(yang), 2)
            self.bigCube.turn(-x-z, x,0,z)
        elif keys[key.E] and keys[key.LSHIFT]:
            yang = np.radians(90 * ((self.yRotation + 135) // 90))
            x = -round(np.cos(yang), 2)
            z = -round(np.sin(yang), 2)
            self.bigCube.turn(x+z, x,0,z)
        elif keys[key.E]:
            yang = np.radians(90 * ((self.yRotation + 135) // 90))
            x = -round(np.cos(yang), 2)
            z = -round(np.sin(yang), 2)
            self.bigCube.turn(-x-z, x,0,z)
        glPopMatrix()




if __name__ == '__main__':
    keys = key.KeyStateHandler()
    window = Window(width=WIDTH, height=HEIGHT, caption='Pyglet Colored Cube', resizable=True)
    window.push_handlers(keys)
    pyglet.app.run()

# TODO: 
# Add random scramle
# Add Reset
# Maybe LATER: ADD solver


