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


def drawAxisOfRotation():
    #glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(2.5)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)

    glVertex3f(0, -15, 0)  # glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(0, 35.0, 0)  # glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(0, 35.0, 0)  # glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(0, -15, 0)  # glVertex3f(-5.0, 0.0, -5.0)

    glColor3f(0.0, 1.0, 0.0)
    # axis
    glVertex3f(30.0, -15.0, 40.0)  # glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(30.0, 35.0, 40.0)  # glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(30.0, 35.0, 40.0)  # glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(30.0, -15.0, 40.0)  # glVertex3f(-5.0, 0.0, -5.0)

    glEnd()


def drawTestShape():
    #glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(2.5)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)

    # SAMPLE SQUARE
    glVertex3f(10.0, 15.0, 0.0)  # glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(25, 15, 0)  # glVertex3f(5, 0, -5)
    glVertex3f(25, 15, 0)  # glVertex3f(5, 0, -5)
    glVertex3f(25, 15, 10)  # glVertex3f(5, 0, 5)
    glVertex3f(25, 15, 10)  # glVertex3f(5, 0, 5)
    glVertex3f(10, 15, 10)  # glVertex3f(-5, 0, 5)
    glVertex3f(10, 15, 10)  # glVertex3f(-5, 0, 5)
    glVertex3f(10.0, 15.0, 0.0)  # glVertex3f(-5, 0, -5)

    glEnd()

    # glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.5)
    # draw two points
    glBegin(GL_POINTS)

    glVertex3f(10.0, 15.0, 0.0)

    # Result of rotation
    glColor3f(0.0, 1.0, 0.0)

    # [[37.07106781]
    #  [15.]
    #  [32.92893219]
    #  [1.]]
    glVertex3f(37.07106781, 15.0, 32.92893219)

    glEnd()


cam_x, cam_y, cam_z = -10, -15, -20
rot_deg = 0
move_speed = 1
projection_mode = "perspective"

transform = False


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if projection_mode == "ortho":
        width_ratio = DISPLAY_WIDTH / DISPLAY_HEIGHT
        zoom = -cam_z
        if zoom > 0:
            glOrtho(-zoom * width_ratio, zoom * width_ratio, -zoom, zoom, .5, 100)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            glRotated(rot_deg, 0, 1, 0)
            glTranslated(cam_x, cam_y, cam_z)

    else:
        gluPerspective(55, (DISPLAY_WIDTH / DISPLAY_HEIGHT), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glRotated(rot_deg, 0, 1, 0)
        glTranslated(cam_x, cam_y, cam_z)


    drawTestShape()

    drawAxisOfRotation()


    if transform:
        shape_offset = [30, 0, 40]
        # problem 1
        transform_shape(shape_offset, 40)

    glFlush()


def transform_shape(shape_offset, rotation):
    glPushMatrix()
    glTranslated(shape_offset[0], shape_offset[1], shape_offset[2])
    glRotated(rotation, 0, 1, 0)
    drawTestShape()
    glPopMatrix()


def get_front_facing_xz():
    """
    Convert to front facing coordinates
    :return: new x,z tuple
    """
    yaw_radian = math.radians(rot_deg)
    return move_speed * math.sin(yaw_radian) * math.cos(0), move_speed * math.cos(
        yaw_radian) * math.cos(0)


def transform_boolean():
    global transform
    transform = not transform


def keyboard(key, x, y):
    global cam_x
    global cam_y
    global cam_z
    global projection_mode
    global transform

    global rot_deg

    if key == chr(27):
        import sys
        sys.exit(0)

    if key == b'a':
        new_z, new_x = get_front_facing_xz()  # swap forward movement for side
        cam_x += new_x
        cam_z += new_z
    if key == b'd':
        new_x, new_z = get_front_facing_xz()  # swap forward movement for side
        cam_x -= new_z
        cam_z -= new_x
    if key == b'w':
        new_x, new_z = get_front_facing_xz()
        cam_x -= new_x
        cam_z += new_z
    if key == b's':
        new_x, new_z = get_front_facing_xz()
        cam_x += new_x
        cam_z -= new_z

    if key == b'q':
        rot_deg -= 1
    if key == b'e':
        rot_deg += 1

    if key == b'r':
        cam_y -= 1
    if key == b'f':
        cam_y += 1

    if key == b'h':  # go home
        cam_x = 0
        cam_y = 0
        cam_z = -15
        rot_deg = 0
    if key == b'p':
        projection_mode = "perspective"
    if key == b'o':
        projection_mode = "ortho"

    if key == b'c':
        cam_x, cam_y, cam_z = -37, -15, -40
    if key == b'v':
        cam_x, cam_y, cam_z = -10, -15, -20

    if key == b't':
        transform_boolean()

    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(int(DISPLAY_WIDTH), int(DISPLAY_HEIGHT))
glutInitWindowPosition(100, 100)
glutCreateWindow(b'OpenGL Lab')
init()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMainLoop()
