from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import randint

w,h= 500,500

bawah = randint(0, 300)
atas = bawah + 150

x1 = 600
x2 = 550

y_atas = 0
y_bawah = 0

geser = 0
jatuh = 0

def kotak():
    global x1, x2
    glColor3ub(35, 235, 39)
#    glTranslatef(geser, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(x1, 500)
    glVertex2f(x2, 500)
    glVertex2f(x2, atas)
    glVertex2f(x1, atas)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(x1, bawah)
    glVertex2f(x2, bawah)
    glVertex2f(x2, 0)
    glVertex2f(x1, 0)
    glEnd()

def karakter():
    global y_atas, y_bawah
    glPushMatrix()
    glColor3ub(235, 221, 28)
    glBegin(GL_QUADS)
    glVertex2f(100, 250+y_atas+jatuh)
    glVertex2f(125, 250+y_atas+jatuh)
    glVertex2f(125, 275+y_bawah+jatuh)
    glVertex2f(100, 275+y_bawah+jatuh)
    glEnd()
    glPopMatrix()

def controller(key, x, y):
    global y_bawah, y_atas
    if key == GLUT_KEY_UP:
        y_bawah += 75
        y_atas += 75
        print("naik")

def timer(value):
    global x1, x2
    x1 -= 5
    x2 -= 5
    glutTimerFunc(100, timer, 10)

def gravitasi(value):
    global jatuh
    jatuh -= 10
    glutTimerFunc(85, gravitasi, 10)

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    karakter()
    kotak()
    if x1 == 500 :
        kotak()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("202410103018_IkangTanoto_GambarGeogebra ")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(controller)
#glutTimerFunc(50, update, 0)
gravitasi(0)
timer(0)
glutMainLoop()