from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



def init():
    global MatShnF
    #LightPos     =  [ 0, 0 , -3 , 0 ]  # Directional light source is at infinite, z = -infinte
    #LightPos     =  [ 0, 0 , 3 , 0 ]   # Directional light source is at infinite, z = +infinte
    #LightPos     =  [ 0, 3 , 0 , 0 ]   # Directional light source is at infinite, y = +infinte

    LightPos     =  [ 0, 0 , 0 , 1 ] # Positional light source
    LightAmb     =  [ 0.2, 0.2 , 0.2 , 1.0 ]   # RGBA of Ambient Light
    LightDiff    =  [ 1, 1 , 1 , 1.0 ]  # RGBA of Diffuse Light
    LightSpec    =  [ 0, 0 , 1 , 1.0 ]  # RGBA of Specular Light


    MatShnF       =  [ 128 ]

    glLightfv(GL_LIGHT0, GL_POSITION, LightPos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, LightAmb)
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  LightDiff)
    glLightfv(GL_LIGHT0, GL_SPECULAR, LightSpec)


    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45, 1, 0.1, 50)
    gluLookAt(10, 10, 10, 0, 0, 0, 0, 1, 0)

    glEnable(GL_DEPTH_TEST)

def DrawPlanet(sun_dist, radius, angle, r, g, b):
    global MatShnF
    glLoadIdentity()

    # Relection of front-face Material
    MatAmbF       =  [ r , g , b ,1 ]
    #MatAmbF       =  [ 0 , 0 , 0 ,1 ] # try this
    MatDifF       =  [ r , g , b ,1 ]
    MatSpecF      =  [ r , g , b ,1 ]
    #MatSpecF      =  [ 0 , 0 , 0 ,0 ]  # try this
    glMaterialfv(GL_FRONT, GL_AMBIENT , MatAmbF)
    glMaterialfv(GL_FRONT, GL_DIFFUSE , MatDifF)
    glMaterialfv(GL_FRONT, GL_SPECULAR , MatSpecF)
    glMaterialfv(GL_FRONT, GL_SHININESS , MatShnF)


    glColor(0.3, 0.3, 0.3)
    glutSolidTorus(0.01, sun_dist, 30, 30)
    glColor(r,g,b)
    glRotate(angle,0, 0, 1)
    glTranslate(sun_dist,0,0)
    #glRotate(angle,0, 0, 1)
    glutSolidSphere(radius,30,30)

angle = [0, 0]

def display_1():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor(1 ,0, 0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    #Sun
    MatAmbF       =  [ 1 , 1, 0 ,1 ]
    #MatAmbF       =  [ 0 , 0 , 0 ,1 ] # try this
    MatDifF       =  [ 1 , 1 , 0 ,1 ]
    MatSpecF      =  [ 1 , 1 , 0 ,1 ]
    #MatSpecF      =  [ 0 , 0 , 0 ,0 ]  # try this
    glMaterialfv(GL_FRONT, GL_AMBIENT , MatAmbF)
    glMaterialfv(GL_FRONT, GL_DIFFUSE , MatDifF)
    glMaterialfv(GL_FRONT, GL_SPECULAR , MatSpecF)
    glMaterialfv(GL_FRONT, GL_SHININESS , MatShnF)
    glColor(1, 1, 0)
    glutSolidSphere(1, 30, 30)

    #Mercury
    DrawPlanet(3, 0.5, angle[0], 1, 0, 0)
    angle[0] = (angle[0] % 360) + 0.1

    #vernus
    DrawPlanet(5, 0.7,angle[1], 1, 0, 1)
    angle[1] = (angle[1] % 360) + 0.15


    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE|GLUT_DEPTH)
    glutInitWindowPosition(500,500)
    glutCreateWindow(b"SolarSystem")
    glutDisplayFunc(display_1)
    glutIdleFunc(display_1)
    init()
    glutMainLoop()

main()


