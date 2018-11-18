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
# pada bidang kartesian 2 dimensi, lalu menerima parameter px dan py yang merupakan
# titik pada bidang kartesian 2 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap titik (px, py).
# Bonus : Menampilkan animasi perpindahan.
def reflect_2d(points, px, py):
    transformation_matrix = [
        [-1, 0],
        [0, -1]
    ]
    newPoints = []

    for point in points:
        newPoint = []
        tx = point[0] - px
        ty = point[1] - py
        newPoint.append((tx * transformation_matrix[0][0] + ty * transformation_matrix[0][1]) + px)
        newPoint.append((tx * transformation_matrix[1][0] + ty * transformation_matrix[1][1]) + py)
        newPoints.append(newPoint)

    return newPoints

# Fungsi ini menerima sebuah array 2 dimensi, yang merupakan kumpulan dari titik-titik
# pada bidang kartesian 2 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap sumbu x.
# Bonus : Menampilkan animasi perpindahan.
def reflect_2d_x(points):
    transformation_matrix = [
        [1, 0],
        [0, -1]
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
# pada bidang kartesian 2 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap sumbu y.
# Bonus : Menampilkan animasi perpindahan.
def reflect_2d_y(points):
    transformation_matrix = [
        [-1, 0],
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
# pada bidang kartesian 2 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap garis y = x.
# Bonus : Menampilkan animasi perpindahan.
def reflect_2d_xy_normal(points):
    transformation_matrix = [
        [0, 1],
        [1, 0]
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
# pada bidang kartesian 2 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap garis y = -x.
# Bonus : Menampilkan animasi perpindahan.
def reflect_2d_xy_invert(points):
    transformation_matrix = [
        [0, -1],
        [-1, 0]
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
# pada bidang kartesian 3 dimensi, lalu menerima parameter px, py, dan pz yang merupakan
# titik pada bidang kartesian 3 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap titik (px, py, pz).
# Bonus : Menampilkan animasi perpindahan.
def reflect_3d(points, px, py, pz):
    transformation_matrix = [
        [-1, 0, 0],
        [0, -1, 0],
        [0, 0, -1]
    ]
    
    newPoints = []

    for point in points:
        newPoint = []
        tx = point[0] - px
        ty = point[1] - py
        tz = point[2] - pz
        newPoint.append((tx * transformation_matrix[0][0] + ty * transformation_matrix[0][1]) + tz * transformation_matrix[0][2] + px)
        newPoint.append((tx * transformation_matrix[1][0] + ty * transformation_matrix[1][1]) + tz * transformation_matrix[1][2] + py)
        newPoint.append((tx * transformation_matrix[2][0] + ty * transformation_matrix[2][1]) + tz * transformation_matrix[2][2] + px)
        newPoints.append(newPoint)

    return newPoints

# Fungsi ini menerima sebuah array 2 dimensi, yang merupakan kumpulan dari titik-titik
# pada bidang kartesian 3 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap sumbu x.
# Bonus : Menampilkan animasi perpindahan.
def reflect_3d_x(points):
    transformation_matrix = [
        [ 1, 0, 0],
        [0, -1, 0],
        [0, 0, -1]
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
# pada bidang kartesian 3 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap sumbu y.
# Bonus : Menampilkan animasi perpindahan.
def reflect_3d_y(points):
    transformation_matrix = [
        [-1, 0, 0],
        [0,  1, 0],
        [0, 0, -1]
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
# pada bidang kartesian 3 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap sumbu z.
# Bonus : Menampilkan animasi perpindahan.
def reflect_3d_z(points):
    transformation_matrix = [
        [-1, 0, 0],
        [0, -1, 0],
        [0, 0,  1]
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