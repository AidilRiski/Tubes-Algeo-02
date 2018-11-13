from OpenGL.GL import *
from OpenGL.GLU import *

import sys

import pygame
from pygame.locals import *

def DrawOrigin2D():
    glBegin(GL_LINES)
    glVertex2fv([500, 0])
    glVertex2fv([-500, 0])
    glVertex2fv([0, 500])
    glVertex2fv([0, -500])
    glEnd()

def DrawOrigin3D():
    glBegin(GL_LINES)
    glVertex3fv([500, 0, 0])
    glVertex3fv([-500, 0, 0])
    glVertex3fv([0, 500, 0])
    glVertex3fv([0, -500, 0])
    glVertex3fv([0, 0, 500])
    glVertex3fv([0, 0, -500])
    glEnd()

def main():
    program_mode = input('2D / 3D: ')

    while program_mode != '2D' and program_mode != '3D':
        print('Input tidak valid!')
        program_mode = input('2D / 3D: ')

    if program_mode == '2D':
        pygame.init()
        display = (800, 600)

        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        console_input = ''

        while not console_input == 'QUIT':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            DrawOrigin2D()
            pygame.display.flip()
            console_input = input()
    elif program_mode == '3D':
        pygame.init()
        display = (800, 600)
        
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        glTranslatef(0.0, 0.0, 0.0)
        
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            DrawOrigin3D()
            pygame.display.flip()


main()