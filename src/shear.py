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
# konstanta shear.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# di-shear terhadap sumbu x dengan skala factor_k.
# Bonus : Menampilkan animasi perpindahan.
def shear_2d_x(points, factor_k):
    transformation_matrix = [
        [1, factor_k],
        [0, 1]
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
# pada bidang kartesian 2 dimensi, lalu menerima parameter factor_k yang merupakan
# konstanta shear.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# di-shear terhadap sumbu y dengan skala factor_k.
# Bonus : Menampilkan animasi perpindahan.
def shear_2d_y(points, factor_k):
    transformation_matrix = [
        [1, 0],
        [factor_k, 1]
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
# konstanta shear.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# di-shear terhadap sumbu x dengan skala factor_k.
# Bonus : Menampilkan animasi perpindahan.
def shear_3d_x(points, factor_k):
    transformation_matrix = [
        [1, 0, 0],
        [factor_k, 1, 0],
        [factor_k, 0, 1]
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
# konstanta shear.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# di-shear terhadap sumbu y dengan skala factor_k.
# Bonus : Menampilkan animasi perpindahan.
def shear_3d_y(points, factor_k):
    transformation_matrix = [
        [1, factor_k, 0],
        [0, 1, 0],
        [0, factor_k, 1]
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
# konstanta shear.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# di-shear terhadap sumbu z dengan skala factor_k.
# Bonus : Menampilkan animasi perpindahan.
def shear_3d_z(points, factor_k):
    transformation_matrix = [
        [1, 0, factor_k],
        [0, 1, factor_k],
        [0, 0, 1]
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