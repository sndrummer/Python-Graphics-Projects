import math
import numpy as np


def create_array(x, y, z):
    return np.array([x, y, z])


def getDiffLighting(s, mdiff, l, n):  # cdiff
    return (s * mdiff) * np.dot(l, n)


def getSpecLighting(s, mspec, v, r, m):
    return (s * mspec) * (np.dot(v, r) ** m)


def getReflectedDir(l, n):  # get r
    return (2 * np.dot(l, n) * n) - l


def get_c_amb(s_amb, m_amb):
    return s_amb * m_amb


def get_total_light(spec, diff, amb):
    return spec + diff + amb


class PhongLight:
    def __init__(self, n, l, s, s_amb, v, mdiff, mspec, m):
        self.c_diff = getDiffLighting(s, mdiff, l, n)
        self.r = getReflectedDir(l, n)
        self.c_spec = getSpecLighting(s, mspec, v, self.r, m)
        self.c_amb = get_c_amb(s_amb, mdiff)

    def get_total_light(self):
        return self.c_diff + self.c_spec + self.c_amb


n = create_array(0.58, 0.58, -0.58)  # surface normal
l = create_array(0.53, 0.80, -0.27)  # lighting coming from direction

s = 0.9 * create_array(1.0, 1.0, 0.8)  # direct light strength (coloring)
s_amb = 0.1 * create_array(1.0, 1.0, 0.8)  # ambient light strength (coloring) samb

viewing_dir = create_array(0, 0, -1)  # v = viewing direction
v = viewing_dir

mdiff = create_array(0.1, 0.2, 0.5)  # surface diffuse reflectance coefficients

mspec = create_array(0.5, 0.5, 0.5)  # surface specular reflectance coefficients

surface_spec_glossy_exp = 4
m = surface_spec_glossy_exp

surface_amb_reflectance = mdiff
m_amb = surface_amb_reflectance
# camb = samb ⌦ mamb

print("l: ", l)
print("n: ", n)
print("np.dot(l, n) ==>", np.dot(l, n))
# Problem 1
print("HERE IS THE ANSWER TO NUMBER 1 - c_diff")

c_diff = getDiffLighting(s, mdiff, l, n)
print(c_diff)

# Problem 2
print("HERE IS THE ANSWER TO NUMBER 2 - c_spec")
r = getReflectedDir(l, n)
print("r: ", r)
c_spec = getSpecLighting(s, mspec, v, r, m)
print(c_spec)

# Problem 3
print("HERE IS THE ANSWER TO NUMBER 3 - c_amb")
c_amb = get_c_amb(s_amb, m_amb)
print(c_amb)


# THIS IS CALLED THE PHONG MODEL
# Problem 4
print("HERE IS THE ANSWER TO NUMBER 4 - Total Light")
total = get_total_light(c_spec, c_diff, c_amb)
print(total)

phong = PhongLight(n, l, s, s_amb, v, mdiff, mspec, m)
print("TOTAL FROM PHONG: \n", phong.get_total_light())
