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
# pada bidang kartesian 2 dimensi, lalu menerima parameter factor_k yang merupakan
# konstanta dilatasi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# didilatasi terhadap titik (0, 0) dengan skala factor_k.
# Bonus : Menampilkan animasi perpindahan.
def dilate_2d(points, factor_k):
    transformation_matrix = [
        [factor_k, 0],
        [0, factor_k]
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
# pada bidang kartesian 3 dimensi, lalu menerima parameter factor_k yang merupakan
# konstanta dilatasi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# didilatasi terhadap titik (0, 0, 0) dengan skala factor_k.
# Bonus : Menampilkan animasi perpindahan.
def dilate_3d(points, factor_k):
    transformation_matrix = [
        [factor_k, 0, 0],
        [0, factor_k, 0],
        [0, 0, factor_k]
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