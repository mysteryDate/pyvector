import pdb

import numpy as np
import moviepy.editor as mpy
import gizeh as gz
import random
import colorsys

R = 128

ROTATION_SPEED, DURATION, DEPTH = 1, 10, 2

TRIANGLE, CIRCLE, SQUARE = 0,1,2
# triangle = 0, circle = 1, square = 2
LENGTH = 48
ORDER = [-1 for x in range(LENGTH-3)]
ORDER = [SQUARE, TRIANGLE, CIRCLE] + ORDER
for itr in range(2,LENGTH):
	ORDER[itr] = ORDER[itr - 1]
	while ORDER[itr] == ORDER[itr - 1]:
		ORDER[itr] = random.randrange(3)
print ORDER
# ORDER = [SQUARE, TRIANGLE] * 24
# ORDER = [SQUARE, TRIANGLE, CIRCLE, SQUARE, TRIANGLE, SQUARE, CIRCLE, TRIANGLE, SQUARE, CIRCLE, SQUARE, TRIANGLE]
ORDER = ORDER * DEPTH
# cabcacbacbcab

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
OLD_RADII = []

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

def add_shape(shape, state, itr):
	"""
	Draws the required shape
	"""
	sides = 0
	# weight = ((OLD_RADII[itr%LENGTH]**(2))/R + 5) 
	# weight = (20*np.cos(2*np.pi/LENGTH*itr) + 20) 
	weight = ((abs(itr-LENGTH/2)%LENGTH)**2)/(LENGTH/2)
	print itr, weight
	weight *= state.radius/R #Normalize vs zoom
	fill = colorsys.hls_to_rgb(float(itr)/(LENGTH/2)%1,.5,1)
	if (shape == CIRCLE):
		SHAPES.append(gz.circle(state.radius, stroke=(1,1,1), stroke_width=weight, fill=fill, xy=state.center))
		return
	elif (shape == TRIANGLE):
		sides = 3
	elif (shape == SQUARE):
		sides = 4
	SHAPES.append(gz.regular_polygon(state.radius, sides, stroke=(1,1,1), stroke_width=weight, fill=fill, xy=state.center, angle=state.angle))

state = Translation([R/2, R/2], -np.pi/4, 2**.5/2*R)
OLD_RADII.append(state.radius)
final_state = Translation([R/2, R/2], -np.pi/4, 2**.5/2*R)
add_shape(ORDER[0], state, 0)
for itr in range(1,len(ORDER)):
	old_shape = ORDER[itr - 1]
	new_shape = ORDER[itr]
	state.iterate(old_shape, new_shape)
	OLD_RADII.append(state.radius)
	add_shape(new_shape, state, itr)
	if itr == (len(ORDER) / DEPTH):
		final_state = Translation([state.center[0], state.center[1]], state.angle, state.radius)
group = gz.Group(SHAPES) 
total_zoom = (2**.5/2*R)/final_state.radius - 1 
total_translation = [R/2 - final_state.center[0],R/2 - final_state.center[1]]
total_rotation = -np.pi/4 - final_state.angle

def make_frame(t):
	surface = gz.Surface(R, R)
	# background = gz.square(l=R, xy= [R/2,R/2], fill=(1,1,1))
	# background.draw(surface)
	G = 2 ** (np.log2(total_zoom)*t/DURATION)
	T = [total_translation[0] * t/DURATION, total_translation[1] * t/DURATION]
	theta = total_rotation*t/DURATION
	group.translate([-final_state.center[0],-final_state.center[1]]).scale(G).rotate(theta).translate(
		[final_state.center[0],final_state.center[1]]).translate(T).draw(surface)
	return surface.get_npimage()

# clip = mpy.VideoClip(make_frame, duration=DURATION)
# clip.write_gif("rainbow2.gif",fps=15, opt="OptimizePlus", fuzz=10)


# pdb.set_trace()