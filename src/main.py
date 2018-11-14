from OpenGL.GL import *
from OpenGL.GLU import *

import threading

import pygame
from pygame.locals import *

import dilation

titik2D = []

def DrawOrigin2D():
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2fv([500, 0])
    glVertex2fv([-500, 0])
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
    glColor3f(1, 0, 0)
    glBegin(GL_POLYGON)

    for point in points:
        glVertex2fv(point)

    glEnd()

def InputHandler2D():
    global titik2D

    user_input = ''
    user_input_Arr = user_input.split()
    while not user_input == 'quit':
        user_input = input('Input: ')
        user_input_Arr = user_input.split()
        if user_input_Arr[0] == 'dilate':
            titik2D = dilation.dilate_2d(titik2D, float(user_input_Arr[1]))


def main():
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

        input_thread = threading.Thread(target = InputHandler2D)
        input_thread.start()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            DrawOrigin2D()
            Draw2D(titik2D)
            pygame.display.flip()
    elif program_mode == '3D':
        pygame.init()
        display = (800, 600)
        
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            DrawOrigin3D()
            pygame.display.flip()


main()