""" Modified code from Peter Colling Ridge 
	Original found at http://www.petercollingridge.co.uk/pygame-3d-graphics-tutorial
"""

import pygame, math
import numpy as np
import wireframe as wf
import basicShapes as shape


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
    def __init__(self, normal, lighting_dir, light_color, amb_color, view_direction, mdiff, mspec,
                 m):
        self.c_diff = getDiffLighting(light_color, mdiff, lighting_dir, normal)
        self.r = getReflectedDir(lighting_dir, normal)
        self.c_spec = getSpecLighting(light_color, mspec, view_direction, self.r, m)
        self.c_amb = get_c_amb(amb_color, mdiff)

    def get_total_light(self):
        return self.c_diff + self.c_spec + self.c_amb


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
                        diffuse_strength = 0.2
                        specular_strength = 0.7



                        #ambient = self.light_color * (ambient_strength * object_color)
                        ambient = ambient_strength * self.light_color


                        #diff = np.dot(normal, self.light_dir)

                        diff = max(np.dot(normal, self.light_dir), 0.0)
                        diffuse = diff * (diffuse_strength * self.light_color)

                        print("diff: ", diff)
                        #lighting_dir, normal
                        reflect_dir  = getReflectedDir(self.light_dir, normal)

                        spec = max(np.dot(self.view_dir, reflect_dir), 0.0) ** 4
                        specular = specular_strength * spec * self.light_color


                        light_total = (ambient + diffuse + specular) * object_color
                        print("light total: ", light_total)
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
                            pygame.draw.aaline(self.screen, object_color, (nodes[n1][0], nodes[n1][1]),
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
        if key == pygame.K_d:
            print("d is pressed")
        if key == pygame.K_w:
            print("w is pressed")
        if key == pygame.K_s:
            print("s is pressed")
        if key == pygame.K_q:
            print("q is pressed")
        if key == pygame.K_e:
            print("e is pressed")

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

# ambient = self.light_color * (m_ambient * colour)
#                         s_amb = self.light_color
#                         m_amb = m_ambient * colour
#
#                         m_diff = m_amb  # surface diffuse reflectance coefficients
#
#                         m_spec = create_array(0.9, 0.9, 0.9)  # surface specular reflectance coefficients
#                         m = 4
#
#                         s = self.light_color * (m_direct * colour)
#                         print("s: ", s)
#                         print("light color: ", self.light_color)
#                         diff = getDiffLighting(s, m_diff, self.light_vector, normal)  # s mdiff l n
#                         r = getReflectedDir(self.light_vector, normal)
#                         #print("r: ", r)
#                         spec = getSpecLighting(s, m_spec, self.view_vector, r, m)
