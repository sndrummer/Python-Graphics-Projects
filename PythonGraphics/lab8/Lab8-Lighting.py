""" Modified code from Peter Colling Ridge 
	Original found at http://www.petercollingridge.co.uk/pygame-3d-graphics-tutorial
"""

import pygame, math
import numpy as np
import wireframe as wf
import basicShapes as shape


def create_2darray(x, y, z):
    return np.array([[x, y, z]])


def to_1darray(vector2d):
    v = vector2d[0]
    x, y, z = v[0], v[1], v[2]
    return np.array([x, y, z])


def create_vector(x, y, z):
    return np.array([[x],
                     [y],
                     [z]])


def getReflectedDir(l, n):  # get r
    return (2 * np.dot(l, n) * n) - l


def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


def get_xrot_matrix(degrees_rotation):
    radians = math.radians(degrees_rotation)
    c, s = np.cos(radians), np.sin(radians)
    return np.array([[1, 0, 0],
                     [0, c, -s],
                     [0, s, c]])


def get_yrot_matrix(degrees_rotation):
    radians = math.radians(degrees_rotation)
    c, s = np.cos(radians), np.sin(radians)
    return np.array([[c, 0, -s],
                     [0, 1, 0],
                     [s, 0, c]])


def get_zrot_matrix(degrees_rotation):
    radians = math.radians(degrees_rotation)
    c, s = np.cos(radians), np.sin(radians)
    return np.array([[c, -s, 0],
                     [s, c, 0],
                     [0, 0, 1]])


class WireframeViewer(wf.WireframeGroup):
    """ A group of wireframes which can be displayed on a Pygame screen """

    def __init__(self, width, height, name="Wireframe Viewer"):
        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)

        self.wireframes = {}
        self.wireframe_colours = {}
        self.object_to_update = []

        self.displayNodes = False
        self.displayEdges = True
        self.displayFaces = True

        self.perspective = False
        self.eyeX = self.width / 2
        self.eyeY = 100
        self.light_color = np.array([1, 1, 1])
        self.view_dir = np.array([0, 0, -1])
        self.light_dir = np.array([0, 0, -1])

        self.background = (10, 10, 50)
        self.nodeColour = (250, 250, 250)
        self.nodeRadius = 4

        self.control = 0

    def addWireframe(self, name, wireframe):
        self.wireframes[name] = wireframe
        #   If colour is set to None, then wireframe is not displayed
        self.wireframe_colours[name] = (250, 250, 250)

    def addWireframeGroup(self, wireframe_group):
        # Potential danger of overwriting names
        for name, wireframe in wireframe_group.wireframes.items():
            self.addWireframe(name, wireframe)

    def display(self):
        self.screen.fill(self.background)

        for name, wireframe in self.wireframes.items():
            nodes = wireframe.nodes

            if self.displayFaces:
                for (face, object_color) in wireframe.sortedFaces():
                    v1 = (nodes[face[1]] - nodes[face[0]])[:3]
                    v2 = (nodes[face[2]] - nodes[face[0]])[:3]

                    normal = np.cross(v1, v2)
                    normal /= np.linalg.norm(normal)
                    towards_us = np.dot(normal, self.view_dir)

                    # Only draw faces that face us
                    if towards_us > 0:
                        ambient_strength = 0.1
                        diffuse_strength = 0.3
                        specular_strength = 0.6
                        shininess = 2  # m
                        ambient = ambient_strength * self.light_color

                        diff = max(np.dot(normal, self.light_dir), 0.0)
                        diffuse = diff * (diffuse_strength * self.light_color)

                        reflect_dir = getReflectedDir(self.light_dir, normal)

                        spec = max(np.dot(self.view_dir, reflect_dir), 0.0) ** shininess
                        specular = specular_strength * spec * self.light_color

                        light_total = (ambient + diffuse + specular) * object_color
                        pygame.draw.polygon(self.screen, light_total,
                                            [(nodes[node][0], nodes[node][1]) for node in face], 0)

                if self.displayEdges:
                    for (n1, n2) in wireframe.edges:
                        if self.perspective:
                            if wireframe.nodes[n1][2] > -self.perspective and nodes[n2][
                                2] > -self.perspective:
                                z1 = self.perspective / (self.perspective + nodes[n1][2])
                                x1 = self.width / 2 + z1 * (nodes[n1][0] - self.width / 2)
                                y1 = self.height / 2 + z1 * (nodes[n1][1] - self.height / 2)

                                z2 = self.perspective / (self.perspective + nodes[n2][2])
                                x2 = self.width / 2 + z2 * (nodes[n2][0] - self.width / 2)
                                y2 = self.height / 2 + z2 * (nodes[n2][1] - self.height / 2)

                                pygame.draw.aaline(self.screen, object_color, (x1, y1), (x2, y2), 1)
                        else:
                            pygame.draw.aaline(self.screen, object_color,
                                               (nodes[n1][0], nodes[n1][1]),
                                               (nodes[n2][0], nodes[n2][1]), 1)

            if self.displayNodes:
                for node in nodes:
                    pygame.draw.circle(self.screen, object_color, (int(node[0]), int(node[1])),
                                       self.nodeRadius, 0)

        pygame.display.flip()

    def keyEvent(self, key):
        # Your code here
        if key == pygame.K_a:
            print("a is pressed")

            x_val = self.light_dir[0]
            x_val -= .25
            self.light_dir[0] = x_val
            self.light_dir = normalize(self.light_dir)

        if key == pygame.K_d:
            print("d is pressed")
            x_val = self.light_dir[0]
            x_val += .25
            self.light_dir[0] = x_val
            self.light_dir = normalize(self.light_dir)

        if key == pygame.K_w:
            print("w is pressed")
            y_val = self.light_dir[1]
            y_val -= .25
            self.light_dir[1] = y_val
            self.light_dir = normalize(self.light_dir)

        if key == pygame.K_s:
            print("s is pressed")
            y_val = self.light_dir[1]
            y_val += .25
            self.light_dir[1] = y_val
            self.light_dir = normalize(self.light_dir)

        if key == pygame.K_q:
            print("q is pressed")
            v = create_2darray(self.light_dir[0], self.light_dir[1], self.light_dir[2])
            z_rot = get_zrot_matrix(10)
            rotated = np.matmul(v, z_rot)
            self.light_dir = to_1darray(rotated)
            self.light_dir = normalize(self.light_dir)

        if key == pygame.K_e:
            print("e is pressed")
            print("q is pressed")
            v = create_2darray(self.light_dir[0], self.light_dir[1], self.light_dir[2])
            z_rot = get_zrot_matrix(-10)
            rotated = np.matmul(v, z_rot)
            self.light_dir = to_1darray(rotated)
            self.light_dir = normalize(self.light_dir)

        return

    def run(self):
        """ Display wireframe on screen and respond to keydown events """

        running = True
        key_down = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    key_down = event.key
                elif event.type == pygame.KEYUP:
                    key_down = None

            if key_down:
                self.keyEvent(key_down)

            self.display()
            self.update()

        pygame.quit()


resolution = 52
viewer = WireframeViewer(600, 400)
viewer.addWireframe('sphere',
                    shape.Spheroid((300, 200, 20), (160, 160, 160), resolution=resolution))

# Colour ball
faces = viewer.wireframes['sphere'].faces
for i in range(int(resolution / 4)):
    for j in range(resolution * 2 - 4):
        f = i * (resolution * 4 - 8) + j
        faces[f][1][1] = 0
        faces[f][1][2] = 0

viewer.displayEdges = False
viewer.run()
