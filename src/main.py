from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import threading
import random

import pygame
from pygame.locals import *

import dilation
import reflect
import rotate
import translate

titik2D = []
target2D = []


#PERHATIKAN URUTAN
titik3D = [
    [-1, -1, 1],
    [-1, -1, -1],
    [1, -1, -1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1],
    [-1, 1, -1],
    [1, 1, -1]
]

faces = [
    
    [0, 1, 2, 3],

    [2, 3, 4, 7],

    [1, 2, 7, 6],

    [3, 0, 5, 4],

    [0, 1, 6, 5],

    [4, 5, 6, 7],
]

quit_state = False
program_mode = ''
in_animation = False

deltaTime = 0
tolerance = 0.01
speed = 3 #PX / S

def DrawOrigin2D():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex2fv([500, 0])
    glVertex2fv([-500, 0])
    glColor3f(0, 1, 0)
    glVertex2fv([0, 500])
    glVertex2fv([0, -500])
    glEnd()

def DrawOrigin3D():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3fv([500, 0, 0])
    glVertex3fv([-500, 0, 0])
    glColor3f(0, 1, 0)
    glVertex3fv([0, 500, 0])
    glVertex3fv([0, -500, 0])
    glColor3f(0, 0, 1)
    glVertex3fv([0, 0, 500])
    glVertex3fv([0, 0, -500])
    glEnd()

def Draw2D(points):
    glColor3f(1, 0, 1)
    glBegin(GL_POLYGON)

    for point in points:
        glVertex2fv(point)

    glEnd()

def Draw3D():

    faceNum = 1

    for face in faces:
        glBegin(GL_POLYGON)
        if faceNum == 1:
            glColor3f(0, 1, 0)
        elif faceNum == 2:
            glColor3f(1, 0, 0)
        elif faceNum == 3:
            glColor3f(0, 0, 1)
        elif faceNum == 4:
            glColor3f(1, 0, 1)
        elif faceNum == 5:
            glColor3f(1, 1, 0)
        elif faceNum == 6:
            glColor3f(0, 1, 1)
        glVertex3fv(titik3D[face[0]])
        glVertex3fv(titik3D[face[1]])
        glVertex3fv(titik3D[face[2]])
        glVertex3fv(titik3D[face[3]])
        glEnd()
        faceNum += 1

def Animate2D(currentPoints, targetPoints):
    global in_animation
    oldPoints = currentPoints.copy()

    maxDistance = 0

    for cI, cPoint in enumerate(currentPoints):
        if ((((cPoint[0] - targetPoints[cI][0]) ** 2) + ((cPoint[1] - targetPoints[cI][1]) ** 2)) ** (1.00 / 2)) > maxDistance:
            maxDistance = ((((cPoint[0] - targetPoints[cI][0]) ** 2) + ((cPoint[1] - targetPoints[cI][1]) ** 2)) ** (1.00 / 2))

    for cI, cPoint in enumerate(currentPoints):
        if maxDistance > 0 :
            Animation2D(cPoint, targetPoints[cI], oldPoints[cI], maxDistance)


def Animation2D(currentPoint, targetPoint, oldPoint, maxDistance):
    global in_animation
    global deltaTime

    directionVector = [
        targetPoint[0] - oldPoint[0],
        targetPoint[1] - oldPoint[1],
    ]

    length = ((directionVector[0] ** 2) + (directionVector[1] ** 2)) ** (1.0 / 2)

    if length > 0 :
        directionVector = [
            directionVector[0] / maxDistance,
            directionVector[1] / maxDistance
        ]

        length_vector = [
            targetPoint[0] - currentPoint[0],
            targetPoint[1] - currentPoint[1],
        ]

        xFlag = abs(length_vector[0]) <= tolerance
        yFlag = abs(length_vector[1]) <= tolerance

        if xFlag:
            currentPoint[0] = targetPoint[0]
        else:
            currentPoint[0] += directionVector[0] * (float(speed) * deltaTime)

        if yFlag:
            currentPoint[1] = targetPoint[1]
        else:
            currentPoint[1] += directionVector[1] * (float(speed) * deltaTime)
    
def InputHandler2D():
    global quit_state
    global titik2D
    global target2D

    user_input = ''
    user_input_Arr = user_input.split()
    while not user_input == 'quit':
        user_input = input('Input: ')
        user_input_Arr = user_input.split()
        if user_input_Arr[0] == 'dilate':
            target2D = dilation.dilate_2d(titik2D, float(user_input_Arr[1]))
        elif user_input_Arr[0] == 'reflect':
            if user_input_Arr[1] == 'y=x':
                target2D = reflect.reflect_2d_xy_normal(titik2D)
            elif user_input_Arr[1] == 'y=-x':
                target2D = reflect.reflect_2d_xy_invert(titik2D)
            elif user_input_Arr[1] == 'x':
                target2D = reflect.reflect_2d_x(titik2D)
            elif user_input_Arr[1] == 'y':
                target2D = reflect.reflect_2d_y(titik2D)
            else:
                target2D = reflect.reflect_2d(titik2D, float(user_input_Arr[1]), float(user_input_Arr[2]))
        elif user_input_Arr[0] == 'rotate' :
            target2D = rotate.rotate_2d(titik2D, float(user_input_Arr[1]), float(user_input_Arr[2]), float(user_input_Arr[3]))
        elif user_input_Arr[0] == 'translate':
            target2D = translate.translate_2d(titik2D, float(user_input_Arr[1]), float(user_input_Arr[2]))

    quit_state = True

def InputHandler3D():
    global quit_state
    global titik3D

    user_input = ''
    user_input_Arr = user_input.split()
    while not user_input == 'quit':
        user_input = input('Input: ')
        user_input_Arr = user_input.split()
        if user_input_Arr[0] == 'dilate':
            titik3D = dilation.dilate_3d(titik2D, float(user_input_Arr[1]))
        elif user_input_Arr[0] == 'rotate' :
            titik3D = rotate.rotate_3d(titik2D, float(user_input_Arr[1]), float(user_input_Arr[2]), float(user_input_Arr[3]), float(user_input_Arr[4]))
        elif user_input_Arr[0] == 'translate':
            titik3D = translate.translate_3d(titik3D, float(user_input_Arr[1]), float(user_input_Arr[2]), float(user_input_Arr[3]))
            

    quit_state = True

def main():
    global quit_state
    global program_mode
    global deltaTime

    global titik2D
    global target2D
    global in_animation

    program_mode = input('2D / 3D: ')
    jumlah_titik = 0

    while program_mode != '2D' and program_mode != '3D':
        print('Input tidak valid!')
        program_mode = input('2D / 3D: ')

    if program_mode == '2D':

        jumlah_titik = int(input('Jumlah titik: '))
        
        for i in range(0, jumlah_titik):
            input_x, input_y = input().split()
            input_x = float(input_x)
            input_y = float(input_y)
            titik2D.append([input_x, input_y])

        target2D = titik2D
            
        pygame.init()
        display = (800, 600)

        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        glClearColor(0.5, 0.5, 0.5, 1)

        input_thread = threading.Thread(target = InputHandler2D)
        input_thread.start()

        xMin = -10
        xMax = 10
        yMin = -10
        yMax = 10
        zMin = -500
        zMax = 500

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(xMin, xMax, yMin, yMax, 500, -500)
        glMatrixMode(GL_MODELVIEW)

        oldTime = glutGet(GLUT_ELAPSED_TIME)

        while not quit_state:
            #SET DELTA TIME
            currentTime = glutGet(GLUT_ELAPSED_TIME)
            deltaTime = (currentTime - oldTime) / 1000
            oldTime = glutGet(GLUT_ELAPSED_TIME)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_state = True
                    pygame.quit()
                    quit()
            
            if (pygame.key.get_pressed()[K_LEFT]):
                glTranslatef((xMax - xMin) / 100, 0, 0)
            elif (pygame.key.get_pressed()[K_RIGHT]):
                glTranslatef(-(xMax - xMin) / 100, 0, 0)

            if (pygame.key.get_pressed()[K_UP]):
                glTranslatef(0, -(yMax - yMin) / 100, 0)
            elif (pygame.key.get_pressed()[K_DOWN]):
                glTranslatef(0, (yMax - yMin) / 100, 0)

            if(pygame.key.get_pressed()[K_x]):
                glMatrixMode(GL_PROJECTION)
                if (xMin > -600):
                    xMin -= 1 / 10
                    xMax += 1 / 10
                    yMin -= 1 / 10
                    yMax += 1 / 10
                glLoadIdentity()
                glOrtho(xMin, xMax, yMin, yMax, 500, -500)
                glMatrixMode(GL_MODELVIEW)
            elif(pygame.key.get_pressed()[K_z]):
                glMatrixMode(GL_PROJECTION)
                if (xMin < -1):
                    xMin += 1 / 10
                    xMax -= 1 / 10
                    yMin += 1 / 10
                    yMax -= 1 / 10
                glLoadIdentity()
                glOrtho(xMin, xMax, yMin, yMax, 500, -500)
                glMatrixMode(GL_MODELVIEW)
                
            
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            DrawOrigin2D()

            #print(deltaTime)
            #titik2D[0][0] += speed * deltaTime

            in_animation = not (titik2D == target2D)

            if (in_animation):
                Animate2D(titik2D, target2D)

            Draw2D(titik2D)
            pygame.display.flip()
                
    elif program_mode == '3D':
        oldTime = 0
        pygame.init()
        display = (800, 600)
        
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        glClearColor(0.5, 0.5, 0.5, 1)

        input_thread = threading.Thread(target = InputHandler3D)
        input_thread.start()

        xMin = -10
        xMax = 10
        yMin = -10
        yMax = 10
        zMin = -500
        zMax = 500

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(xMin, xMax, yMin, yMax, -500, 500)
        glMatrixMode(GL_MODELVIEW)

        gluPerspective(0, display[0]/display[1], 0.01, 50)

        glEnable(GL_DEPTH_TEST)

        while not quit_state:
            #SET DELTA TIME
            currentTime = glutGet(GLUT_ELAPSED_TIME)
            deltaTime = (currentTime - oldTime) / 1000
            oldTime = glutGet(GLUT_ELAPSED_TIME)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_state = True
                    pygame.quit()
                    quit()

            if (pygame.key.get_pressed()[K_LEFT]):
                glTranslatef((xMax - xMin) / 100, 0, 0)
            elif (pygame.key.get_pressed()[K_RIGHT]):
                glTranslatef(-(xMax - xMin) / 100, 0, 0)

            if (pygame.key.get_pressed()[K_UP]):
                glTranslatef(0, -(yMax - yMin) / 100, 0)
            elif (pygame.key.get_pressed()[K_DOWN]):
                glTranslatef(0, (yMax - yMin) / 100, 0)

            if (pygame.key.get_pressed()[K_a]):
                glRotatef(1, 0, 1, 0)
            elif (pygame.key.get_pressed()[K_d]):
                glRotatef(-1, 0, 1, 0)
            elif (pygame.key.get_pressed()[K_w]):
                glRotatef(1, 1, 0, 0)
            elif (pygame.key.get_pressed()[K_s]):
                glRotatef(-1, 1, 0, 0)

            if(pygame.key.get_pressed()[K_x]):
                glMatrixMode(GL_PROJECTION)
                if (xMin > -600):
                    xMin -= 1 / 10
                    xMax += 1 / 10
                    yMin -= 1 / 10
                    yMax += 1 / 10
                glLoadIdentity()
                glOrtho(xMin, xMax, yMin, yMax, -500, 500)
                glMatrixMode(GL_MODELVIEW)
            elif(pygame.key.get_pressed()[K_z]):
                glMatrixMode(GL_PROJECTION)
                if (xMin < -1):
                    xMin += 1 / 10
                    xMax -= 1 / 10
                    yMin += 1 / 10
                    yMax -= 1 / 10
                glLoadIdentity()
                glOrtho(xMin, xMax, yMin, yMax, -500, 500)
                glMatrixMode(GL_MODELVIEW)

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            DrawOrigin3D()
            Draw3D()

            pygame.display.flip()

main()