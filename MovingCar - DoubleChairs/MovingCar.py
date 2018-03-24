from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np
from numpy import *

def myInit():
    glMatrixMode(GL_PROJECTION)

    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,0.1,50)
    gluLookAt(5,5,5,0,0,0,0,1,0)
    #glOrtho(-10,10,-10,10,-10,10)
#result = False
x = -10
angle = 0
def draw():

    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global angle
    global result

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3f(0,0,0)
    glTranslate(0,0,-1)
    glScale(10,0.25,1.5)
    glutSolidCube(7)

    glColor3f(0,1,0)
    glTranslate(0,0,-15)
    glScale(10,0.25,3)
    glutSolidCube(7)

    glColor3f(0,1,0)
    glTranslate(0,0,16.5)
    glScale(10,0.25,3)
    glutSolidCube(7)

    for i in range(-100,100,10):
        glLoadIdentity()
        glColor(1, 1, 1)
        glScale(0.5, 0.001, 0.2)
        glTranslate(i+x, 0, 0)
        glutSolidCube(4)
        glColor(0.34,0.17,0.035)
        glLoadIdentity()
        glScale(1,1,1)
        glTranslate(i+x, 0, -20)
        glutSolidCube(4)
        glLoadIdentity()
        glScale(1,1,1)
        glTranslate(i+x, 0, 5.5)
        glutSolidCube(4)

    glLoadIdentity()
    glColor3f(1,0,0)
    glTranslate(x,0,0)
    glScale(1,0.25,0.5)
    glutWireCube(5)
    glLoadIdentity()
    glTranslate(x,0.25*5,0)
    glScale(0.5,0.25,0.5)
    glutWireCube(5)

    glColor3f(1,1,0)
    glLoadIdentity()



    glTranslate(x+2.5,-2.5*0.25,2.5*0.5)
    glRotate(angle,0,0,1)
    glutWireTorus(0.125,0.5,12,8)

    glColor3f(1,1,0)
    glLoadIdentity()

    glTranslate(x+2.5,-0.25*2.5,-2.5*0.5)
    glRotate(angle,0,0,1)
    glutWireTorus(0.125,0.5,12,8)

    glColor3f(1,1,0)
    glLoadIdentity()

    glTranslate(x-2.5,-0.25*2.5,2.5*0.5)
    glRotate(angle,0,0,1)
    glutWireTorus(0.125,0.5,12,8)

    glColor3f(1,1,0)
    glLoadIdentity()

    glTranslate(x-2.5,-0.25*2.5,-2.5*0.5)
    glRotate(angle,0,0,1)
    glutWireTorus(0.125,0.5,12,8)


    if x > 10:
        x = -10


    x += 0.007



    """
    
    This code below for moving forward and backward <3
    if x>3:
        result = False


    elif x < -3:
        result = True



    if result:
        x += 0.007
        angle -= 0.1
    else:
        x -= 0.007
        angle += 0.1

    """


    glFlush()



glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
glutDisplayFunc(draw)
glutIdleFunc(draw)
myInit()
glutMainLoop()


