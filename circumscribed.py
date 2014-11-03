import pdb

import numpy as np
import moviepy.editor as mpy
import gizeh as gz
# import colorsys

R = 512

ROTATION_SPEED, DURATION = 1, 2

# abcacb, bacbca, cabcba
# abcacbacbcabc
# Triangle inside circle: 1/1
# Circle inside square: 1/2
# Square inside circle:
    # Square length = (6 - 3*sqrt(3)) * Triangle Raidus
    # Square radius = sqrt(2)/2*(6 - 3*sqrt(3)) * Triangle Raidus
    # Center moves down by: [3*sqrt(3) - 5]/2 * Triangle Raidus
    # Square rotates: pi/4
# Triangle inside a square:
    # Triangle radius = sqrt(2)*sqrt(3)/(3*sin(5pi/12)) * Square Radius
    # Rotation = pi/12
    # Center moves: [1 - sqrt(2)*sqrt(3)/(3*sin(5pi/12))] * Square Radius

surface = gz.Surface(R*2, R*2)

#  Square in a triangle
# tri = gz.regular_polygon(R, 3, stroke=(0,0,0), stroke_width=1, xy=[R, R], angle=-np.pi/2)
# sqr = gz.regular_polygon(np.sqrt(2)/2*(6 - 3*np.sqrt(3))*R, 4, stroke=(0,0,0), stroke_width=1, xy=[R, R + (3*np.sqrt(3) - 5)/2*R], angle=-np.pi/4)
# grp = gz.Group([tri, sqr])

# Triangle in a square, rotated 90 degrees
# sqr = gz.regular_polygon(R, 4, stroke=(0,0,0), stroke_width=1, xy=[R, R], angle=-np.pi/2)
# tri = gz.regular_polygon((np.sqrt(2)*np.sqrt(3))/3*R/np.sin(5*np.pi/12), 3, stroke=(0,0,0), stroke_width=1, xy=[R, R - (1 - np.sqrt(2)*np.sqrt(3)/(3*np.sin(5*np.pi/12)))*R], angle=-np.pi/2)
# grp = gz.Group([sqr, tri])

# Square inside a circle
# cir = gz.circle(R, stroke=(0,0,0), stroke_width=1, xy=[R, R])
# sqr = gz.regular_polygon(R, 4, stroke=(0,0,0), stroke_width=1, xy=[R, R], angle=-np.pi/4)
# grp = gz.Group([cir, sqr])

# Circle inside a square
# sqr = gz.regular_polygon(np.sqrt(2)*R, 4, stroke=(0,0,0), stroke_width=1, xy=[R, R], angle=-np.pi/4)
# cir = gz.circle(R, stroke=(0,0,0), stroke_width=1, xy=[R, R])
# grp = gz.Group([sqr, cir])

# Triangle inside a circle
# cir = gz.circle(R, stroke=(0,0,0), stroke_width=1, xy=[R, R])
# tri = gz.regular_polygon(R, 3, stroke=(0,0,0), stroke_width=1, xy=[R, R], angle=-np.pi/2)
# grp = gz.Group([cir, tri])

# Circle inside a triangle
# tri = gz.regular_polygon(R, 3, stroke=(0,0,0), stroke_width=1, xy=[R, R], angle=-np.pi/2)
# cir = gz.circle(R/2, stroke=(0,0,0), stroke_width=1, xy=[R, R])
# grp = gz.Group([cir, tri])

def draw_pointer_circles(radius, center, angle):
	x1 = center[0]
	y1 = center[1]
	x2 = center[0] + radius*np.cos(angle)
	y2 = center[1] + radius*np.sin(angle)
	c1 = gz.circle(radius/10, fill=(0,0,0), xy=[x1, y1])
	c2 = gz.circle(radius/10, fill=(0,0,0), xy=[x2, y2])
	# c1.draw(surface)
	c2.draw(surface)

# Let's try summach
centerX = R
centerY = R
center = [R, R]
ang = 0
# draw_pointer_circles(R, center, ang)
ang = -np.pi/2
draw_pointer_circles(R, center, ang)
print [centerX, centerY], ang, R
tri = gz.regular_polygon(R, 3, stroke=(0,0,0), stroke_width=1, xy=[centerX, centerY], angle=ang)
R /= 2
draw_pointer_circles(R, center, ang)
print [centerX, centerY], ang, R
cir = gz.circle(R, stroke=(0,0,0), stroke_width=1, xy=[centerX, centerY])
ang += np.pi/4
draw_pointer_circles(R, [centerX, centerY], ang)
print [centerX, centerY], ang, R
sqr = gz.regular_polygon(R, 4, stroke=(0,0,0), stroke_width=1, xy=[centerX, centerY], angle=ang)
d = (1 - np.sqrt(2)*np.sqrt(3)/(3*np.sin(5*np.pi/12)))*R
centerX += d * np.cos(ang)
centerY += d * np.sin(ang)
R *= np.sqrt(2)*np.sqrt(3)/(3*np.sin(5*np.pi/12))
draw_pointer_circles(R, [centerX, centerY], ang)
print [centerX, centerY], ang, R
tri2 = gz.regular_polygon(R, 3, stroke=(0,0,0), stroke_width=1, xy=[centerX, centerY], angle=ang)
d = -(3*np.sqrt(3) - 5)/2*R
centerX += d * np.cos(ang)
centerY += d * np.sin(ang)
ang += np.pi/4
R *= np.sqrt(2)/2*(6 - 3*np.sqrt(3))
draw_pointer_circles(R, [centerX, centerY], ang)
print [centerX, centerY], ang, R
sqr2 = gz.regular_polygon(R, 4, stroke=(0,0,0), stroke_width=1, xy=[centerX, centerY], angle=ang)
R *= 2**.5/2
draw_pointer_circles(R, [centerX, centerY], ang)
print [centerX, centerY], ang, R
cir2 = gz.circle(R, stroke=(0,0,0), stroke_width=1, xy=[centerX, centerY])
ang += 5*np.pi/12
draw_pointer_circles(R, [centerX, centerY], ang)
print [centerX, centerY], ang, R
tri3 = gz.regular_polygon(R, 3, stroke=(0,0,0), stroke_width=1, xy=[centerX, centerY], angle=ang)
d = -(3*np.sqrt(3) - 5)/2*R
centerX += d * np.cos(ang)
centerY += d * np.sin(ang)
ang += np.pi/4
R *= np.sqrt(2)/2*(6 - 3*np.sqrt(3))
draw_pointer_circles(R, [centerX, centerY], ang)
print [centerX, centerY], ang, R
sqr3 = gz.regular_polygon(R, 4, stroke=(0,0,0), stroke_width=1, xy=[centerX, centerY], angle=ang)
R *= 2**0.5/2
draw_pointer_circles(R, [centerX, centerY], ang)
print [centerX, centerY], ang, R
cir3 = gz.circle(R, stroke=(0,0,0), stroke_width=1, xy=[centerX, centerY])
ang += np.pi/4
draw_pointer_circles(R, [centerX, centerY], ang)
print [centerX, centerY], ang, R
sqr4 = gz.regular_polygon(R, 4, stroke=(0,0,0), stroke_width=1, xy=[centerX, centerY], angle=ang)
d = (1 - np.sqrt(2)*np.sqrt(3)/(3*np.sin(5*np.pi/12)))*R
centerX += d * np.cos(ang)
centerY += d * np.sin(ang)
R *= np.sqrt(2)*np.sqrt(3)/(3*np.sin(5*np.pi/12))
draw_pointer_circles(R, [centerX, centerY], ang)
print [centerX, centerY], ang, R
tri4 = gz.regular_polygon(R, 3, stroke=(0,0,0), stroke_width=1, xy=[centerX, centerY], angle=ang)
R /= 2
draw_pointer_circles(R, [centerX, centerY], ang)
cir4 = gz.circle(R, stroke=(0,0,0), stroke_width=1, xy=[centerX, centerY])
ang += np.pi/4
draw_pointer_circles(R, [centerX, centerY], ang)
print [centerX, centerY], ang, R
sqr5 = gz.regular_polygon(R, 4, stroke=(0,0,0), stroke_width=1, xy=[centerX, centerY], angle=ang)
# ... and that's as far as I'm gonna get

grp = gz.Group([tri,cir,sqr, tri2, sqr2, cir2, tri3, sqr3, cir3, sqr4, tri4, cir4, sqr5])
# pdb.set_trace()

grp.draw(surface)

surface.write_to_png("cirumc.png")
