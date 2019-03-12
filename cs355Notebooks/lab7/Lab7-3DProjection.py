# Import a library of functions called 'pygame'
import pygame
import math
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Line3D():

    def __init__(self, start, end):
        self.start = start
        self.end = end


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_as_hvector(self):
        return np.array([[self.x],
                         [self.y],
                         [self.z],
                         [1]])


def get_scale_matrix(x_scalar, y_scalar, z_scalar):
    return np.matrix([[x_scalar, 0, 0, 0],
                      [0, y_scalar, 0, 0],
                      [0, 0, z_scalar, 0],
                      [0, 0, 0, 1]])


def get_yrot_matrix(degrees_rotation):
    radians = math.radians(degrees_rotation)
    c, s = np.cos(radians), np.sin(radians)
    return np.matrix([[c, 0, -s, 0],
                      [0, 1, 0, 0],
                      [s, 0, c, 0],
                      [0, 0, 0, 1]])


class Camera:
    def __init__(self, x, y, z, deg_rot):
        self.starting_position = Vector3(x, y, z)
        self.starting_rotation = deg_rot
        self.cur_position = Vector3(x, y, z)
        self.cur_rotation = deg_rot
        self.projection_mode = "perspective"
        self.step = 1

    def get_starting_pos(self):
        return self.starting_position.x, self.starting_position.y, self.starting_position.z

    def get_starting_rot(self):
        return self.get_starting_rot()

    def reset_position(self):
        x, y, z = self.get_starting_pos()
        self.cur_position = Vector3(x, y, z)
        self.cur_rotation = self.starting_rotation
        self.projection_mode = "perspective"

    def get_front_facing_xz(self):
        """
        Convert to front facing coordinates
        :return: new x,z tuple
        """
        yaw_radian = math.radians(self.cur_rotation)
        return cam.step * math.sin(yaw_radian) * math.cos(0), cam.step * math.cos(
            yaw_radian) * math.cos(0)

    def get_translation_matrix(self):
        # x, y, z = cam_position.x, cam_position.y, cam_position.z
        return np.matrix([[1, 0, 0, -self.cur_position.x],
                          [0, 1, 0, -self.cur_position.y],
                          [0, 0, 1, -self.cur_position.z],
                          [0, 0, 0, 1]])


class Car:
    def __init__(self, x, y, z):
        self.position = Vector3(x, y, z)
        self.tire_rotation = 0  # in degrees
        # back tires
        self.tire1 = Vector3(-2, 0, -2)
        self.tire2 = Vector3(-2, 0, 2)
        # front tires
        self.tire3 = Vector3(2, 0, -2)
        self.tire4 = Vector3(2, 0, 2)
        self.tires = [self.tire1, self.tire2, self.tire3, self.tire4]


def reset_car():
    global car
    car = Car(0, 1, 0)


def loadOBJ(filename):
    vertices = []
    indices = []
    lines = []

    f = open(filename, "r")
    for line in f:
        t = str.split(line)
        if not t:
            continue
        if t[0] == "v":
            vertices.append(Point3D(float(t[1]), float(t[2]), float(t[3])))

        if t[0] == "f":
            for i in range(1, len(t) - 1):
                index1 = int(str.split(t[i], "/")[0])
                index2 = int(str.split(t[i + 1], "/")[0])
                indices.append((index1, index2))

    f.close()

    # Add faces as lines
    for index_pair in indices:
        index1 = index_pair[0]
        index2 = index_pair[1]
        lines.append(Line3D(vertices[index1 - 1], vertices[index2 - 1]))

    # Find duplicates
    duplicates = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            line1 = lines[i]
            line2 = lines[j]

            # Case 1 -> Starts match
            if line1.start.x == line2.start.x and line1.start.y == line2.start.y and line1.start.z == line2.start.z:
                if line1.end.x == line2.end.x and line1.end.y == line2.end.y and line1.end.z == line2.end.z:
                    duplicates.append(j)
            # Case 2 -> Start matches end
            if line1.start.x == line2.end.x and line1.start.y == line2.end.y and line1.start.z == line2.end.z:
                if line1.end.x == line2.start.x and line1.end.y == line2.start.y and line1.end.z == line2.start.z:
                    duplicates.append(j)

    duplicates = list(set(duplicates))
    duplicates.sort()
    duplicates = duplicates[::-1]

    # Remove duplicates
    for j in range(len(duplicates)):
        del lines[duplicates[j]]

    return lines


def loadHouse():
    house = []
    # Floor
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(5, 0, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 0, 5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(-5, 0, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 0, -5)))
    # Ceiling
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 5, -5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(5, 5, 5), Point3D(-5, 5, 5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(-5, 5, -5)))
    # Walls
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(-5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 5, 5)))
    # Door
    house.append(Line3D(Point3D(-1, 0, 5), Point3D(-1, 3, 5)))
    house.append(Line3D(Point3D(-1, 3, 5), Point3D(1, 3, 5)))
    house.append(Line3D(Point3D(1, 3, 5), Point3D(1, 0, 5)))
    # Roof
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(0, 8, -5)))
    house.append(Line3D(Point3D(0, 8, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(0, 8, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(0, 8, -5)))

    return house


def loadCar():
    car = []
    # Front Side
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-2, 3, 2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(2, 3, 2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(3, 2, 2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 1, 2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(-3, 1, 2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 2, 2)))

    # Back Side
    car.append(Line3D(Point3D(-3, 2, -2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(-2, 3, -2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, -2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 2, -2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(3, 1, -2), Point3D(-3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, -2), Point3D(-3, 2, -2)))

    # Connectors
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-3, 2, -2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 1, -2)))

    return car


def loadTire():
    tire = []
    # Front Side
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-.5, 1, .5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(.5, 1, .5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(1, .5, .5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, -.5, .5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(.5, -1, .5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(-.5, -1, .5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-1, -.5, .5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, .5, .5)))

    # Back Side
    tire.append(Line3D(Point3D(-1, .5, -.5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, -.5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, -.5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, .5, -.5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, -.5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(.5, -1, -.5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, -.5), Point3D(-1, -.5, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, -.5), Point3D(-1, .5, -.5)))

    # Connectors
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-1, .5, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, -.5, -.5)))

    return tire


def get_input(event):
    done = False
    if event.type == pygame.QUIT:  # If user clicked close
        done = True
    elif event.type == pygame.KEYDOWN:
        print("x: ", cam.cur_position.x, " y: ", cam.cur_position.y, "z: ", cam.cur_position.z)
        print("Rotation: ", cam.cur_rotation)
        key = pygame.key

        if event.key == pygame.K_w:
            print("w is pressed")
            new_x, new_z = cam.get_front_facing_xz()
            cam.cur_position.x += new_x
            cam.cur_position.z += new_z
        elif event.key == pygame.K_s:
            print("s is pressed")
            new_x, new_z = cam.get_front_facing_xz()
            cam.cur_position.x -= new_x
            cam.cur_position.z -= new_z

        elif event.key == pygame.K_a:
            print("a is pressed")
            new_z, new_x = cam.get_front_facing_xz()  # swap forward movement for side
            cam.cur_position.x -= new_x
            cam.cur_position.z += new_z
        elif event.key == pygame.K_d:
            print("d is pressed")
            new_x, new_z = cam.get_front_facing_xz()  # swap forward movement for side
            cam.cur_position.x += new_z
            cam.cur_position.z -= new_x

        elif event.key == pygame.K_q:
            print("q is pressed")
            cam.cur_rotation -= 1

        elif event.key == pygame.K_e:
            print("e is pressed")
            cam.cur_rotation += 1

        elif event.key == pygame.K_r:
            print("r is pressed")
            cam.cur_position.y += 1

        elif event.key == pygame.K_f:
            print("f is pressed")
            cam.cur_position.y -= 1

        elif event.key == pygame.K_h:
            print("h is pressed")
            cam.reset_position()
            reset_car()
    return done


# init camera
cam = Camera(0, 0, -10, 0)
# init car
car = Car(0, 1, 0)

camera_matrix = None


def test_xy_clipping(x, y, w):
    """
    Returns true if should be clipped
    :param x: x coordinate of vertex
    :param y: y coordinate of vertex
    :param w: w of camera space point
    :return: True if should be clipped, False if not
    """
    clip = False

    if x < -w or x > w or y < -w or y > w:
        clip = True
    return clip


def test_clipping(camera_space_coordinates1, camera_space_coordinates2):
    x1, y1, z1 = camera_space_coordinates1.item(0), camera_space_coordinates1.item(1), \
                 camera_space_coordinates1.item(2)
    w1 = camera_space_coordinates1.item(3)

    x2, y2, z2 = camera_space_coordinates2.item(0), camera_space_coordinates2.item(
        1), camera_space_coordinates2.item(2)
    w2 = camera_space_coordinates2.item(3)

    # clipping tests
    if x1 < -w1 and x2 < -w2:
        return False
    if x1 > w1 and x2 > w2:
        return False
    if y1 < -w1 and y2 < -w2:
        return False
    if y1 > w1 and y2 > w2:
        return False

    if z1 < -w1 or z2 < -w2:
        return False
    if z1 > w1 or z2 > w2:
        return False

    return True


def get_perspective_matrix(fov_degrees, aspect, near, far):
    """
    Returns the projection matrix for perspective
    Multiply the position of the camera by the matrix that this function returns
    :param fov_degrees: degrees of field of view
    :param aspect: ratio DISPLAY_WIDTH / DISPLAY_HEIGHT
    :param near: near clipping plane
    :param far: far clipping plane
    :return: clip matrix
    """
    radians = math.radians(fov_degrees)

    zoom = 1 / math.tan(radians / 2)
    y_zoom = zoom
    x_zoom = y_zoom / aspect

    z_clip_a = (far + near) / (far - near)
    z_clip_b = (-2 * near * far) / (far - near)

    return np.matrix([[x_zoom, 0, 0, 0],
                      [0, y_zoom, 0, 0],
                      [0, 0, z_clip_a, z_clip_b],
                      [0, 0, 1, 0]])


def get_camera_space_coordinates(perspective, rotation, translation, world_position):
    """
    :param perspective: perspective camera matrix
    :param rotation: camera rotation matrix
    :param translation: camera translation matrix
    :param world_position: position of coordinate in the world
    :return: camera space coordinates
    """
    world_coordinates = world_position.get_as_hvector()
    camera_space_coordinates = perspective * rotation * translation * world_coordinates
    # print("Camera Space coordinates: ", camera_space_coordinates)
    return camera_space_coordinates


def get_canonical_coordinates(camera_space_coordinates):
    """
    :return: camera space coordinates
    """
    w = camera_space_coordinates.item(3)

    canonical_coordinates = camera_space_coordinates / w
    # print("Canonical coordinates: \n", canonical_coordinates)
    return canonical_coordinates


def get_screen_space_coordinates(w_x, w_y):
    """

    :param x:
    :param y:
    :return:
    """
    return None


def to_screen_space(vertex_coordinates):
    """
    Return the x,y coordinates to be drawn onto the screen
    :param vertex_coordinates: canonical space coordinates coordinates a vertex
    :return: x,y tuple of the coordinates to be drawn on the screen
    """
    w = DISPLAY_WIDTH / 2
    h = DISPLAY_HEIGHT / 2
    screen_matrix = np.matrix([[w, 0, w],
                               [0, -h, h],
                               [0, 0, 1]])

    x, y = vertex_coordinates.item(0), vertex_coordinates.item(1)
    xy_matrix = np.array([[x],
                          [y],
                          [1]])
    new_coordinates = screen_matrix * xy_matrix
    return new_coordinates.item(0), new_coordinates.item(1)


DISPLAY_WIDTH = 512
DISPLAY_HEIGHT = 512


def main():
    # Initialize the game engine
    pygame.init()
    global camera_matrix

    # Define the colors we will use in RGB format
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # Set the height and width of the screen
    size = [DISPLAY_WIDTH, DISPLAY_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Shape Drawing")

    # Set needed variables
    done = False
    clock = pygame.time.Clock()
    start = Point(0.0, 0.0)
    end = Point(0.0, 0.0)
    linelist = loadHouse()

    # Loop until the user clicks the close button.
    while not done:
        # This limits the while loop to a max of 100 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(100)

        # Clear the screen and set the screen background
        screen.fill(BLACK)

        # Controller Code#
        #####################################################################

        for event in pygame.event.get():
            done = get_input(event)

        # pressed = pygame.key.get_pressed()
        #
        # if pressed[pygame.K_a]:
        #     count += 1
        #     print("a is pressed ", count)

        # Viewer Code#
        #####################################################################

        # Get Perspective Camera
        # TODO I AM HERE

        # P' = Projection × View × Model × P
        # Step 1 Project
        perspective = get_perspective_matrix(60, (DISPLAY_WIDTH / DISPLAY_HEIGHT), 0.1, 100.0)
        # Step 2 Rotate
        rotation = get_yrot_matrix(cam.cur_rotation)
        # Step 3 Translate
        translation = cam.get_translation_matrix()
        # print("translation matrix: \n", translation)

        # Step 4 put them together
        # camera_matrix = perspective * rotation * translation

        # Step 5 do all real world crap and then translate it with the camera

        # camera_pos = cam.cur_position.get_as_hvector()  # get numpy array of position

        for s in linelist:
            # BOGUS DRAWING PARAMETERS SO YOU CAN SEE THE HOUSE WHEN YOU START UP
            # TODO GET NEW COORDINATES OF LINE
            # 1. Transform and rotate modelview matrix
            # 2. Apply to screen space matrix
            line_start = Vector3(s.start.x, s.start.y, s.start.z)
            line_end = Vector3(s.end.x, s.end.y, s.end.z)
            camera_space_coordinates1 = get_camera_space_coordinates(perspective, rotation,
                                                                     translation, line_start)
            camera_space_coordinates2 = get_camera_space_coordinates(perspective, rotation,
                                                                     translation, line_end)
            # If line doesn't pass clipping test go to next line
            if not test_clipping(camera_space_coordinates1, camera_space_coordinates2):
                continue

            canonical_space_coordinates_start = get_canonical_coordinates(camera_space_coordinates1)
            canonical_space_coordinates_end = get_canonical_coordinates(camera_space_coordinates2)

            start_x, start_y = to_screen_space(canonical_space_coordinates_start)
            end_x, end_y = to_screen_space(canonical_space_coordinates_end)

            pygame.draw.line(screen, RED, (start_x, start_y), (end_x, end_y))

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()

    # Be IDLE friendly
    pygame.quit()


# call main function
main()
