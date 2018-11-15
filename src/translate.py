from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

# Format points untuk 2 dimensi:
# [[x1, y1], [x2, y2], ..., [xn, yn]]
#
# Contoh:
#
#
# USAHAKAN TIAP TITIK DENGAN TITIK SELANJUTNYA HANYA BERBEDA
# SATU POIN, CONTOH:
#  [0, 0] dengan titik [2, 0] hanya berbeda di poin x.

# Format points untuk 3 dimensi:
# [[x1, y1, z1], [x2, y2, z2], ..., [xn, yn, zn]]
#
# Contoh:
#
# P = [
#   [0, 0, 0],
#   [1, 0, 0],
#   [1, 1, 0],
#   [0, 1, 0],
#   [0, 1, 1],
#   [1, 1, 1],
#   [1, 0, 1],
#   [0, 0, 1]
# ]
#
# USAHAKAN TIAP TITIK DENGAN TITIK SELANJUTNYA HANYA BERBEDA
# SATU POIN, CONTOH:
#  [0, 0, 0] dengan titik [2, 0, 0] hanya berbeda di poin x.

# Fungsi ini menerima sebuah array 2 dimensi, yang merupakan kumpulan dari titik-titik
# pada bidang kartesian 2 dimensi, lalu menerima parameter dx dan dy, yang merupakan
# jarak perpindahan pada sumbu x dan sumbu y.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# ditranslasi sejauh dx dan dy.
# Bonus : Menampilkan animasi perpindahan.
def translate_2d(points, dx, dy):
    transform_matrix = [
            [1,0,dx],
            [0,1,dy],
            [0,0,1]
    ]
    translated_points = []
    
    for point in points:
        translated_point = []
        for tmE in transform_matrix:
            sum = 0
            point.append(1) #Dummy element
            for tmEVI, tmEVV in enumerate(tmE):
                sum += tmEVV * point[tmEVI]
            translated_point.append(sum)
        translated_point = translated_point[0:2] #Remove Dummy Element
        translated_points.append(translated_point)
    return translated_points
    
    
# Fungsi ini menerima sebuah array 2 dimensi, yang merupakan kumpulan dari titik-titik
# pada bidang kartesian 3 dimensi, lalu menerima parameter dx, dy, dan dz, yang merupakan
# jarak perpindahan pada sumbu x, sumbu y, dan sumbu z.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# ditranslasi sejauh dx, dy, dan dz.
# Bonus : Menampilkan animasi perpindahan.


def translate_3d(points, dx, dy, dz):
    transform_matrix = [
            [1,0,0,dx],
            [0,1,0,dy],
            [0,0,1,dz],
            [0,0,0,1]]
    translated_points = []
    
    for point in points:
        translated_point = []
        point.append(1) #Dummy element
        for tmE in transform_matrix:
            sum = 0
            for tmEVI, tmEVV in enumerate(tmE):
                sum += tmEVV * point[tmEVI]
            translated_point.append(sum)
        translated_point = translated_point[0:3] #Remove Dummy Element
        translated_points.append(translated_point)
    return translated_points
