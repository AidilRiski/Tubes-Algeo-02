from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

# Format points untuk 2 dimensi:
# [[x1, y1], [x2, y2], ..., [xn, yn]]
#
# Contoh:
#
# P = [
#   [0, 0],
#   [1, 0],
#   [1, 1],
#   [0, 1]
# ]
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
# pada bidang kartesian 2 dimensi, lalu menerima parameter yang merupakan matriks
# transformasi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# diubah sesuai matriks transformasi.
# Bonus : Menampilkan animasi perpindahan.
def custom_2d(points, m1, m2, m3, m4):
    transformation_matrix = [
        [float(m1), float(m2)],
        [float(m3), float(m4)]
    ]
    
    newPoints = []

    for point in points:
        newPoint = []
        for tmE in transformation_matrix:
            sum = 0
            for tmEVI, tmEVV in enumerate(tmE):
                sum += tmEVV * point[tmEVI]
            newPoint.append(sum)
        newPoints.append(newPoint)

    return newPoints

# Fungsi ini menerima sebuah array 2 dimensi, yang merupakan kumpulan dari titik-titik
# pada bidang kartesian 3 dimensi, lalu menerima parameter yang merupakan matriks
# transformasi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# diubah sesuai matriks transformasi.
# Bonus : Menampilkan animasi perpindahan.
def custom_3d(points, m1, m2, m3, m4, m5, m6, m7, m8, m9):
    transformation_matrix = [
        [float(m1), float(m2), float(m3)],
        [float(m4), float(m5), float(m6)],
        [float(m7), float(m8), float(m9)]
    ]
    
    newPoints = []

    for point in points:
        newPoint = []
        for tmE in transformation_matrix:
            sum = 0
            for tmEVI, tmEVV in enumerate(tmE):
                sum += tmEVV * point[tmEVI]
            newPoint.append(sum)
        newPoints.append(newPoint)

    return newPoints