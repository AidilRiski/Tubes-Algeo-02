from OpenGL.GL import *
from OpenGL.GLU import *

import threading

import pygame
from pygame.locals import *

import dilation

titik2D = []

quit_state = False

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
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex3fv([500, 0, 0])
    glVertex3fv([-500, 0, 0])
    glVertex3fv([0, 500, 0])
    glVertex3fv([0, -500, 0])
    glVertex3fv([0, 0, 500])
    glVertex3fv([0, 0, -500])
    glEnd()

def Draw2D(points):
    glColor3f(1, 0, 1)
    glBegin(GL_POLYGON)

    for point in points:
        glVertex2fv(point)

    glEnd()

def InputHandler2D():
    global quit_state
    global titik2D

    user_input = ''
    user_input_Arr = user_input.split()
    while not user_input == 'quit':
        user_input = input('Input: ')
        user_input_Arr = user_input.split()
        if user_input_Arr[0] == 'dilate':
            titik2D = dilation.dilate_2d(titik2D, float(user_input_Arr[1]))

    quit_state = True

def main():
    global quit_state

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
        glOrtho(xMin, xMax, yMin, yMax, 1, -1)
        glMatrixMode(GL_MODELVIEW)

        while not quit_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_state = True
                    pygame.quit()
                    quit()
            if (pygame.key.get_pressed()[K_LEFT]):
                glTranslatef(0.0001, 0, 0)
            elif(pygame.key.get_pressed()[K_RIGHT]):
                glTranslatef(-0.0001, 0, 0)

            if(pygame.key.get_pressed()[K_UP]):
                glTranslatef(0, -0.0001, 0)
            elif(pygame.key.get_pressed()[K_DOWN]):
                glTranslatef(0, 0.0001, 0)

            if(pygame.key.get_pressed()[K_x]):
                glMatrixMode(GL_PROJECTION)
                if (xMin > -600):
                    xMin -= 1 / 10
                    xMax += 1 / 10
                    yMin -= 1 / 10
                    yMax += 1 / 10
                glLoadIdentity()
                glOrtho(xMin, xMax, yMin, yMax, 1, -1)
                glMatrixMode(GL_MODELVIEW)
            elif(pygame.key.get_pressed()[K_z]):
                glMatrixMode(GL_PROJECTION)
                if (xMin < -1):
                    xMin += 1 / 10
                    xMax -= 1 / 10
                    yMin += 1 / 10
                    yMax -= 1 / 10
                glLoadIdentity()
                glOrtho(xMin, xMax, yMin, yMax, 1, -1)
                glMatrixMode(GL_MODELVIEW)
                
            
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            DrawOrigin2D()
            Draw2D(titik2D)
            pygame.display.flip()
                
    elif program_mode == '3D':
        pygame.init()
        display = (800, 600)
        
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        
        while not quit_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_state = True
                    pygame.quit()
                    quit()
        
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            DrawOrigin3D()
            pygame.display.flip()

main()