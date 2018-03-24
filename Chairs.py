from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np
from numpy import *

def myInit():
    glMatrixMode(GL_PROJECTION)

    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,.1,50)
    gluLookAt(15,15,15,0,0,0,0,1,0)

def chair():

    #Chair_Back

    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glPushMatrix()
    glColor3f(1,0,0)
    glScale(1,1.5,0.5)
    glTranslate(0,1,0)
    glutWireCube(4)
    glPopMatrix()
    glPopAttrib()


    #Chair_Seat

    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glPushMatrix()
    glColor3f(1,0,0)
    glScale(1,0.5,1)
    glTranslate(0,-1.5,3)
    glutWireCube(4)
    glPopMatrix()
    glPopAttrib()

    #Chair_Legs

    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glPushMatrix()
    glColor3f(1,0,0)
    glScale(0.25,1.5,0.25)
    glTranslate(1,-3.5,-2)
    glutWireCube(4)
    glPopMatrix()
    glPopAttrib()

    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glPushMatrix()
    glColor3f(1,0,0)
    glScale(0.25,1.5,0.25)
    glTranslate(-12,-3.5,-2)
    glutWireCube(4)
    glPopMatrix()
    glPopAttrib()

    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glPushMatrix()
    glColor3f(1,0,0)
    glScale(0.25,1.5,0.25)
    glTranslate(1,-3.5,12)
    glutWireCube(4)
    glPopMatrix()
    glPopAttrib()

    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glPushMatrix()
    glColor3f(1,0,0)
    glScale(0.25,1.5,0.25)
    glTranslate(-12,-3.5,12)
    glutWireCube(4)
    glPopMatrix()
    glPopAttrib()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    chair()
    glLoadIdentity()
    glTranslate(10,0,0)
    chair()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(100,100)
glutInitWindowSize(600, 600)
glutCreateWindow(b"MyChair")
myInit()
glutDisplayFunc(draw)
glutMainLoop()
