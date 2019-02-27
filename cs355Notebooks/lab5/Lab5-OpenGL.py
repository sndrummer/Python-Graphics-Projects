import sys

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


cam_x, cam_y, cam_z = 0, 0, -25
rot_deg, rot_x, rot_y, rot_z = 0, 0, 0, 0

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (DISPLAY_WIDTH / DISPLAY_HEIGHT), 0.1, 50.0)

    # DO NOT CHANGE -- THIS SETS THE CAMERA!!!!
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotated(rot_deg, rot_x, rot_y, rot_z)
    glTranslated(cam_x, cam_y, cam_z)

    drawHouse()

    glFlush()


def keyboard(key, x, y):
    global cam_x
    global cam_y
    global cam_z

    global rot_deg
    global rot_x
    global rot_y
    global rot_z

    if key == chr(27):
        import sys
        sys.exit(0)

    if key == b'a':
        cam_x += 1
    if key == b'd':
        cam_x -= 1
    if key == b'w':
        cam_z += 1
    if key == b's':
        cam_z -= 1
    if key == b'r':
        cam_y -= 1
    if key == b'f':
        cam_y += 1
    if key == b'q':
        rot_deg -= 1
        rot_y = 1
    if key == b'e':
        rot_deg += 1
        rot_y = 1


    # Your Code Here

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

# viewing transformation
# TODO 1. Perspecive projection -- to coordinates on the imaging plane
# TODO 2. View Transformation -- to pixel coordinates on the screen

# World to camera - you know the position of the camera in world coordinates: c = (x,y,z)
# And you know the orientation of the camera as given by a set of basic vectors in world coordinates {e1,e2,e3}
# e1 = camera_x, e2 = camera_y, e3 = camera_z

# TODO There are two steps for world to camera
# 1. Translate
# 2. Rotate - into the camera's viewing orientation

# OpenGL concatenates new rotation/translation operations to the right
# of the current one

# ModelView (converts from model coordinates to camera ones)
# Your Code Here

# Field of View = 45 degrees
# Aspect Ratio = Width/height
# Near Clipping plane, 0.1 (when you pass an object)
# Far clipping plane, 50 when you are far enough away it disappears

# glMatrixMode(GL_PROJECTION)
# glLoadIdentity()
#
# glMatrixMode(GL_MODELVIEW)


# HEERE!!!!!!!!!!
# IT LOOKS LIKE THE ORDER THAT YOU DO IT IN IS model = scale * rot * trans
# mvp_matrix = proj_matrix * view_matrix * model_matrix

# glTranslated(x, y, z)
# glRotated(0, 0, 0, 0)

# glTranslate — multiply the current matrix by a translation matrix
# x,y,z --> z we want to zoom out so we do -5
# glTranslated(0.0, 0.0, -1)

# glRotate — multiply the current matrix by a rotation matrix
# Parameters:
# 1. angle - Specifies the angle of rotation, in degrees.
# 2. x,y,z coordinates of a vector
# glRotated(0, 0, 0, 0)
