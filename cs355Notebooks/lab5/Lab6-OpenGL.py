import sys
import math

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GL import glOrtho
    from OpenGL.GLU import gluPerspective
    from OpenGL.GL import glRotated
    from OpenGL.GL import glTranslated
    from OpenGL.GL import glLoadIdentity
    from OpenGL.GL import glMatrixMode
    from OpenGL.GL import GL_MODELVIEW
    from OpenGL.GL import GL_PROJECTION
except:
    print("ERROR: PyOpenGL not installed properly. ")

DISPLAY_WIDTH = 500.0
DISPLAY_HEIGHT = 500.0


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


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


def drawCar():
    glLineWidth(2.5)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    # Front Side
    glVertex3f(-3, 2, 2)
    glVertex3f(-2, 3, 2)
    glVertex3f(-2, 3, 2)
    glVertex3f(2, 3, 2)
    glVertex3f(2, 3, 2)
    glVertex3f(3, 2, 2)
    glVertex3f(3, 2, 2)
    glVertex3f(3, 1, 2)
    glVertex3f(3, 1, 2)
    glVertex3f(-3, 1, 2)
    glVertex3f(-3, 1, 2)
    glVertex3f(-3, 2, 2)
    # Back Side
    glVertex3f(-3, 2, -2)
    glVertex3f(-2, 3, -2)
    glVertex3f(-2, 3, -2)
    glVertex3f(2, 3, -2)
    glVertex3f(2, 3, -2)
    glVertex3f(3, 2, -2)
    glVertex3f(3, 2, -2)
    glVertex3f(3, 1, -2)
    glVertex3f(3, 1, -2)
    glVertex3f(-3, 1, -2)
    glVertex3f(-3, 1, -2)
    glVertex3f(-3, 2, -2)
    # Connectors
    glVertex3f(-3, 2, 2)
    glVertex3f(-3, 2, -2)
    glVertex3f(-2, 3, 2)
    glVertex3f(-2, 3, -2)
    glVertex3f(2, 3, 2)
    glVertex3f(2, 3, -2)
    glVertex3f(3, 2, 2)
    glVertex3f(3, 2, -2)
    glVertex3f(3, 1, 2)
    glVertex3f(3, 1, -2)
    glVertex3f(-3, 1, 2)
    glVertex3f(-3, 1, -2)
    glEnd()


def drawTire():
    glLineWidth(2.5)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    # Front Side
    glVertex3f(-1, .5, .5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(.5, 1, .5)
    glVertex3f(.5, 1, .5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, -.5, .5)
    glVertex3f(1, -.5, .5)
    glVertex3f(.5, -1, .5)
    glVertex3f(.5, -1, .5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, .5, .5)
    # Back Side
    glVertex3f(-1, .5, -.5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-1, -.5, -.5)
    glVertex3f(-1, -.5, -.5)
    glVertex3f(-1, .5, -.5)
    # Connectors
    glVertex3f(-1, .5, .5)
    glVertex3f(-1, .5, -.5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(.5, 1, .5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, -.5, .5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(.5, -1, .5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, -.5, -.5)
    glEnd()


def drawHouse():
    glLineWidth(2.5)
    glColor3f(1.0, 0.0, 0.0)
    # Floor
    glBegin(GL_LINES)
    glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, -5)
    # Ceiling
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, -5)
    # Walls
    glVertex3f(-5, 0, -5)
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 5, 5)
    # Door
    glVertex3f(-1, 0, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 0, 5)
    # Roof
    glVertex3f(-5, 5, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, -5)
    glEnd()


# init camera
cam = Camera(8, 0, -10, 37)
# init car
car = Car(0, 1, 0)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if cam.projection_mode == "ortho":
        width_ratio = DISPLAY_WIDTH / DISPLAY_HEIGHT
        zoom = -cam.cur_position.z
        if zoom > 0:
            glOrtho(-zoom * width_ratio, zoom * width_ratio, -zoom, zoom, .5, 100)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            glRotated(cam.cur_rotation, 0, 1, 0)
            glTranslated(cam.cur_position.x, cam.cur_position.y, cam.cur_position.z)

    else:
        gluPerspective(60, (DISPLAY_WIDTH / DISPLAY_HEIGHT), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glRotated(cam.cur_rotation, 0, 1, 0)
        glTranslated(cam.cur_position.x, cam.cur_position.y, cam.cur_position.z)

    draw_neighborhood()
    animate_car()

    glFlush()


def animate_car():
    """Use push so that you can apply some transformations at the same time?
       1. Push the matrix from stack
       2. Translate to position
       3. Rotate it
       4. Draw it
       5. Pop the matrix
       """
    # move car along
    glPushMatrix()
    glTranslated(car.position.x, car.position.y, car.position.z)
    drawCar()

    # translate and rotate tires
    for tire in car.tires:
        glPushMatrix()
        glTranslated(tire.x, tire.y, tire.z)
        car.tire_rotation -= .2
        glRotated(car.tire_rotation, 0, 0, 1)
        drawTire()
        glPopMatrix()

    glPopMatrix()


def reset_car():
    global car
    car = Car(0, 1, 0)


def transform_house(house_offset, rotation):
    glPushMatrix()
    glTranslated(house_offset[0], house_offset[1], house_offset[2])
    glRotated(rotation, 0, 1, 0)
    drawHouse()
    glPopMatrix()


def draw_neighborhood():
    # First row of houses
    house_offset = [0, 0, -25]
    for i in range(5):
        transform_house(house_offset, 0)
        house_offset[0] += 15

    # Second row of houses
    house_offset = [0, 0, 16]
    for i in range(5):
        transform_house(house_offset, 180)
        house_offset[0] += 15

    # houses at the end of the street
    house_offset = [-18, 0, -12]
    transform_house(house_offset, 90)

    house_offset = [-18, 0, 2]
    transform_house(house_offset, 90)


def get_front_facing_xz():
    """
    Convert to front facing coordinates
    :return: new x,z tuple
    """
    yaw_radian = math.radians(cam.cur_rotation)
    return cam.step * math.sin(yaw_radian) * math.cos(0), cam.step * math.cos(
        yaw_radian) * math.cos(0)


def keyboard(key, x, y):
    print("x: ", cam.cur_position.x, " y: ", cam.cur_position.y, "z: ", cam.cur_position.z)
    print("Rotation: ", cam.cur_rotation)

    if key == chr(27):
        import sys
        sys.exit(0)

    if key == b'a':
        new_z, new_x = get_front_facing_xz()  # swap forward movement for side
        cam.cur_position.x += new_x
        cam.cur_position.z += new_z
    if key == b'd':
        new_x, new_z = get_front_facing_xz()  # swap forward movement for side
        cam.cur_position.x -= new_z
        cam.cur_position.z -= new_x
    if key == b'w':
        new_x, new_z = get_front_facing_xz()
        cam.cur_position.x -= new_x
        cam.cur_position.z += new_z
    if key == b's':
        new_x, new_z = get_front_facing_xz()
        cam.cur_position.x += new_x
        cam.cur_position.z -= new_z

    if key == b'q':
        cam.cur_rotation -= 1
    if key == b'e':
        cam.cur_rotation += 1

    if key == b'r':
        cam.cur_position.y -= 1
    if key == b'f':
        cam.cur_position.y += 1

    if key == b'h':
        cam.reset_position()
        reset_car()
    if key == b'p':
        cam.projection_mode = "perspective"
    if key == b'o':
        cam.projection_mode = "ortho"

    glutPostRedisplay()


def move_car(value):
    car.position.x += .02
    display()
    glutTimerFunc(10, move_car, 1)


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(int(DISPLAY_WIDTH), int(DISPLAY_HEIGHT))
glutInitWindowPosition(100, 100)
glutCreateWindow(b'OpenGL Lab')
init()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutTimerFunc(1000, move_car, 1)
glutMainLoop()
