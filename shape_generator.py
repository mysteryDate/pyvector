import pdb

import numpy as np
import moviepy.editor as mpy
import gizeh as gz
# import colorsys
from scipy import misc

R = 1024
surface = gz.Surface(R*2, R*2)

ROTATION_SPEED, DURATION = 1, 2

TRIANGLE, CIRCLE, SQUARE = 0,1,2
# triangle = 0, circle = 1, square = 2
# ORDER = [CIRCLE]
ORDER = [TRIANGLE, CIRCLE, SQUARE, TRIANGLE, SQUARE, CIRCLE, TRIANGLE, SQUARE, CIRCLE, SQUARE]
ORDER = ORDER * 2
# abcacbacbcabc

# Scaling for [old_shape][new_shape]
# Translate -> Rotate -> Scale, don't ask why, yet
SCALE_MATRIX = [
	[1, 									0.5, 			np.sqrt(2)*(6-3*np.sqrt(3))/2],
	[1,										1,				1],
	[np.sqrt(6)/(3*np.sin(5*np.pi/12)), 	np.sqrt(2)/2, 	1]]

TRANSLATE_MATRIX = [
	[0, 									0, 	-(3*np.sqrt(3)-5)/2],
	[0, 									0, 	0],
	[1-np.sqrt(6)/(3*np.sin(5*np.pi/12)), 	0, 	0]]


ROTATION_MATRIX = [
	[0,				0,	np.pi/4],
	[5*np.pi/12, 	0,	np.pi/4],
	[0, 			0, 	0]]

SHAPES = []

class Translation:
    """
    A text message received into the mailbox
    """
    def __init__(self, center, angle, radius):
        self.center = center # The x,y coordinates of the center
        self.angle = angle
        self.radius = radius

    def display(self):
    	print self.center, self.angle, self.radius

    def iterate(self, old_shape, new_shape):
    	"""
    	Returns a tuple (center, angle, radius) for the transformation
    	"""
    	# Translate
    	distance = TRANSLATE_MATRIX[old_shape][new_shape] * self.radius
    	self.center[0] += distance * np.cos(self.angle)
    	self.center[1] += distance * np.sin(self.angle)
    	# Rotate
    	self.angle += ROTATION_MATRIX[old_shape][new_shape]
    	# Scale
    	self.radius *= SCALE_MATRIX[old_shape][new_shape]

grp2 = []
fill = (0,0,0,1.0/255)
def draw_pointer_circles(radius, center, angle):
	x2 = center[0] + radius*np.cos(angle)
	y2 = center[1] + radius*np.sin(angle)
	c2 = gz.circle(radius/10, fill=fill, xy=[x2, y2])
	# c1.draw(surface)
	# c2.draw(surface)
	grp2.append(c2)

def add_shape(shape, state, itr):
	"""
	Draws the required shape
	"""
	sides = 0
	weight = state.radius/R * 2.5 + 0.5
	# if itr % 2 == 0:
	# 	fill = (0,0,0)
	# else: fill = (1,1,1)
	if (shape == CIRCLE):
		SHAPES.append(gz.circle(state.radius, stroke=(0,0,0), stroke_width=0, xy=state.center, fill = fill))
		return
	elif (shape == TRIANGLE):
		sides = 3
	elif (shape == SQUARE):
		sides = 4
	SHAPES.append(gz.regular_polygon(state.radius, sides, stroke=(0,0,0), stroke_width=0, xy=state.center, fill = fill, angle=state.angle))

background = gz.square(l=R*2, xy= [R,R], fill=(1,1,1))
background.draw(surface)
state = Translation([R, R+R/4], -np.pi/2, R)
add_shape(ORDER[0], state, 0)
draw_pointer_circles(state.radius, state.center, state.angle)
for itr in range(1,len(ORDER)):
	old_shape = ORDER[itr - 1]
	new_shape = ORDER[itr]
	state.iterate(old_shape, new_shape)
	add_shape(new_shape, state, itr)
	draw_pointer_circles(state.radius, state.center, state.angle)
group = gz.Group(SHAPES) 

group2 = gz.Group(grp2)
group.draw(surface)
group2.draw(surface)
im = 255*((surface.get_npimage()) % 2)
misc.imsave('autogen.png', im)

# pdb.set_trace()