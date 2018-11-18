import os

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
import shear
import stretch
import custom

titik2D = []
target2D = []
titik2DInitial = []


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

target3D = []
titik3DInitial = []

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
speed = 5 #PX / S
rotation_speed = 45 #DG / S

is_rotation = False
rotation_point2d = []
rotation_point3d = []

def DrawOrigin2D():
    glPushAttrib(GL_ENABLE_BIT)

    glLineStipple(1, 10)
    glEnable(GL_LINE_STIPPLE)

    glBegin(GL_LINES)

    glColor3f(1, 0, 0)
    glVertex2fv([-500, 0])
    glVertex2fv([0, 0])

    glColor3f(0, 1, 0)
    glVertex2fv([0, -500])
    glVertex2fv([0, 0])

    glEnd()

    glPopAttrib()

    glBegin(GL_LINES)

    glColor3f(1, 0, 0)
    glVertex2fv([500, 0])
    glVertex2fv([0, 0])

    glColor3f(0, 1, 0)
    glVertex2fv([0, 500])
    glVertex2fv([0, 0])

    glEnd()

def DrawOrigin3D():

    glPushAttrib(GL_ENABLE_BIT)

    glLineStipple(1, 10)
    glEnable(GL_LINE_STIPPLE)

    glBegin(GL_LINES)

    glColor3f(1, 0, 0)
    glVertex3fv([-500, 0, 0])
    glVertex3fv([0, 0, 0])

    glColor3f(0, 1, 0)
    glVertex3fv([0, -500, 0])
    glVertex3fv([0, 0, 0])

    glColor3f(0, 0, 1)
    glVertex3fv([0, 0, -500])
    glVertex3fv([0, 0, 0])

    glEnd()

    glPopAttrib()

    glBegin(GL_LINES)

    glColor3f(1, 0, 0)
    glVertex3fv([500, 0, 0])
    glVertex3fv([0, 0, 0])

    glColor3f(0, 1, 0)
    glVertex3fv([0, 500, 0])
    glVertex3fv([0, 0, 0])

    glColor3f(0, 0, 1)
    glVertex3fv([0, 0, 500])
    glVertex3fv([0, 0, 0])

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
    global rotation_point2d

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

def AnimationRotational2D(currentPoints, targetPoints, rotation_point):
    global in_animation
    global deltaTime

    global titik2D

    global is_rotation
    global rotation_speed
    global rotation_point2d

    p_sum = 0

    for cI, cPoint in enumerate(currentPoints):
      p_sum += abs(cPoint[0] - targetPoints[cI][0]) + abs(cPoint[1] - targetPoints[cI][1])

    rFlag = p_sum <= ((tolerance * 2) * len(currentPoints))

    if not rFlag :
        currentPoints = rotate.rotate_2d(currentPoints, float(rotation_speed) * deltaTime, rotation_point2d[0], rotation_point2d[1])
    else :
        currentPoints = targetPoints
        is_rotation = False

    return currentPoints

def Animate3D(currentPoints, targetPoints):
    global in_animation
    global rotation_point3d

    oldPoints = currentPoints.copy()
    
    maxDistance = 0

    for cI, cPoint in enumerate(currentPoints):
        if (((cPoint[0] - targetPoints[cI][0]) ** 2) + ((cPoint[1] - targetPoints[cI][1]) ** 2) + ((cPoint[2] - targetPoints[cI][2]) ** 2)) ** (1.00 / 2) > maxDistance:
            maxDistance = (((cPoint[0] - targetPoints[cI][0]) ** 2) + ((cPoint[1] - targetPoints[cI][1]) ** 2) + ((cPoint[2] - targetPoints[cI][2]) ** 2)) ** (1.00 / 2)
    
    for cI, cPoint in enumerate(currentPoints):
        if maxDistance > 0 :
            Animation3D(cPoint, targetPoints[cI], oldPoints[cI], maxDistance)

def Animation3D(currentPoint, targetPoint, oldPoint, maxDistance):
    global in_animation
    global deltaTime

    directionVector = [
        targetPoint[0] - oldPoint[0],
        targetPoint[1] - oldPoint[1],
        targetPoint[2] - oldPoint[2],
    ]

    length = ((directionVector[0] ** 2) + (directionVector[1] ** 2) + (directionVector[2] ** 2)) ** (1.0 / 2)

    if length > 0 :
        directionVector = [
            directionVector[0] / maxDistance,
            directionVector[1] / maxDistance,
            directionVector[2] / maxDistance
        ]

        length_vector = [
            targetPoint[0] - currentPoint[0],
            targetPoint[1] - currentPoint[1],
            targetPoint[2] - currentPoint[2]
        ]

        xFlag = abs(length_vector[0]) <= tolerance
        yFlag = abs(length_vector[1]) <= tolerance
        zFlag = abs(length_vector[2]) <= tolerance

        if xFlag:
            currentPoint[0] = targetPoint[0]
        else:
            currentPoint[0] += directionVector[0] * (float(speed) * deltaTime)

        if yFlag:
            currentPoint[1] = targetPoint[1]
        else:
            currentPoint[1] += directionVector[1] * (float(speed) * deltaTime)

        if zFlag:
            currentPoint[2] = targetPoint[2]
        else:
            currentPoint[2] += directionVector[2] * (float(speed) * deltaTime)

def AnimationRotational3D(currentPoints, targetPoints, rotation_point):
    global in_animation
    global deltaTime

    global titik3D

    global is_rotation
    global rotation_speed
    global rotation_point3d

    p_sum = 0

    for cI, cPoint in enumerate(currentPoints):
      p_sum += abs(cPoint[0] - targetPoints[cI][0]) + abs(cPoint[1] - targetPoints[cI][1]) + abs(cPoint[2] - targetPoints[cI][2])

    rFlag = p_sum <= ((tolerance * 3) * len(currentPoints))

    if not rFlag :
        currentPoints = rotate.rotate_3d(currentPoints, float(rotation_speed) * deltaTime, rotation_point2d[0], rotation_point2d[1], rotation_point2d[2])
    else :
        currentPoints = targetPoints
        is_rotation = False

    return currentPoints
    
def InputHandler2D():
    global titik2D
    global target2D
    global titik2DInitial

    global is_rotation
    global rotation_point2d

    global quit_state
    
    user_input = ''
    while not user_input == 'exit':
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
            rotation_point2d = [float(user_input_Arr[2]), float(user_input_Arr[3])]
            is_rotation = True
        elif user_input_Arr[0] == 'translate':
            target2D = translate.translate_2d(titik2D, float(user_input_Arr[1]), float(user_input_Arr[2]))
        elif user_input_Arr[0] == 'shear':
            if user_input_Arr[1] == 'x':
                target2D = shear.shear_2d_x(titik2D, float(user_input_Arr[2]))
            elif user_input_Arr[1] == 'y':
                target2D = shear.shear_2d_y(titik2D, float(user_input_Arr[2]))
        elif user_input_Arr[0] == 'stretch':
            if user_input_Arr[1] == 'x':
                target2D = stretch.stretch_2d_x(titik2D, float(user_input_Arr[2]))
            elif user_input_Arr[1] == 'y':
                target2D = stretch.stretch_2d_y(titik2D, float(user_input_Arr[2]))
        elif user_input_Arr[0] == 'custom':
            target2D = custom.custom_2d(
                titik2D,
                float(user_input_Arr[1]), float(user_input_Arr[2]),
                float(user_input_Arr[3]), float(user_input_Arr[4])
            )
        elif user_input_Arr[0] == 'reset':
            target2D = titik2DInitial.copy()
        elif user_input_Arr[0] == 'multiple':
            command_array = []
            n = int(input('Jumlah Perintah: '))
            for i in range(0, n):
                command = input('Perintah: ')
                command_array.append(command)
            target2D = CommandHandler2D(command_array)
        elif user_input_Arr[0] == 'exit':
            pass
        else:
            print('Perintah tidak valid!')
        
    quit_state = True

def CommandHandler2D(command_list):
    global titik2D

    newMatrix = titik2D

    for command in command_list:
        user_input_Arr = command.split()
        if user_input_Arr[0] == 'dilate':
            newMatrix = dilation.dilate_2d(newMatrix, float(user_input_Arr[1]))
        elif user_input_Arr[0] == 'reflect':
            if user_input_Arr[1] == 'y=x':
                newMatrix = reflect.reflect_2d_xy_normal(newMatrix)
            elif user_input_Arr[1] == 'y=-x':
                newMatrix = reflect.reflect_2d_xy_invert(newMatrix)
            elif user_input_Arr[1] == 'x':
                newMatrix = reflect.reflect_2d_x(newMatrix)
            elif user_input_Arr[1] == 'y':
                newMatrix = reflect.reflect_2d_y(newMatrix)
            else:
                newMatrix = reflect.reflect_2d(newMatrix, float(user_input_Arr[1]), float(user_input_Arr[2]))
        elif user_input_Arr[0] == 'rotate' :
            newMatrix = rotate.rotate_2d(newMatrix, float(user_input_Arr[1]), float(user_input_Arr[2]), float(user_input_Arr[3]))
        elif user_input_Arr[0] == 'translate':
            newMatrix = translate.translate_2d(newMatrix, float(user_input_Arr[1]), float(user_input_Arr[2]))
        elif user_input_Arr[0] == 'shear':
            if user_input_Arr[1] == 'x':
                newMatrix = shear.shear_2d_x(newMatrix, float(user_input_Arr[2]))
            elif user_input_Arr[1] == 'y':
                newMatrix = shear.shear_2d_y(newMatrix, float(user_input_Arr[2]))
        elif user_input_Arr[0] == 'stretch':
            if user_input_Arr[1] == 'x':
                newMatrix = stretch.stretch_2d_x(newMatrix, float(user_input_Arr[2]))
            elif user_input_Arr[1] == 'y':
                newMatrix = stretch.stretch_2d_y(newMatrix, float(user_input_Arr[2]))
        elif user_input_Arr[0] == 'custom':
            newMatrix = custom.custom_2d(
                newMatrix,
                float(user_input_Arr[1]), float(user_input_Arr[2]),
                float(user_input_Arr[3]), float(user_input_Arr[4])
            )
        else:
            print('Perintah tidak valid!')
    
    return newMatrix

def InputHandler3D():
    global quit_state
    global titik3D
    global target3D
    global titik3DInitial

    global is_rotation
    global rotation_point3d

    user_input = ''
    user_input_Arr = user_input.split()
    while not user_input == 'exit':
        user_input = input('Input: ')
        user_input_Arr = user_input.split()
        if user_input_Arr[0] == 'dilate':
            target3D = dilation.dilate_3d(titik3D, float(user_input_Arr[1]))
        elif user_input_Arr[0] == 'rotate' :
            titik3D = rotate.rotate_3d(titik3D, float(user_input_Arr[1]), float(user_input_Arr[2]), float(user_input_Arr[3]), float(user_input_Arr[4]))
            rotation_point3d = [float(user_input_Arr[2]), float(user_input_Arr[3]), float(user_input_Arr[4])]
            is_rotation = True
        elif user_input_Arr[0] == 'translate':
            target3D = translate.translate_3d(titik3D, float(user_input_Arr[1]), float(user_input_Arr[2]), float(user_input_Arr[3]))
        elif user_input_Arr[0] == 'reflect':
            if user_input_Arr[1] == 'x':
                target3D = reflect.reflect_3d_x(titik3D)
            elif user_input_Arr[1] == 'y':
                target3D = reflect.reflect_3d_y(titik3D)
            elif user_input_Arr[1] == 'z':
                target3D = reflect.reflect_3d_z(titik3D)
        elif user_input_Arr[0] == 'shear':
            if user_input_Arr[1] == 'x':
                target3D = shear.shear_3d_x(titik3D, float(user_input_Arr[2]))
            elif user_input_Arr[1] == 'y':
                target3D = shear.shear_3d_y(titik3D, float(user_input_Arr[2]))
            elif user_input_Arr[1] == 'z':
                target3D = shear.shear_3d_z(titik3D, float(user_input_Arr[2]))
        elif user_input_Arr[0] == 'stretch':
            if user_input_Arr[1] == 'x':
                target3D = stretch.stretch_3d_x(titik3D, float(user_input_Arr[2]))
            elif user_input_Arr[1] == 'y':
                target3D = stretch.stretch_3d_y(titik3D, float(user_input_Arr[2]))
            elif user_input_Arr[1] == 'z':
                target3D = stretch.stretch_3d_z(titik3D, float(user_input_Arr[2]))
        elif user_input_Arr[0] == 'custom':
            target3D = custom.custom_3d(
                titik3D,
                float(user_input_Arr[1]), float(user_input_Arr[2]), float(user_input_Arr[3]),
                float(user_input_Arr[4]), float(user_input_Arr[5]), float(user_input_Arr[6]),
                float(user_input_Arr[7]), float(user_input_Arr[8]), float(user_input_Arr[9])
            )
        elif user_input_Arr[0] == 'reset':
            target3D = titik3DInitial.copy()
        elif user_input_Arr[0] == 'multiple':
            command_array = []
            n = int(input('Jumlah Perintah: '))
            for i in range(0, n):
                command = input('Perintah: ')
                command_array.append(command)
            target3D = CommandHandler3D(command_array)
        elif user_input_Arr[0] == 'exit':
            pass
        else:
            print('Perintah tidak valid!')
            
    quit_state = True

def CommandHandler3D(command_list):
    global titik3D

    newMatrix = titik3D

    for command in command_list:
        user_input_Arr = command.split()
        if user_input_Arr[0] == 'dilate':
            newMatrix = dilation.dilate_3d(newMatrix, float(user_input_Arr[1]))
        elif user_input_Arr[0] == 'rotate' :
            newMatrix = rotate.rotate_3d(newMatrix, float(user_input_Arr[1]), float(user_input_Arr[2]), float(user_input_Arr[3]), float(user_input_Arr[4]))
        elif user_input_Arr[0] == 'translate':
            newMatrix = translate.translate_3d(newMatrix, float(user_input_Arr[1]), float(user_input_Arr[2]), float(user_input_Arr[3]))
        elif user_input_Arr[0] == 'reflect':
            if user_input_Arr[1] == 'x':
                newMatrix = reflect.reflect_3d_x(newMatrix)
            elif user_input_Arr[1] == 'y':
                newMatrix = reflect.reflect_3d_y(newMatrix)
            elif user_input_Arr[1] == 'z':
                newMatrix = reflect.reflect_3d_z(newMatrix)
        elif user_input_Arr[0] == 'shear':
            if user_input_Arr[1] == 'x':
                newMatrix = shear.shear_3d_x(newMatrix, float(user_input_Arr[2]))
            elif user_input_Arr[1] == 'y':
                newMatrix = shear.shear_3d_y(newMatrix, float(user_input_Arr[2]))
            elif user_input_Arr[1] == 'z':
                newMatrix = shear.shear_3d_z(newMatrix, float(user_input_Arr[2]))
        elif user_input_Arr[0] == 'stretch':
            if user_input_Arr[1] == 'x':
                newMatrix = stretch.stretch_3d_x(newMatrix, float(user_input_Arr[2]))
            elif user_input_Arr[1] == 'y':
                newMatrix = stretch.stretch_3d_y(newMatrix, float(user_input_Arr[2]))
            elif user_input_Arr[1] == 'z':
                newMatrix = stretch.stretch_3d_z(newMatrix, float(user_input_Arr[2]))
        elif user_input_Arr[0] == 'custom':
            newMatrix = custom.custom_3d(
                newMatrix,
                float(user_input_Arr[1]), float(user_input_Arr[2]), float(user_input_Arr[3]),
                float(user_input_Arr[4]), float(user_input_Arr[5]), float(user_input_Arr[6]),
                float(user_input_Arr[7]), float(user_input_Arr[8]), float(user_input_Arr[9])
            )
        else:
            print('Perintah tidak valid!')
    
    return newMatrix

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    global quit_state
    global program_mode
    global deltaTime

    global titik2D
    global target2D
    global titik2DInitial

    global titik3D
    global target3D
    global titik3DInitial

    global in_animation
    global is_rotation

    cls()

    print("  ________  ___________   _____    ____  ___________ ___    ____                                   ")
    print(" /_  __/ / / / ____/   | / ___/   / __ )/ ____/ ___//   |  / __ \                                  ")
    print("  / / / / / / / __/ /| | \__ \   / __  / __/  \__ \/ /| | / /_/ /                                  ")
    print(" / / / /_/ / /_/ / ___ |___/ /  / /_/ / /___ ___/ / ___ |/ _, _/                                   ")
    print("/_/ _\\\\___/\\\\___/_/  \\\\\\\\\\__/ _\\\\\\__\\\\\\____\\\\\\\\__/_/__\\\\\\\\\\_\\\\\\_____  __  ___________________  ____")
    print("   /   |  / /       / /   |  / __ )/   |  / __ \   / ____/ ____/ __ \/  |/  / ____/_  __/ __ \/  _/")
    print("  / /| | / /   __  / / /| | / __  / /| | / /_/ /  / / __/ __/ / / / / /|_/ / __/   / / / /_/ // /  ")
    print(" / ___ |/ /___/ /_/ / ___ |/ /_/ / ___ |/ _, _/  / /_/ / /___/ /_/ / /  / / /___  / / / _, _// /   ")
    print("/_/  |_/_____/\____/_/  |_/_____/_/  |_/_/ |_|   \____/_____/\____/_/  /_/_____/ /_/ /_/ |_/___/   ")
    print("                                                                                                   ")
    print('#=================================================================================================#')
    print('#	Tugas Besar - Aljabar Geometri								  #')
    print('#	"Simulasi Transformasi Linier pada Bidang 2D dan 3D dengan Menggunakan OpenGL API"	  #')
    print('#												  #')
    print('#	Bahasa Pemrograman yang digunakan: Python						  #')
    print('#-------------------------------------------------------------------------------------------------#')
    print('#	Anggota Kelompok:									  #')
    print('#												  #')
    print('#	Abda Shaffan Diva	-	13517021						  #')
    print('#	Aidil Rezjki S		-	13517070						  #')
    print('#	Taufikurrahman Anwar	-	13517074						  #')
    print('#=================================================================================================#')
    print('#	Kontrol Kamera										  #')
    print('#												  #')
    print('#		1. W, S		:	Rotasi kamera terhadap sumbu x.	(Hanya pada mode 3D).	  #')
    print('#		2. A, D		:	Rotasi kamera terhadap sumbu y.	(Hanya pada mode 3D).	  #')
    print('#		3. Z, X		:	Melakukan zoom pada kamera.				  #')
    print('#		4. Arrow Keys	:	Melakukan pan pada kamera.				  #')
    print('#=================================================================================================#')
    print('#	Silahkan baca README.txt untuk bantuan.							  #')
    print('#=================================================================================================#')
    print()

    print('Pilih mode program (2D / 3D)!')
    program_mode = input('Mode Program: ')
    jumlah_titik = 0

    while program_mode != '2D' and program_mode != '3D':
        print('Input tidak valid!')
        program_mode = input('2D / 3D: ')

    if program_mode == '2D':

        jumlah_titik = int(input('Jumlah titik: '))
        
        for i in range(0, jumlah_titik):
            input_x, input_y = input('Titik ke ' + str(i + 1) + ': ').split()
            input_x = float(input_x)
            input_y = float(input_y)
            titik2D.append([input_x, input_y])

        for point in titik2D:
            nP = []
            for e in point:
                nP.append(e)
            titik2DInitial.append(nP)

        target2D = titik2D.copy()
            
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

            in_animation = not (titik2D == target2D)

            if in_animation:
                if is_rotation:
                    titik2D = AnimationRotational2D(titik2D, target2D, rotation_point2d)
                else:
                    Animate2D(titik2D, target2D)

            Draw2D(titik2D)
            pygame.display.flip()
                
    elif program_mode == '3D':

        for point in titik3D:
            nP = []
            for e in point:
                nP.append(e)

            titik3DInitial.append(nP)

        target3D = titik3D.copy()

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

            in_animation = not (titik3D == target3D)

            if in_animation:
                if is_rotation:
                    titik3D = AnimationRotational3D(titik3D, target3D, rotation_point3d)
                else:
                    Animate3D(titik3D, target3D)

            Draw3D()

            pygame.display.flip()

main()