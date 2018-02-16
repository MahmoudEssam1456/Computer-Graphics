from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def draw1():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)         #legs is here
    glColor(0.85, 0.49, 0.023)
    for theta in np.arange(0,2*pi,0.01):
        x = 0.1*sin(theta) +0.2
        y = 0.2*cos(theta) -0.7
        glVertex2d(x, y)
    glEnd()
    glBegin(GL_POLYGON)             #legs is here
    glColor(0.85, 0.49, 0.023)
    for theta in np.arange(0,2*pi,0.01):
        x = 0.1*sin(theta) -0.2
        y = 0.2*cos(theta) -0.7
        glVertex2d(x, y)
    glEnd()
    glBegin(GL_POLYGON)             #Hand of the fan is here
    glColor(0.85, 0.49, 0.023)
    glVertex2d(0.3, 0)
    glVertex2d( 0.6, 0)
    glVertex2d( 0.6, -0.2)
    glVertex2d(0.3, -0.2)
    glEnd()
    glBegin(GL_POLYGON)             #Hand of the fan is here
    glColor(0.85, 0.49, 0.023)
    glVertex2d(-0.3, 0)
    glVertex2d( -0.6, 0)
    glVertex2d( -0.6, -0.2)
    glVertex2d(-0.3, -0.2)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.16, 0.25, 0.29)       #Body is here
    for theta in np.arange(0,2*pi,0.01):
        x = 0.5*sin(theta)
        y = 0.65*cos(theta)
        z = 0
        glVertex3f(x,y,z)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(1, 1, 1)                #cutting the body with background
    for theta in np.arange(0,2*pi,0.01):
        x = 0.5*sin(theta)
        y = 0.65*cos(theta) + 0.85
        z = 0
        glVertex3f(x,y,z)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.69, 0.011, 0.011)     #Knee is here
    glVertex2d(-0.1, 0.5)
    glVertex2d( 0.1, 0.5)
    glVertex2d( 0.1, 0.2)
    glVertex2d(-0.1, 0.2)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.16, 0.25, 0.29)       #Head is here
    for theta in np.arange(0,2*pi,0.01):
        x = 0.4*sin(theta)
        y = 0.3*cos(theta) +0.6
        glVertex2d(x, y)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.85, 0.49, 0.023)      #Fan is here
    for theta in np.arange(0,2*pi,0.01):
        x = 0.1*sin(theta) +0.7
        y = 0.4*cos(theta) -0.1
        glVertex2d(x, y)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.85, 0.49, 0.023)      #Fan is here
    for theta in np.arange(0,2*pi,0.01):
        x = 0.1*sin(theta) -0.7
        y = 0.4*cos(theta) -0.1
        glVertex2d(x, y)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.83, 0.83, 0.83)       #Face is here
    for theta in np.arange(0,2*pi,0.01):
        x = 0.3*sin(theta)
        y = 0.3*cos(theta) +0.6
        glVertex2d(x, y)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.69, 0.011, 0.011)     #Eye Border is here
    for theta in np.arange(0,2*pi,0.01):
        x = 0.17*sin(theta) - 0.2
        y = 0.17*cos(theta) +0.6
        glVertex2d(x, y)
    glEnd()
    glBegin(GL_POLYGON)              #Eye Border is here
    glColor(0.69, 0.011, 0.011)
    for theta in np.arange(0,2*pi,0.01):
        x = 0.17*sin(theta) + 0.2
        y = 0.17*cos(theta) +0.6
        glVertex2d(x, y)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(1, 1, 1)                #Eye is here
    for theta in np.arange(0,2*pi,0.01):
        x = 0.14*sin(theta) + 0.2
        y = 0.14*cos(theta) +0.6
        glVertex2d(x, y)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(1, 1, 1)                 #Eye is here
    for theta in np.arange(0,2*pi,0.01):
        x = 0.14*sin(theta) - 0.2
        y = 0.14*cos(theta) +0.6
        glVertex2d(x, y)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0, 0, 0)                 #Eye is here
    for theta in np.arange(0,2*pi,0.01):
        x = 0.1*sin(theta) + 0.2
        y = 0.1*cos(theta) +0.6
        glVertex2d(x, y)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0, 0, 0)                 #Eye is here
    for theta in np.arange(0,2*pi,0.01):
        x = 0.1*sin(theta) - 0.2
        y = 0.1*cos(theta) +0.6
        glVertex2d(x, y)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(1, 1, 1)                 #Eye is here
    for theta in np.arange(0,2*pi,0.01):
        x = 0.02*sin(theta) + 0.2
        y = 0.02*cos(theta) +0.6
        glVertex2d(x, y)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(1, 1, 1)                 #Eye is here
    for theta in np.arange(0,2*pi,0.01):
        x = 0.02*sin(theta) - 0.2
        y = 0.02*cos(theta) +0.6
        glVertex2d(x, y)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.69, 0.011, 0.011)     #Legs is here
    glVertex2d(0.1, -0.7)
    glVertex2d( 0.3, -0.7)
    glVertex2d( 0.3, -0.9)
    glVertex2d(0.1, -0.9)
    glEnd()
    glBegin(GL_POLYGON)             #Legs is here
    glColor(0.69, 0.011, 0.011)
    glVertex2d(-0.1, -0.7)
    glVertex2d( -0.3, -0.7)
    glVertex2d( -0.3, -0.9)
    glVertex2d(-0.1, -0.9)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.83, 0.83, 0.83)       #Circle for Logo
    for theta in np.arange(0,2*pi,0.01):
        x = 0.3*sin(theta)
        y = 0.3*cos(theta) - 0.2
        glVertex2d(x, y)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.69, 0.011, 0.011)    #Letter M
    glVertex2d(-0.2, -0.01)
    glVertex2d( 0.2, -0.01)
    glVertex2d( 0.2, -0.37)
    glVertex2d(-0.2, -0.37)
    glEnd()
    glBegin(GL_POLYGON)             #Letter M
    glColor(0.83, 0.83, 0.83)
    glVertex2d(-0.1, -0.01)
    glVertex2d( 0.1, -0.01)
    glVertex2d( 0, -0.2)
    glEnd()
    glBegin(GL_POLYGON)             #Letter M
    glColor(0.83, 0.83, 0.83)
    glVertex2d(0, -0.37)
    glVertex2d( 0.1, -0.37)
    glVertex2d( 0.1, -0.2)
    glEnd()
    glBegin(GL_POLYGON)             #Letter M
    glColor(0.83, 0.83, 0.83)
    glVertex2d(0, -0.37)
    glVertex2d(-0.1, -0.37)
    glVertex2d(-0.1, -0.2)
    glEnd()
    glBegin(GL_LINE_LOOP)           #Mouse
    glColor(0.85, 0.49, 0.023)
    for theta in np.arange(0,2*pi,0.001):
        x = 0.09*sin(theta)
        y = 0.07*cos(theta) + 0.4
        z = 0
        glVertex3f(x,y,z)
    glEnd()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"Boqloz")
glutInitWindowSize(600, 600)   # Set the window's initial width & height
glutDisplayFunc(draw1)
glutMainLoop()
