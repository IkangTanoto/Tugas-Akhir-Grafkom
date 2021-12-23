from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
from random import randrange
from background import *

w,h= 500,500
bg = background(1)
font1 = GLUT_BITMAP_TIMES_ROMAN_24
font2 = GLUT_BITMAP_HELVETICA_12
naik = 0
moveStop = False
skor = 0
game_over = 0

bawah = randrange(50, 300, 25)
atas = bawah + 150
geser = 0

bawah2 = randrange(50, 300, 25)
atas2 = bawah2 + 150
geser2 = 150

bawah3 = randrange(50, 300, 25)
atas3 = bawah3 + 150
geser3 = 300

def drawLine (list_titik) :
    glLineWidth(0.5)
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    for i in range (len(list_titik)) :
        if i != len(list_titik)-1 :
            glVertex2f(list_titik[i][0], list_titik[i][1])
            glVertex2f(list_titik[i+1][0], list_titik[i+1][1])
        elif i == len(list_titik)-1 :
            glVertex2f(list_titik[i][0], list_titik[i][1])
            glVertex2f(list_titik[0][0], list_titik[0][1])
    glEnd()

def garis(titikA, titikB):
    glLineWidth(0.5)
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    glVertex2f(titikA[0], titikA[1])
    glVertex2f(titikB[0], titikB[1])
    glEnd()

def jendela(x, y):
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3ub(255, 253, 200)
    glVertex2f(x, y)
    glEnd()
    glBegin(GL_POINTS)
    glColor3ub(255, 253, 200)
    glVertex2f(x, y+10)
    glEnd()

def kotak():
    global atas,bawah, geser
    if geser%(-450) == 0 :
        bawah = randrange(50, 300, 25)
        atas = bawah + 150
    a = 500+geser
    b = a - 50
    if geser <= -450 :
        geser = 0
# BAGIAN ATAS
    glBegin(GL_POLYGON) #outline putih
    glColor3f(1, 1, 1)
    glVertex2f(b-1, 500)
    glVertex2f(b-1, atas+4)
    glVertex2f(b+4, atas-1)
    glVertex2f(a-4, atas-1)
    glVertex2f(a+1, atas+4)
    glVertex2f(a+1, 500)
    glEnd()
    glBegin(GL_POLYGON) #kotak atas
    glColor3f(0, 0, 0)
    glVertex2f(b, 500)
    glVertex2f(b, atas+5)
    glVertex2f(b+5, atas)
    glVertex2f(a-5, atas)
    glVertex2f(a, atas+5)
    glVertex2f(a, 500)
    glEnd()
    jendela(465+geser, atas+25)
    jendela(485+geser, atas+25)
    jendela(465+geser, atas+55)
    jendela(485+geser, atas+55)
    jendela(465+geser, atas+85)
    jendela(485+geser, atas+85)
    jendela(465+geser, atas+115)
    jendela(485+geser, atas+145)
    jendela(465+geser, atas+175)
    jendela(485+geser, atas+175)
    jendela(485+geser, atas+205)
    jendela(485+geser, atas+235)
    jendela(465+geser2, atas+235)
    glBegin(GL_QUADS) #garis item di atas
    glColor3f(0, 0, 0)
    glVertex2f(500+geser, 480)
    glVertex2f(500+geser, 500)
    glVertex2f(450+geser, 500)
    glVertex2f(450+geser, 480)
    glEnd()
# BAGIAN BAWAH
    glBegin(GL_POLYGON) #outline putih
    glColor3f(1, 1, 1)
    glVertex2f(b-1, 0)
    glVertex2f(b-1, bawah-4)
    glVertex2f(b+4, bawah-4)
    glVertex2f(b+4, bawah+1)
    glVertex2f(a-4, bawah+1)
    glVertex2f(a-4, bawah-4)
    glVertex2f(a+1, bawah-4)
    glVertex2f(a+1, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex2f(b, 0)
    glVertex2f(b, bawah-5)
    glVertex2f(b+5, bawah-5)
    glVertex2f(b+5, bawah)
    glVertex2f(a-5, bawah)
    glVertex2f(a-5, bawah-5)
    glVertex2f(a, bawah-5)
    glVertex2f(a, 0)
    glEnd()
    jendela(465+geser, bawah-35)
    jendela(465+geser, bawah-65)
    jendela(465+geser, bawah-95)
    jendela(485+geser, bawah-95)
    jendela(465+geser, bawah-125)
    jendela(485+geser, bawah-155)
    jendela(465+geser, bawah-155)
    jendela(485+geser, bawah-185)
    jendela(465+geser, bawah-215)
    jendela(485+geser, bawah-245)
    jendela(465+geser, bawah-245)
    glBegin(GL_QUADS) #garis item di bawah
    glColor3f(0, 0, 0)
    glVertex2f(500+geser, 20)
    glVertex2f(500+geser, 0)
    glVertex2f(450+geser, 0)
    glVertex2f(450+geser, 20)
    glEnd()

def kotak2():
    global atas2,bawah2, geser2
    if geser2%(-450) == 0 :
        bawah2 = randrange(50, 300, 25)
        atas2 = bawah2 + 150
    c = 500+geser2
    d = c - 50
    if geser2 <= -450 :
        geser2 = 0
#BAGIAN ATAS
    glBegin(GL_POLYGON) #outline putih
    glColor3f(1, 1, 1)
    glVertex2f(d-1, 500)
    glVertex2f(d-1, atas2+4)
    glVertex2f(d+4, atas2+4)
    glVertex2f(d+4, atas2-1)
    glVertex2f(c-4, atas2-1)
    glVertex2f(c-4, atas2+4)
    glVertex2f(c+1, atas2+4)
    glVertex2f(c+1, 500)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex2f(d, 500)
    glVertex2f(d, atas2+5)
    glVertex2f(d+5, atas2+5)
    glVertex2f(d+5, atas2)
    glVertex2f(c-5, atas2)
    glVertex2f(c-5, atas2+5)
    glVertex2f(c, atas2+5)
    glVertex2f(c, 500)
    glEnd()
    jendela(465+geser2, atas2+25)
    jendela(485+geser2, atas2+25)
    jendela(465+geser2, atas2+55)
    jendela(485+geser2, atas2+55)
    jendela(485+geser2, atas2+85)
    jendela(485+geser2, atas2+115)
    jendela(465+geser2, atas2+145)
    jendela(465+geser2, atas2+175)
    jendela(485+geser2, atas2+175)
    jendela(465+geser2, atas2+205)
    jendela(485+geser2, atas2+205)
    jendela(465+geser2, atas2+235)
    glBegin(GL_QUADS) #garis item di atas
    glColor3f(0, 0, 0)
    glVertex2f(500+geser2, 480)
    glVertex2f(500+geser2, 500)
    glVertex2f(450+geser2, 500)
    glVertex2f(450+geser2, 480)
    glEnd()
#BAGIAN BAWAH
    glBegin(GL_POLYGON) #outline putih
    glColor3f(1, 1, 1)
    glVertex2f(d-1, 0)
    glVertex2f(d-1, bawah2-4)
    glVertex2f(d+4, bawah2+1)
    glVertex2f(c-4, bawah2+1)
    glVertex2f(c+1, bawah2-4)
    glVertex2f(c+1, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex2f(d, 0)
    glVertex2f(d, bawah2-5)
    glVertex2f(d+5, bawah2)
    glVertex2f(c-5, bawah2)
    glVertex2f(c, bawah2-5)
    glVertex2f(c, 0)
    glEnd()
    jendela(465+geser2, bawah2-35)
    jendela(485+geser2, bawah2-65)
    jendela(465+geser2, bawah2-65)
    jendela(465+geser2, bawah2-95)
    jendela(485+geser2, bawah2-95)
    jendela(465+geser2, bawah2-125)
    jendela(485+geser2, bawah2-155)
    jendela(485+geser2, bawah2-185)
    jendela(465+geser2, bawah2-185)
    jendela(465+geser2, bawah2-215)
    jendela(485+geser2, bawah2-245)
    jendela(465+geser2, bawah3-245)
    glBegin(GL_QUADS) #garis item di bawah
    glColor3f(0, 0, 0)
    glVertex2f(500+geser2, 20)
    glVertex2f(500+geser2, 0)
    glVertex2f(450+geser2, 0)
    glVertex2f(450+geser2, 20)
    glEnd()

def kotak3():
    global atas3,bawah3, geser3
    if geser3%(-450) == 0 :
        bawah3 = randrange(50, 300, 25)
        atas3 = bawah3 + 150
    e = 500+geser3
    f = e - 50
    if geser3 <= -450 :
        geser3 = 0
#BAGIAN ATAS
    glBegin(GL_POLYGON) #outline putih
    glColor3f(1, 1, 1)
    glVertex2f(f-1, 500)
    glVertex2f(f-1, atas3+4)
    glVertex2f(f+4, atas3+4)
    glVertex2f(f+4, atas3-1)
    glVertex2f(e-4, atas3-1)
    glVertex2f(e-4, atas3+4)
    glVertex2f(e+1, atas3+4)
    glVertex2f(e+1, 500)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex2f(f, 500)
    glVertex2f(f, atas3+5)
    glVertex2f(f+5, atas3+5)
    glVertex2f(f+5, atas3)
    glVertex2f(e-5, atas3)
    glVertex2f(e-5, atas3+5)
    glVertex2f(e, atas3+5)
    glVertex2f(e, 500)
    glEnd()
    #465 / 485
    jendela(465+geser3, atas3+25)
    jendela(485+geser3, atas3+25)
    jendela(465+geser3, atas3+55)
    jendela(485+geser3, atas3+85)
    jendela(485+geser3, atas3+115)
    jendela(485+geser3, atas3+145)
    jendela(465+geser3, atas3+145)
    jendela(465+geser3, atas3+175)
    jendela(465+geser3, atas3+205)
    jendela(485+geser3, atas3+205)
    jendela(465+geser3, atas3+235)
    glBegin(GL_QUADS) #garis item di atas
    glColor3f(0, 0, 0)
    glVertex2f(500+geser3, 480)
    glVertex2f(500+geser3, 500)
    glVertex2f(450+geser3, 500)
    glVertex2f(450+geser3, 480)
    glEnd()
#BAGIAN BAWAH
    glBegin(GL_POLYGON) #outline putih
    glColor3f(1, 1, 1)
    glVertex2f(f-1, 0)
    glVertex2f(f-1, bawah3-4)
    glVertex2f(f+4, bawah3+1)
    glVertex2f(e-4, bawah3+1)
    glVertex2f(e+1, bawah3-4)
    glVertex2f(e+1, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex2f(f, 0)
    glVertex2f(f, bawah3-5)
    glVertex2f(f+5, bawah3)
    glVertex2f(e-5, bawah3)
    glVertex2f(e, bawah3-5)
    glVertex2f(e, 0)
    glEnd()
    jendela(465+geser3, bawah3-35)
    jendela(485+geser3, bawah3-35)
    jendela(465+geser3, bawah3-65)
    jendela(485+geser3, bawah3-95)
    jendela(485+geser3, bawah3-125)
    jendela(485+geser3, bawah3-155)
    jendela(465+geser3, bawah3-155)
    jendela(465+geser3, bawah3-185)
    jendela(465+geser3, bawah3-215)
    jendela(485+geser3, bawah3-215)
    jendela(465+geser3, bawah3-245)
    glBegin(GL_QUADS) #garis item di bawah
    glColor3f(0, 0, 0)
    glVertex2f(500+geser3, 20)
    glVertex2f(500+geser3, 0)
    glVertex2f(450+geser3, 0)
    glVertex2f(450+geser3, 20)
    glEnd()

def karakter():
    # L : 100, R : 130
    # T : 275, B : 225
    # 30 x 50
    global naik
# B A D A N
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(245, 12, 12)
    glVertex2f(110, 275+naik) #E
    glVertex2f(120, 275+naik)
    glVertex2f(122, 271+naik)
    glVertex2f(122, 261+naik)
    glVertex2f(120, 257+naik)
    glVertex2f(124, 255+naik) #N
    glVertex2f(126, 245+naik)
    glVertex2f(124, 235+naik)
    glVertex2f(122, 235+naik)
    glVertex2f(122, 237+naik)
    glVertex2f(108, 237+naik)
    glVertex2f(108, 235+naik)
    glVertex2f(102, 235+naik)
    glVertex2f(100, 245+naik)
    glVertex2f(102, 253+naik)
    glVertex2f(104, 255+naik)
    glVertex2f(110, 257+naik)
    glVertex2f(104, 261+naik)
    glVertex2f(104, 271+naik)
    glEnd()
    badan = [[110, 275+naik],[120, 275+naik],[122, 271+naik],[122, 261+naik],[120, 257+naik],[124, 255+naik],
    [126, 245+naik],[124, 235+naik],[122, 235+naik],[122, 237+naik],[108, 237+naik],[108, 235+naik],
    [102, 235+naik],[100, 245+naik],[102, 253+naik],[104, 255+naik],[110, 257+naik],[104, 261+naik],[104, 271+naik]]
    drawLine(badan)
# K A K I
    glBegin(GL_POLYGON) 
    glColor3ub(245, 12, 12)
    glVertex2f(106, 237+naik)
    glVertex2f(106, 225+naik)
    glVertex2f(114, 225+naik)
    glVertex2f(114, 237+naik)
    glEnd()
    glBegin(GL_POLYGON) 
    glColor3ub(245, 12, 12)
    glVertex2f(116, 237+naik)
    glVertex2f(116, 225+naik)
    glVertex2f(122, 225+naik)
    glVertex2f(122, 237+naik)
    glEnd()
    kaki_kiri = [[106, 237+naik],[106, 225+naik],[114, 225+naik],[114, 237+naik]]
    kaki_kanan = [[116, 237+naik],[116, 225+naik],[122, 225+naik],[122, 237+naik]]
    drawLine(kaki_kiri)
    drawLine(kaki_kanan)
# M U K A
    glBegin(GL_POLYGON) 
    glColor3ub(255, 255, 166)
    glVertex2f(110, 273+naik) #W
    glVertex2f(114, 273+naik)
    glVertex2f(114, 271+naik)
    glVertex2f(118, 271+naik)
    glVertex2f(118, 273+naik)
    glVertex2f(120, 273+naik)
    glVertex2f(120, 271+naik)
    glVertex2f(122, 271+naik) #M1
    glVertex2f(122, 263+naik)
    glVertex2f(120, 259+naik)
    glVertex2f(110, 259+naik)
    glVertex2f(106, 263+naik)
    glVertex2f(106, 271+naik)
    glVertex2f(110, 271+naik)
    glEnd()
    garis([122, 263+naik],[120, 259+naik])
    garis([120, 259+naik],[110, 259+naik])
    garis([110, 259+naik],[106, 263+naik])
    garis([106, 263+naik],[106, 271+naik])
# M A T A
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(109, 269+naik) #H1
    glVertex2f(109, 267+naik)
    glVertex2f(114, 267+naik)
    glVertex2f(114, 269+naik)
    glEnd()
    mata_kiri = [[109, 269+naik],[109, 267+naik],[114, 267+naik], [114, 269+naik]]
    drawLine(mata_kiri)
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(116, 269+naik) #J1
    glVertex2f(116, 267+naik)
    glVertex2f(122, 267+naik)
    glVertex2f(122, 269+naik)
    glEnd()
    mata_kanan = [[116, 269+naik],[116, 267+naik],[122, 267+naik],[122, 269+naik]]
    drawLine(mata_kanan)
# L A M P U
    glBegin(GL_POLYGON) 
    glColor3ub(150, 140, 255)
    glVertex2f(112, 253+naik)
    glVertex2f(115, 249+naik)
    glVertex2f(118, 253+naik)
    glEnd()
    glPopMatrix()
    titik_lampu = [[112, 253+naik],[115, 249+naik],[118, 253+naik]]
    drawLine(titik_lampu)

def drawText (text, font, x, y, Red, Green, Blue) :
    glPushMatrix()
    glColor3ub(Red, Green, Blue)
    glRasterPos2i(x, y)
    for i in str(text) :
        c =  ord(i)
        glutBitmapCharacter(font, c)
    glPopMatrix()

def bg_color():
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glDisable(GL_LIGHTING)
    glBegin(GL_QUADS)
    glColor3ub(102, 102, 255) #18, 47, 80
    glVertex2f(-1.0,-1.0)
    glVertex2f(1.0,-1.0)
    glColor3ub(0, 0, 40) #
    glVertex2f(1.0, 1.0)
    glVertex2f(-1.0, 1.0)
    glEnd()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

    glBegin(GL_QUADS)   # menara tertinggi
    glColor3ub(47, 47, 168) #746, 46, 176
    glVertex2f(135, 0)
    glVertex2f(135, 180)
    glVertex2f(180, 180)
    glVertex2f(180, 0)
    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 128)
    glVertex2f(50, 0)
    glVertex2f(50, 100)
    glVertex2f(75, 100)
    glVertex2f(75, 0)
    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 160)
    glVertex2f(80, 0)
    glVertex2f(80, 140)
    glVertex2f(110, 150)
    glVertex2f(110, 0)
    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 130)
    glVertex2f(90, 0)
    glVertex2f(90, 120)
    glVertex2f(125, 120)
    glVertex2f(125, 0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(0, 0, 160)
    glVertex2f(195, 0)
    glVertex2f(195, 130)
    glVertex2f(155, 130)
    glVertex2f(155, 0)
    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 128)
    glVertex2f(130, 0)
    glVertex2f(130, 80)
    glVertex2f(170, 80)
    glVertex2f(170, 0)
    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(47, 47, 168)
    glVertex2f(195, 0)
    glVertex2f(195, 150)
    glVertex2f(235, 150)
    glVertex2f(235, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 168)
    glVertex2f(240, 0)
    glVertex2f(240, 110)
    glVertex2f(250, 120)
    glVertex2f(260, 120)
    glVertex2f(280, 110)
    glVertex2f(280, 0)
    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 130)
    glVertex2f(185, 0)
    glVertex2f(185, 65)
    glVertex2f(260, 65)
    glVertex2f(260, 0)
    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(47, 47, 168)
    glVertex2f(355, 0)
    glVertex2f(355, 165)
    glVertex2f(405, 165)
    glVertex2f(405, 0)
    glEnd()
    glBegin(GL_POLYGON)     # -- menara lancip
    glColor3ub(0, 0, 130)
    glVertex2f(380, 0)
    glVertex2f(380, 70)
    glVertex2f(390, 83)
    glVertex2f(400, 83)
    glVertex2f(410, 70)
    glVertex2f(410, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 130)
    glVertex2f(390, 83)
    glVertex2f(400, 83)
    glVertex2f(395, 120)
    glEnd()                 # -- menara lancip
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 160)
    glVertex2f(295, 0)
    glVertex2f(295, 115)
    glVertex2f(327, 115)
    glVertex2f(327, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 130)
    glVertex2f(270, 0)
    glVertex2f(270, 90)
    glVertex2f(275, 90)
    glVertex2f(275, 97)
    glVertex2f(300, 97)
    glVertex2f(300, 90)
    glVertex2f(310, 90)
    glVertex2f(310, 0)
    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 130)
    glVertex2f(330, 0)
    glVertex2f(330, 130)
    glVertex2f(370, 130)
    glVertex2f(370, 0)
    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 165)
    glVertex2f(430, 0)
    glVertex2f(430, 130)
    glVertex2f(450, 130)
    glVertex2f(450, 0)
    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 130)
    glVertex2f(415, 0)
    glVertex2f(415, 95)
    glVertex2f(448, 95)
    glVertex2f(448, 0)
    glEnd()

def score(value):
    global skor, moveStop
    if moveStop == False :
        skor += 1
        glutTimerFunc(2250, score, 10)

def timer(value):
    global geser, geser2, geser3, moveStop
    if not moveStop :
        geser -= 5
        geser2 -= 5
        geser3 -= 5
        glutTimerFunc(75, timer, 10)
    elif moveStop == True :
        geser -= 0
        geser2 -= 0
        geser3 -= 0

def gravitasi(value):
    global naik, game_over
    if not moveStop :
        naik -= 5
        glutTimerFunc(40, gravitasi, 10)
    elif moveStop == True :
        if game_over <= 300 :
            game_over += 5
            glutTimerFunc(20, gravitasi, 10)

def controller(key, x, y):
    global moveStop, naik,  skor
    if moveStop == False :
        if key == GLUT_KEY_UP:
            naik += 65
            # print("FLY")
    
def update(value):
    glutPostRedisplay()
    glutTimerFunc(10, update, 0)

def iterate():
    glViewport(0, 0, 400, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(50.0, 450, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global moveStop, naik, geser, geser2, geser3, atas, bawah, atas2, bawah2, atas3, bawah3, skor, game_over
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    bg_color()
    bg.moon(150, 400, 55, 100)
    bg.MoonLight(150, 400, 57, 100)
    kotak()
    kotak2() 
    kotak3()  
    karakter()
    drawText("SCORE", font2, 70, 475, 255, 255, 255)
    drawText(skor, font1, 75, 450, 255, 255, 255)

    if naik >= 225 or naik <= -225:
        moveStop = True
    if moveStop == False :
        if geser <= -320 and geser >= -400 :
            if (275+naik) >= atas or (225+naik) <= bawah :
                moveStop = True
        elif geser2 <= -320 and geser2 >= -400 :
            if (275+naik) >= atas2 or (225+naik) <= bawah2 :
                moveStop = True
        elif geser3 <= -320 and geser3 >= -400 :
            if (275+naik) >= atas3 or (225+naik) <= bawah3 :
                moveStop = True
    elif moveStop == True :
        naik += 0
        skor += 0
        drawText("YOU LOSE", font1, 200, (-50+game_over), 255, 255, 255)
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(400, 500)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("Flying IronMan")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutSpecialFunc(controller)
    glutTimerFunc(6000, score, 10)
    update(0)
    gravitasi(0)
    timer(0)
    glutMainLoop()
main()
