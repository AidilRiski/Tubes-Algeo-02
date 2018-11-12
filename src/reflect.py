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
    return 0

# Fungsi ini menerima sebuah array 2 dimensi, yang merupakan kumpulan dari titik-titik
# pada bidang kartesian 2 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap sumbu x.
# Bonus : Menampilkan animasi perpindahan.
def reflect_2d_x(points):
    return 0

# Fungsi ini menerima sebuah array 2 dimensi, yang merupakan kumpulan dari titik-titik
# pada bidang kartesian 2 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap sumbu y.
# Bonus : Menampilkan animasi perpindahan.
def reflect_2d_y(points):
    return 0

# Fungsi ini menerima sebuah array 2 dimensi, yang merupakan kumpulan dari titik-titik
# pada bidang kartesian 2 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap garis y = x.
# Bonus : Menampilkan animasi perpindahan.
def reflect_2d_xy_normal(points):
    return 0

# Fungsi ini menerima sebuah array 2 dimensi, yang merupakan kumpulan dari titik-titik
# pada bidang kartesian 2 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap garis y = -x.
# Bonus : Menampilkan animasi perpindahan.
def reflect_2d_xy_invert(points):
    return 0

# Fungsi ini menerima sebuah array 2 dimensi, yang merupakan kumpulan dari titik-titik
# pada bidang kartesian 3 dimensi, lalu menerima parameter px, py, dan pz yang merupakan
# titik pada bidang kartesian 3 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap titik (px, py, pz).
# Bonus : Menampilkan animasi perpindahan.
def reflect_3d(points, px, py, pz):
    return 0

# Fungsi ini menerima sebuah array 2 dimensi, yang merupakan kumpulan dari titik-titik
# pada bidang kartesian 3 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap sumbu x.
# Bonus : Menampilkan animasi perpindahan.
def reflect_3d_x(points):
    return 0

# Fungsi ini menerima sebuah array 2 dimensi, yang merupakan kumpulan dari titik-titik
# pada bidang kartesian 3 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap sumbu y.
# Bonus : Menampilkan animasi perpindahan.
def reflect_3d_y(points):
    return 0

# Fungsi ini menerima sebuah array 2 dimensi, yang merupakan kumpulan dari titik-titik
# pada bidang kartesian 3 dimensi.
# Fungsi ini mengembalikan nilai dari kumpulan titik-titik pada parameter yang sudah
# direfleksi terhadap sumbu z.
# Bonus : Menampilkan animasi perpindahan.
def reflect_3d_z(points):
    return 0